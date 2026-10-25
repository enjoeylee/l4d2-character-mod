"""Extract public Bilibili lesson evidence; OCR is a draft, not verified instruction.

Uses existing ffmpeg/ffprobe, Pillow, OpenCV and RapidOCR. No browser cookies,
login bypass, installers, global configuration, or automatic skill updates.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


HEADERS = {"User-Agent": "Mozilla/5.0", "Referer": "https://www.bilibili.com/"}


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def api(path, **params):
    req = Request("https://api.bilibili.com" + path + "?" + urlencode(params), headers=HEADERS)
    with urlopen(req, timeout=40) as response:
        payload = json.load(response)
    if payload.get("code") != 0:
        raise RuntimeError(f"{path}: {payload.get('code')} {payload.get('message')}")
    return payload["data"]


def fetch(bvid, folder, page=None):
    metadata_path = folder / "metadata.json"
    if metadata_path.exists():
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        if metadata.get("bvid") != bvid or metadata.get("page") != page:
            raise RuntimeError("Cached metadata does not match requested BVID/page.")
    else:
        raw = api("/x/web-interface/view", bvid=bvid)
        pages = raw.get("pages", [])
        if page is None and len(pages) != 1:
            raise RuntimeError("Multipart video: explicitly select --page N; each part is recorded separately.")
        selected = next((p for p in pages if p["page"] == (page or 1)), None)
        if selected is None:
            raise RuntimeError(f"Requested page {page} is not present.")
        metadata = {k: raw.get(k) for k in ("bvid", "aid", "cid", "title", "desc", "duration", "pubdate", "pages")}
        metadata.update(cid=selected["cid"], duration=selected["duration"], page=page,
                        part=selected["part"])
        metadata["owner"] = {k: raw["owner"].get(k) for k in ("mid", "name")}
        metadata["url"] = f"https://www.bilibili.com/video/{bvid}/" + (f"?p={page}" if page else "")
        metadata["retrieved_at"] = datetime.now(timezone.utc).isoformat()
        player = api("/x/player/v2", bvid=bvid, cid=metadata["cid"])
        metadata["subtitle_tracks"] = player.get("subtitle", {}).get("subtitles", [])
        write_json(metadata_path, metadata)
        for i, track in enumerate(metadata["subtitle_tracks"]):
            url = track.get("subtitle_url", "")
            if url.startswith("//"):
                url = "https:" + url
            if url:
                with urlopen(Request(url, headers=HEADERS), timeout=40) as response:
                    write_json(folder / f"subtitle_{i}.json", json.load(response))
    media = folder / "media.mp4"
    if not media.exists():
        play = api("/x/player/playurl", bvid=bvid, cid=metadata["cid"], qn=64, fnval=0, fnver=0, fourk=1)
        streams = play.get("durl", [])
        if len(streams) != 1:
            raise RuntimeError("No single public progressive stream; stop and obtain accessible source media.")
        partial = folder / "media.mp4.part"
        with urlopen(Request(streams[0]["url"], headers=HEADERS), timeout=60) as response, partial.open("wb") as target:
            shutil.copyfileobj(response, target)
        expected = streams[0].get("size")
        if expected and partial.stat().st_size != expected:
            raise RuntimeError("Media download incomplete; .part retained.")
        partial.rename(media)
    probe = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,width,height:format=duration,size", "-of", "json", str(media)], check=True, capture_output=True, text=True)
    measured = json.loads(probe.stdout)
    if abs(float(measured["format"]["duration"]) - metadata["duration"]) > 3:
        raise RuntimeError("Downloaded duration differs from source metadata.")
    write_json(folder / "media_probe.json", measured)
    print(f"{bvid} P{page or 1}: media ready, {metadata['duration']} seconds", flush=True)
    return metadata


def frames(folder, interval):
    import cv2
    from PIL import Image, ImageDraw

    directory = folder / "frames"
    directory.mkdir(exist_ok=True)
    capture = cv2.VideoCapture(str(folder / "media.mp4"))
    if not capture.isOpened():
        raise RuntimeError("Cannot open media")
    duration = capture.get(cv2.CAP_PROP_FRAME_COUNT) / capture.get(cv2.CAP_PROP_FPS)
    records = []
    for second in range(0, int(duration), interval):
        destination = directory / f"{second:05d}.jpg"
        if not destination.exists():
            capture.set(cv2.CAP_PROP_POS_MSEC, second * 1000)
            ok, frame = capture.read()
            if not ok:
                raise RuntimeError(f"Cannot decode frame at {second}")
            # imencode/tofile supports non-ASCII Windows paths.
            cv2.imencode(".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, 94])[1].tofile(str(destination))
        records.append({"seconds": second, "file": destination.name})
    capture.release()
    write_json(directory / "index.json", {"interval_seconds": interval, "frames": records})
    sheets = folder / "sheets"
    sheets.mkdir(exist_ok=True)
    for start in range(0, len(records), 12):
        page = Image.new("RGB", (1920, 1560), "#171717")
        draw = ImageDraw.Draw(page)
        for i, row in enumerate(records[start:start + 12]):
            with Image.open(directory / row["file"]) as source:
                source.thumbnail((640, 360))
                x, y = (i % 3) * 640, (i // 3) * 390
                page.paste(source, (x, y + 30))
                draw.text((x + 8, y + 7), f"{row['seconds']//60:02d}:{row['seconds']%60:02d}", fill="white")
        page.save(sheets / f"sheet_{start//12 + 1:02d}.jpg", quality=90)
    print(f"{folder.name}: {len(records)} frames ready", flush=True)


def ocr(folder, crop_fraction):
    import cv2
    import numpy as np
    from rapidocr_onnxruntime import RapidOCR

    engine = RapidOCR(intra_op_num_threads=2, inter_op_num_threads=1)
    records = json.loads((folder / "frames" / "index.json").read_text(encoding="utf-8"))["frames"]
    target = folder / "ocr.json"
    previous = json.loads(target.read_text(encoding="utf-8")) if target.exists() else {}
    same_crop = previous.get("caption_crop_start") == crop_fraction
    done = {row["seconds"]: row for row in previous.get("frames", [])} if same_crop else {}
    for i, row in enumerate(records):
        second = row["seconds"]
        if second in done:
            continue
        path = folder / "frames" / row["file"]
        frame = cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_COLOR)
        frame = frame[int(frame.shape[0] * crop_fraction):]
        result, _ = engine(frame)
        lines = [{"text": r[1], "confidence": round(float(r[2]), 3)} for r in result or [] if r[2] >= .5]
        done[second] = {"seconds": second, "frame": row["file"], "lines": lines}
        if (i + 1) % 20 == 0:
            write_json(target, {"caption_crop_start": crop_fraction, "frames": sorted(done.values(), key=lambda r: r['seconds'])})
            print(f"{folder.name}: OCR {i+1}/{len(records)}", flush=True)
    output = sorted((done[r["seconds"]] for r in records), key=lambda r: r["seconds"])
    write_json(target, {"caption_crop_start": crop_fraction, "frames": output})
    text = [f"[{r['seconds']//60:02d}:{r['seconds']%60:02d}] " + " | ".join(x["text"] for x in r["lines"]) for r in output]
    (folder / "ocr.txt").write_text("\n".join(text) + "\n", encoding="utf-8")
    print(f"{folder.name}: OCR draft ready", flush=True)


def transcribe(folder, model_path, device):
    """Transcribe narration using an explicitly supplied existing local model."""
    from faster_whisper import WhisperModel

    model_path = model_path.resolve()
    if not (model_path / "model.bin").is_file():
        raise RuntimeError("ASR requires an existing local model; no automatic model download.")
    target = folder / "transcript.json"
    if target.exists():
        print(f"{folder.name}: existing ASR draft retained", flush=True)
        return
    model = WhisperModel(str(model_path), device=device,
                         compute_type="int8" if device == "cpu" else "float16",
                         cpu_threads=2, num_workers=1, local_files_only=True)
    segments, info = model.transcribe(str(folder / "media.mp4"), language="zh",
                                      beam_size=5, vad_filter=True,
                                      condition_on_previous_text=False)
    rows = []
    for segment in segments:
        rows.append({"start": round(segment.start, 2), "end": round(segment.end, 2),
                     "text": segment.text})
        if len(rows) % 40 == 0:
            write_json(folder / "transcript.partial.json", {
                "kind": "incomplete uncorrected ASR checkpoint, not full coverage",
                "model": str(model_path), "segments": rows})
            print(f"{folder.name}: ASR through {segment.end:.0f}s", flush=True)
    write_json(target, {"kind": "uncorrected ASR draft", "model": str(model_path),
                        "language": info.language, "segments": rows})
    lines = [f"[{int(r['start'])//60:02d}:{int(r['start'])%60:02d}–"
             f"{int(r['end'])//60:02d}:{int(r['end'])%60:02d}] {r['text']}" for r in rows]
    (folder / "transcript.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{folder.name}: ASR draft ready", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bvid")
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--page", type=int, help="Explicit 1-based part; required for multipart videos")
    parser.add_argument("--stage", choices=["fetch", "frames", "ocr", "transcribe", "all"], default="all")
    parser.add_argument("--asr-model", type=Path, help="Existing local faster-whisper model directory")
    parser.add_argument("--asr-device", choices=["cpu", "cuda"], default="cpu")
    parser.add_argument("--interval", type=int, default=8)
    parser.add_argument("--caption-crop-start", type=float, default=0)
    args = parser.parse_args()
    if not re.fullmatch(r"BV[0-9A-Za-z]{10}", args.bvid):
        parser.error("Expected one exact BVID")
    if args.interval < 1 or not 0 <= args.caption_crop_start < 1:
        parser.error("Invalid frame interval or crop")
    if args.page is not None and args.page < 1:
        parser.error("Page must be >= 1")
    if args.stage == "transcribe" and args.asr_model is None:
        parser.error("--stage transcribe requires --asr-model (existing local directory)")
    folder = args.output_root.resolve() / args.bvid
    if args.page is not None:
        folder = folder / f"P{args.page:02d}"
    folder.mkdir(parents=True, exist_ok=True)
    if args.stage in ("fetch", "all"):
        fetch(args.bvid, folder, args.page)
    if args.stage in ("frames", "all"):
        frames(folder, args.interval)
    if args.stage in ("ocr", "all"):
        ocr(folder, args.caption_crop_start)
    if args.stage == "transcribe":
        transcribe(folder, args.asr_model, args.asr_device)


if __name__ == "__main__":
    main()
