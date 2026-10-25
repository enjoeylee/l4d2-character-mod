# 求生之路 2 人物 MOD 制作 Skill

面向 Claude Code 与支持 `SKILL.md` 的代理工具，提供《Left 4 Dead 2》幸存者人物模型替换、表情、眼动、T-Pose、骨架权重、VRD、材质、第一人称手模、编译、打包与排错的制作知识。

本仓库包含 **11 个原始 Skill 文件，合计约 257 KiB**，另附本说明与忽略规则。发布包保留整理后的知识、来源账本和两个 Python 辅助脚本，不附带教程视频、抽帧、模型资产、软件安装包、运行环境或 Python 缓存。

## 内容入口

- [SKILL.md](SKILL.md)：任务路由、工程制作约定与交付要求。
- [人物制作流程](references/character-workflow.md)：导入、形态键、T-Pose、骨骼、权重和 VRD。
- [编译、材质与测试](references/compile-materials-testing.md)：GLB/QC、VMT/VTF、手模、图标、打包与验证。
- [表情与眼动诊断](references/face-eye-diagnostics.md)：表情、眼球、眼睑与材质问题。
- [已审核纠错](references/reviewed-corrections.md)：教程错误、条件分支与模板约束。
- [工具链记录](references/toolchain.md)：教程版本、原环境工具路径及待补齐组件。
- [视频学习流程](references/video-learning.md)与[来源账本](references/source-ledger.md)：学习范围、来源、时间戳和验证边界。

默认服务于幸存者人物替换。感染者、旧 Max、SMD/VTA 和其他路线按文档注明的条件单独判断；武器皮肤制作可参考另一个独立仓库 [l4d2-weapon-skin](https://github.com/enjoeylee/l4d2-weapon-skin)。

## 安装到 Claude Code

### Windows / PowerShell

```powershell
$claudeSkillsPath = Join-Path $env:USERPROFILE '.claude\skills'
New-Item -ItemType Directory -Path $claudeSkillsPath -Force | Out-Null
git clone https://github.com/enjoeylee/l4d2-character-mod.git (Join-Path $claudeSkillsPath 'l4d2-character-mod')
```

### Linux / macOS

```sh
mkdir -p ~/.claude/skills
git clone https://github.com/enjoeylee/l4d2-character-mod.git ~/.claude/skills/l4d2-character-mod
```

安装后在 Claude Code 中调用：

```text
/l4d2-character-mod 请检查我的幸存者人物工程，先核对目标角色、输入文件和实际可用工具。
```

仅供某个项目使用时，可以把整个仓库放到项目的 `.claude/skills/l4d2-character-mod/`。

更新已有副本：

```sh
git -C <安装目录>/l4d2-character-mod pull --ff-only
```

Claude Code 的安装路径与调用方式见 [官方 Skills 文档](https://code.claude.com/docs/en/skills)。使用其他代理工具时，按其 Skill 发现规则安装整个目录，并保留参考资料和脚本的相对位置。

## 工具与脚本依赖

知识文档可直接阅读。教程主线记录为 Blender 4.5、NekoMDL 2.3.0 与 GLB/glTF；这是教程路线的版本条件，目标环境是否已安装、插件是否兼容及实际工程是否通过测试，需要另行确认。

| 内容 | 依赖及能力范围 |
| --- | --- |
| 人物工程制作 | Blender、与所选路线匹配的插件、模板及编译工具；按实际工程选择 NekoMDL 或 Source 工具链 |
| [audit_character_scene.py](scripts/audit_character_scene.py) | 在 Blender 自带的 Python / `bpy` 环境运行，读取场景、权重、骨骼和形态键；报告不能替代编译或游戏测试 |
| [extract_video_evidence.py](scripts/extract_video_evidence.py) | Python、PATH 中的 ffmpeg/ffprobe；抽帧依赖 OpenCV/Pillow，OCR 依赖 NumPy/RapidOCR，转写依赖 faster-whisper 和明确指定的本地模型 |
| 自动操作 Blender | 根据目标代理实际配置的 MCP、后台脚本或其他可用入口执行；本仓库未附带 MCP 服务端或连接配置 |

不运行脚本也能使用已整理的知识。视频提取脚本会在执行对应阶段时访问 B 站并写入指定输出目录；它不是安装时自动执行的步骤。`--stage all` 执行 fetch/frames/ocr，转写应单独指定 `--stage transcribe` 与已有模型；不会自动下载语音模型。OCR/ASR 输出仍需要审核。

没有所需插件、模板或编译器时，应说明具体缺口并完成不依赖它的步骤。文件存在、插件注册、教程演示和当前工程通过编译/游戏验证是不同状态。

## 历史证据与路径

原 Skill 保留 `D:/11111/...`、`D:/tool/...` 等原环境路径，以及 `../../../../learning/...` 指向的审核笔记、采集脚本和证据记录。这些是历史来源引用，**对应原工程目录和证据文件没有随仓库发布**，在 GitHub 或其他机器上可能无法打开。

仓库内 `SKILL.md`、`references/`、`scripts/` 之间的链接用于当前知识导航；指向原工程的链接只用于追溯。来源 URL、平台 ID、分 P、时间戳、纠错结论、未完成项目与验证边界均保留。使用现有知识无需复制全部视频库；需要复核某条结论时，再按账本取得对应材料。

工具链中的路径、安装状态和测试结果属于注明日期的原环境记录，不能直接当成目标机器的当前状态。迁移时按实际工具路径配置；历史委托只描述当时任务，当前制作、安装或发布以使用者本次授权范围为准。

## 资源范围

本仓库不分发游戏文件、人物模型、商业插件、作者模板、视频/音频原件、抽帧/OCR/转写资料库、建模软件、编译器安装包或语音模型。外部教程、工具及资产的权利归各自权利人；保留来源信息不代表代为授予它们的再分发许可。
