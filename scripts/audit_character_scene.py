"""Read-only Blender preflight for a survivor body OR arms export collection.

Run: blender -b INPUT.blend --python audit_character_scene.py -- --output REPORT.json
Use --collection to exclude backups, references and non-export objects.
This reports compatibility concerns; it never deletes bones or fixes weights.
"""
import argparse
import json
import math
import sys
from pathlib import Path

import bpy


def audit(collection=None, bone_budget=128, influence_budget=3):
    objects = list(bpy.data.collections[collection].all_objects) if collection else list(bpy.context.scene.objects)
    findings, meshes, rigs = [], [], {}

    def add(code, object_name, detail, count=None, samples=None):
        row = {"code": code, "object": object_name, "detail": detail}
        if count is not None:
            row["count"] = count
        if samples:
            row["sample_vertex_indices"] = samples[:12]
        findings.append(row)

    for obj in objects:
        if obj.type != "MESH":
            continue
        rig = obj.find_armature()
        shape_keys = obj.data.shape_keys
        keys = list(shape_keys.key_blocks) if shape_keys else []
        row = {"name": obj.name, "vertices": len(obj.data.vertices), "polygons": len(obj.data.polygons),
               "armature": rig.name if rig else None, "scale": list(obj.scale),
               "shape_keys": [k.name for k in keys],
               "materials": [slot.material.name if slot.material else None for slot in obj.material_slots]}
        meshes.append(row)
        if any(abs(s - 1.0) > 1e-5 for s in obj.scale):
            add("non_unit_scale", obj.name, "Review mesh/rig transforms and rest pose together; do not apply blindly after rigging.")
        if len(keys) > 1 and any(abs(k.value) > 1e-5 for k in keys[1:]):
            add("active_shape_keys", obj.name, "Nonzero shape-key values: verify intended neutral/export state.")
        for key in keys:
            if len(key.data) != len(obj.data.vertices):
                add("shape_key_vertex_mismatch", obj.name, key.name)
        if not rig:
            add("no_armature", obj.name, "Check whether this is an intended rigid object or an unbound character mesh.")
            continue
        bones = {b.name for b in rig.data.bones}
        rigs[rig.name] = {"name": rig.name, "total_bones": len(bones),
                          "deform_flag_bones": sum(b.use_deform for b in rig.data.bones),
                          "scale": list(rig.scale)}
        valid_groups = {g.index: g.name for g in obj.vertex_groups if g.name in bones}
        orphan_groups = {g.index: g.name for g in obj.vertex_groups if g.name not in bones}
        unweighted, over_limit, non_normalized, invalid_weights = [], [], [], []
        used_orphans = set()
        for vertex in obj.data.vertices:
            weights = []
            for group in vertex.groups:
                if group.weight <= 1e-6:
                    continue
                if group.group in valid_groups:
                    weights.append(group.weight)
                elif group.group in orphan_groups:
                    used_orphans.add(orphan_groups[group.group])
            if not all(math.isfinite(w) for w in weights):
                invalid_weights.append(vertex.index)
            if not weights:
                unweighted.append(vertex.index)
            elif abs(sum(weights) - 1.0) > 1e-3:
                non_normalized.append(vertex.index)
            if len(weights) > influence_budget:
                over_limit.append(vertex.index)
        for code, indices, detail in (
            ("unweighted_vertices", unweighted, "No positive matching bone-group weight."),
            ("influence_budget", over_limit, f"More than {influence_budget} positive bone influences; L4D2 compatibility baseline."),
            ("non_normalized_weights", non_normalized, "Matching bone weights do not sum to one."),
            ("non_finite_weights", invalid_weights, "Non-finite weight values."),
        ):
            if indices:
                add(code, obj.name, detail, len(indices), indices)
        if used_orphans:
            add("non_bone_groups", obj.name, "May be masks, NOT automatic deletion candidates: " + ", ".join(sorted(used_orphans)))
    for rig in rigs.values():
        if rig["total_bones"] > bone_budget:
            add("bone_budget", rig["name"], f"Scene rig has {rig['total_bones']} bones; baseline is {bone_budget}. Final QC/include/helper bone table must be checked separately.")
        if any(abs(s - 1.0) > 1e-5 for s in rig["scale"]):
            add("rig_non_unit_scale", rig["name"], "Review rig transforms together with bound meshes and exported rest pose.")
    used_materials = {slot.material for obj in objects if obj.type == "MESH" for slot in obj.material_slots if slot.material}
    images = set()
    for material in used_materials:
        if material.use_nodes:
            images.update(node.image for node in material.node_tree.nodes if node.type == "TEX_IMAGE" and node.image)
    for image in images:
        if image.source == "FILE" and not image.packed_file:
            resolved = bpy.path.abspath(image.filepath, library=image.library)
            if not resolved or not Path(resolved).is_file():
                add("missing_texture", image.name, resolved or "Empty image filepath")
    return {"blender_version": bpy.app.version_string, "source": bpy.data.filepath or "<unsaved>",
            "collection": collection, "bone_budget_baseline": bone_budget, "influence_budget_baseline": influence_budget,
            "meshes": meshes, "armatures": list(rigs.values()), "findings": findings,
            "limits": "Scene data only: does not validate compiled bone table, flex controllers, VMT/VTF, VRD motion, game visuals, or nested node-group textures."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--collection")
    args = parser.parse_args(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else [])
    if args.collection and args.collection not in bpy.data.collections:
        parser.error("Named collection does not exist")
    if args.output.exists():
        parser.error("Report already exists; choose a new output path")
    result = audit(args.collection)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"output": str(args.output), "meshes": len(result["meshes"]), "findings": len(result["findings"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()
