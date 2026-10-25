# 本机工具链与教程版本

核查日期：2026-09-08。路径存在、程序可启动、插件装载、完整实模编译是不同状态。不要把本表的“已有文件”读成全套教程已经配置完成。

**用户当前安排：下载不顺的工具/软件只记录，后续由用户处理。** 本轮已停止获取缺失包；不用这些待办拖延知识学习，也不继续安装客户端、重试下载或自动追踪下载进度。后续收到明确继续指令或文件后再核验。

## 已确认可用/存在的工具

| 组件 | 位置 | 状态与决策 |
|---|---|---|
| Blender 4.5.13 LTS | `D:\11111\求生之路2人物mod制作\software\blender-4.5.13-windows-x64\blender.exe` | 本轮从官方镜像取得，官方 SHA-256 匹配；`--version` 与后台 Python 小样运行通过。教程原版4.5.3，同4.5 LTS系列；尚未装齐教程插件 |
| 原 Blender 4.2.23 LTS | `D:\Steam\steamapps\common\Blender\blender.exe` | 实际运行 `--version` 确认；保留未覆盖，不默认拿4.2配置替代4.5 |
| 旧 NekoMDL 1.3.2 | `D:\11111\求生之类2贴皮大陈子整理\猫猫编译\nekomdl.exe` | FileVersion/ProductVersion为1.3.2；**不是教程2.3.0，不认为满足主线编译条件** |
| 旧 Crowbar 0.68 | `D:\11111\求生之类2贴皮大陈子整理\Crowbar.exe` | PE版本0.68.0.0；视频用0.74。可按实际功能检查复用，不能写成已安装0.74 |
| Blender Source Tools 3.4.3 | `%APPDATA%\Blender Foundation\Blender\4.2\scripts\addons\io_scene_valvesource` | 原4.2安装下已有文件；没有自动安装到新4.5 |
| BoneAnimCopy | `D:\tool\l4d2-weapon-lab\bin\blender_BoneAnimCopy` | 作者源码已在本机；是否在目标Blender启用需另查 |
| VTFEdit | `D:\11111\求生之类2贴皮大陈子整理\vtfedit\VTFEdit.exe` | 文件已存在，按需复用 |
| 官方 studiomdl / vpk / hlmv | `D:\Steam\steamapps\common\Left 4 Dead 2\bin\` | 文件已存在；默认Source路线工具，不支持凭空混入Neko专用命令 |
| 视频提取 Python | `D:\tool\l4d2-weapon-lab\.venv\Scripts\python.exe` | Python3.11.15；Pillow/OpenCV/RapidOCR/faster-whisper等依赖实际可导入 |
| yt-dlp | `D:\tool\l4d2-weapon-lab\.venv\Scripts\yt-dlp.exe` | 已有，无需重复下载；本轮直接用公开播放接口 |
| ffmpeg / ffprobe | `C:\Users\Administrator\AppData\Local\Microsoft\WinGet\Links\` | 实际提帧和媒体探测已使用 |

当前会话没有可调用的 Blender / l4d2_weapon MCP。未来先查实际工具列表和连接状态；优先使用可用的具体工具或 Blender 后台脚本，不能把隔壁 skill 中的 MCP 名字当成已连接服务。

## 教程专用组件：版本记录不等于已安装

| 教程组件 | 视频版本/用途 | 获取与替代条件 |
|---|---|---|
| NekoMDL | 2.3.0；GLB、Flex、程序骨与USQC | [作者发布页](https://steamcommunity.com/sharedfiles/filedetails/?id=3142607978)；版本专属2.3.0直链未核实，需检查包内版本与NewCommands.qci |
| L4D2_Character_Tools | 1.1.0；骨名映射、对骨、VRD导出 | 视频第1集配套资源入口。未拿到本体及模板，不伪造插件API |
| CATS（Neoneko分支） | 4.5.3.2；合骨、权重合并、保持网格的Rest Pose操作 | [作者发布记录](https://github.com/teamneoneko/Cats-Blender-Plugin-Unofficial-/releases)明确4.5专用；5.x另有分支；不装错主版本 |
| Shape Key Utilities Enhanced | 1.0；形态键辅助 | 基础置值、命名可用Blender原生；不为简单按钮强制装插件 |
| Simple Renaming Panel / Bone Manager | 2.1.4 / 4.4.3；重命名、分组 | 可用原生操作完成基本任务，保留映射检查 |
| BoneAnimCopy / SourceIO | 1.0 / 5.5.2；T-Pose迁移、MDL导入 | [BoneAnimCopy作者](https://github.com/kumopult/blender_BoneAnimCopy)；SourceIO需对应作者版本核查。不可假设预设也随插件存在 |
| Better FBX Importer & Exporter | 6.3.0；示例FBX导入 | 商业插件非通用必需；内置导入正确时直接使用，不购买/安装非授权副本 |
| NekoShaders / Left4Neko | 视频第5集演示2.6.6并提2.7.3修复；第2集形态键眼动依赖Left4Neko | 运行依赖要按作品要求单独确定，不能默认替所有用户安装或升级 |

## 作者配套资源

[第1集资源分享](https://pan.baidu.com/s/1FvuXmqEtKFMzzhuvD1lUKw?pwd=2026)，提取码 `2026`。本轮通过正常网页确认可见目录 `ModGuide2026`，包含：

- `MOD工程文件.7z.bytes`，网页显示85.6M、修改日期2026-05-01。
- `图标制作资源.7z.bytes`，网页显示84M、修改日期2026-02-20。

网页能列文件，但下载操作实际触发百度网盘客户端安装包，而非目标压缩包。安装包已移至 `D:\tool\downloads\BaiduNetdisk_8.7.9.102.exe`，未运行；本次产生的重复安装包已删除。**工程/图标压缩包未取得，模板、BAT源码及其附带软件链接尚未审核。** 后续取得后，先静态检查实际类型与内容，再在副本去掉`.bytes`伪后缀；不要自动运行其中脚本或安装包。只加载模型数据时关闭不需要的自动执行脚本。

不得将这个缺口隐去：当前可进行输入整理和能力学习；精确复现本教程的USQC/角色工具编译前，需要匹配的模板、插件、NekoMDL及其说明。

## Blender下载记录

- [Blender 4.5 LTS 官方发布页](https://www.blender.org/releases/4-5/)：本轮选择4.5.13 LTS，同4.5系列补丁版，不追随5.x大版本。
- [官方便携包](https://mirror.blender.org/release/Blender4.5/blender-4.5.13-windows-x64.zip)，398,648,740字节。
- [官方校验文件](https://mirror.blender.org/release/Blender4.5/blender-4.5.13.sha256)；已匹配 `b5fdf800ce65fa2f209e8f68d02667e4d720fa1c42f247c72d1882ab04decba6`。
- ZIP及校验文件保留在项目 `software/downloads`。不改系统PATH、不注册文件关联、不替换Steam版。

## 只读场景预检

适用于准备导出的身体或手模工程，最好用独立导出合集过滤参考物和备份：

```powershell
& 'D:\11111\求生之路2人物mod制作\software\blender-4.5.13-windows-x64\blender.exe' `
  -b 'D:\path\to\character.blend' `
  --python 'D:\11111\求生之路2人物mod制作\.agents\skills\l4d2-character-mod\scripts\audit_character_scene.py' `
  -- --collection 'EXPORT_BODY' --output 'D:\path\to\build\scene-audit.json'
```

替换示例输入/合集/输出路径，输出必须是新文件。脚本不保存`.blend`、不改权重或骨架。本轮在4.5.13的内存合成网格上验证了：四骨影响顶点、无权重顶点能被定位，修正后的合规网格无误报。它只做场景级预检；最终QC/包含模型合成骨表、形态键游戏控制、VRD、VMT/VTF、真实关节表现仍需分别检查。

## 第二批序号7–12：2024环境与复用工具（2026-09-08）

| 项目 | 实际确认 / 状态 |
|---|---|
| 教学环境 | BV1Y61RYPERF画面为Blender4.2.2 LTS；P4 02:40/02:56为CATS4.2.1.3，P15为Crowbar0.74。与主线4.5/2.3.0分开，不为看旧课降级或重装本机Blender |
| 旧MOD工具、重命名/约束预设 | P4使用MMD名称预设及批量位置/旋转面板；P12输出传统survivor.vrd，P13输出$jigglebone QCI。精确插件/预设版本及源码未取得，仍待包内审核；不假报与2026 L4D2_Character_Tools1.1.0是同一套API |
| VTFEdit Reloaded、VMT模板 | P10窗口可见Reloaded但未清楚给版本；已有普通VTFEdit不据此改记成Reloaded。先按实际功能复用；lightwarp、假眼追QC、原版arms参考及作者预设按工程需要待补 |
| 既有large-v3模型 | `D:\tool\l4d2-weapon-lab\models\models--Systran--faster-whisper-large-v3\snapshots\edaa852ec7e145841d8ffdb056a99866b5f0a478`；符号链接指向既有完整blobs，实际完成13P音轨转写，无新模型下载 |
| 既有CUDA DLL | `D:\tool\l4d2-weapon-lab\cuda12`；首次GPU调用缺搜索路径，使用该已有目录的进程级PATH后成功。未装CUDA、未改系统PATH；P4使用CPU，其余P使用GPU |
| 摄取脚本 | 原脚本原地新增`--page`分P隔离与显式本地ASR阶段；13P各自media/probe/frames/OCR/ASR齐备。不是新下载器或第二份skill |

[2024合集简介配套工具包](https://pan.baidu.com/s/1JlhmlX4_CGuQ-VRl8JxTuw?pwd=4xgx)，提取码`4xgx`。仅登记来源，未尝试下载/安装；既有2026包的缺口也原样保留。不为旧教程再尝试网盘客户端，不把可见软件按钮当本机已启用的功能。

新增本机验证仅为4.5.13内存合成网格上的Data Transfer法线应用：保留两个形态键、顶点数不变、自定义法线存在。没有运行作者角色工程、模板BAT或游戏部署。

## 第三批序号13–21：工具身份、过时版本与待办（2026-09-08）

本批复用既有媒体/ASR工具，**没有新下载或安装建模软件、插件、ASR模型或运行扩展**。下表“官方页面核查”不等于“本机已装”；历史视频版本与现行文档明确分开。

| 组件/来源 | 本次核实与使用条件 | 待办/状态 |
|---|---|---|
| 织梦者人物MOD工具 | BV1ms421g7yz画面3.6.2；[作者仓库](https://github.com/Saberafter/Blender_L4D2_Character_Tools)说明骨名映射、VRD/jiggle/Flex功能及选择/导出差异 | 未取得并验证该版插件与预设。与2026课名近似的L4D2_Character_Tools1.1.0不因名称近似视为同作者/同API |
| BoneAnimCopy | 2023 BV17X4y1v73d的T-Pose/位置约束；[作者仓库](https://github.com/kumopult/blender_BoneAnimCopy)与本机已有路径可作入口 | 已有文件但本批未启用/改装；模板与目标Blender兼容需按实际任务核验 |
| Crowbar | 2020上传课、2021感染者课的UI不同；感染者可见0.42，轻语2024用0.74；[官方releases](https://github.com/ZeqMacaw/Crowbar/releases)当前页列0.74 | 本机仍记录实查的0.68，不谎称已升级。旧上传失败法不作为清空用户云数据依据 |
| McQueen / MQTools | BV1MyXXYuEmy 01:09起给[MQTool/L4D2-MOD-Tools](https://github.com/MQTool/L4D2-MOD-Tools)。同日仓库README列MQToolsBlender1.6.1、Max5.7，推荐Blender4.5与Max2019+；2025录像4.3/4.5不是最新版本 | 未下载/安装/运行。仓库明示没有开源许可证、再发布须联系作者；公开可见不等于任意再分发。新版功能/脚本仍待实际源码和模板审核，不能凭README保证全兼容 |
| Max中转与导出组件 | 2024/2025课为Blender→FBX→Max→SMD/VTA；感染者课有Max2014和Blender2.79/2.8。Skin Wrap原理核[Autodesk官方说明](https://help.autodesk.com/cloudhelp/2026/ENU/3DSMax-Modifiers/files/GUID-1B3C4662-8C42-4F02-BD1B-204CD491166B.htm) | 不为学习安装/降级Max、Unity或商业Better FBX。实际项目选此路时核合法授权、导出插件、Morpher及模板 |
| NekoVTF、Patch基材质、Max辅助BAT/INI | 视频有NekoVTF、共享VMT、RenamePresets.ini/TPosePresets.ini及release脚本；图片可见选项不等于获得文件 | 准确版本、完整SMD/VTA/QCI/VRD及资源包待用户提供/后续明确获取；先静态审阅删除/覆盖/部署命令 |
| L4N2.34配套转换器 | BV1ymT16pEPL展示l4n_magic_converter.exe及参考组、身体/FPS转换入口 | 本体与参考/批处理未取得。本片不证明最终包无L4N依赖，也不因工具随包附带就自动给用户安装L4N |
| 2021感染者模板 | BV15y4y1b7z2四P的专用QC、参考、变体与舌头/尸块等 | 360p不可完整辨读长代码；等待真实包和目标资产清单，不另追其引用教程。FPS完整制作不在四P覆盖内 |
| 材质专题辅助工具 | 多帧导图/VTF、夜光蒙版、渐变/描边可用已有合法工具；PNG支持RGBA已核[W3C规范](https://www.w3.org/TR/png-3/) | 不为教材按钮强装商业编辑器；原素材、Alpha、实际编码、mips与目标shader另核 |

仅为本次32条来源添加[批次调度脚本](../../../../learning/collect_13_21.py)，调用原摄取脚本并按显式清单读取缓存元数据；不是另一份skill/通用工具安装。原摄取脚本只增加关闭前文条件化与ASR中间检查点，检查点明确为未完成底稿。避免同时装载多个large-v3 GPU进程争用显存；已有输出可按阶段继续，空转写/幻听不靠重复安装模型解决。

前两批未取得的NekoMDL2.3.0、2026工程/图标包及2024工具包等记录全部保留。将来只有实际制作需要、用户给文件或明确允许继续获取时再处理；不反复尝试网盘客户端，不将待办写成已安装。

## McQueen2023十P：历史工具与高清补证（2026-09-08）

本批没有安装/升级建模软件、插件或转写依赖。下列记录是视频身份与后续复现待办，不覆盖本机上表。

| 项目 | 已核事实与适用条件 | 当前状态 |
|---|---|---|
| Blender / Max | 高清P1 03:04与P10 02:24底栏为Blender2.93.17；Max标题为2020。桌面另有3.3.6快捷方式不代表该画面在用3.3.6 | 不为旧课降级；现有4.5主线保留 |
| CATS / MMD Tools | P1 Fix Model和P10 PMX内部字典；P10设置页可见Install version0.19.0选择项，不据此认定实际已安装插件版本 | 录像精确包/源码未取得；按当前Blender匹配版本再核 |
| SourceOps | P5复制父空间位置/旋转的实际工具；[作者仓库](https://github.com/bonjorno7/SourceOps)、[相应操作源码](https://raw.githubusercontent.com/bonjorno7/SourceOps/main/addon/ops/pose_bone_transforms.py)已读 | 与SourceIO、Source Tools是不同工具，未安装本课版 |
| SourceIO | [作者仓库](https://github.com/REDxEYE/SourceIO)当前说明4.0+导入Source模型/材质；本课口误不改变其身份 | 不把导入能力记为MDL/VMT导出；未为此更新 |
| Max SMD / VTA导出 | 高清P4 19:12明确Neil Jedrzejewski的Valve SMD File Exporter v1.7，显示非商业使用条件；P7导Source Vertex Animation | [简介所列Wunderboy作者页](https://www.wunderboy.org/3d-modelling-tools-plug-ins/)访问失败，停止重试；准确二进制、Max版本匹配及许可待取得 |
| ui人物模板2022稳定版 | 视频实际文件夹名如此；P4称不能提供，P10 00:42–00:51说已获ui同意分享，简介给奶牛快传口令b0r94j | 未试旧口令下载；完整QC/QCI、手模模板、ref脚本及授权范围待实际包，不能把其他MOD反编译结果当该完整包 |
| Perl / tz→ref脚本 | P4高清25:36要求对齐后官方骨架tz.smd、选动画来源人物BAT生成ref，PL依赖Perl路径；P5开头接续该结果 | 未取得/运行BAT和PL、未下载Perl；只在选此旧模板复现时才是依赖，不成为GLB主线必装项 |
| 既有faster-whisper | 全10P本地large-v3；P1/P3沿用原入口，其余用已安装BatchedInferencePipeline，batch4/int8_float16，单GPU进程 | 无新模型/依赖；仅本批调度文件新增批处理分支，原通用提取脚本不改 |
| 用户授权的Chrome高清播放 | 原公开接口只给360p；用户明确许可后，Chrome已登录且各P显示1080P60。取得当前已加载媒体资源的完整video-only流，逐P实测1080p60/时长 | 原360p音画及ASR保留，HD单独保存。未读取浏览器Cookie/凭证库；出处不保存签名查询串。没有把视频下载当建模环境已就绪 |

本批[固定十P采集脚本](../../../../learning/collect_bv1ug4y1j7lj.py)调用原提取器；[高清关键证据脚本](../../../../learning/capture_course_hd.py)只接受与指定分P CID相符、在授权Chrome页面实际观察到的媒体地址，保存高清画面/探测与选定时间戳。不会自动获取登录信息、发现新教程或安装工具。浏览器的媒体打包接口不支持本次M4S，原生保存也未产生成品；随后只下载实际已加载的资源流，未绕过登录/付费限制。

## 2026-09-09六条：面部/预览/资源迭代

本批只复用已安装的Python、ffmpeg/OCR/large-v3/CUDA及Blender4.5.13，**没有安装或升级软件、插件、运行扩展**。六条媒体全取得；以下待办指复现实作资源，不是视频缺失。原2026包、NekoMDL2.3.0等缺口保留。

| 项目 | 本批核实 | 可用状态/条件 |
|---|---|---|
| TC5B5 P11 | Blender3.6.7、已有面部rig、复制Armature再Apply as Shape Key；2024合集 | 没有为旧课降级；4.5.13内存小样验证Save与复制后Apply两法，报告在本批catalog。未取得作者脸部工程/表情方案txt本体 |
| MLUIdgb补档 | Max2019、XPS脸骨→VTA、QC Eyes，当前补档UP账号已注销，非原作者新版本 | 完整XPS模板/QCI/VMT和ambient.vtf未取得；Max/Perl不成为主线必装。简介旧链接仅保留元数据 |
| Kokkorylien眼材质包 | [作者简介](https://www.bilibili.com/video/BV1SY4y1L7Uo/)提供`https://wwp.lanzouw.com/b03j50yah`，密码ko；包含眼图/眼VMT模板的声明 | 未下载包，低清长QC待实际文件/高清；无反复换下载器。ambient等依赖不能靠同名假文件顶替 |
| 鱼不吃茄子工程 | Blender4.1、SMD/VTA、Crowbar0.74；[简介工程](https://pan.baidu.com/s/1bir_TDjet8z7lwtS2GyqUQ?pwd=xvme) | 仅登记，未再次尝试网盘客户端；片内未讲全VMT，准确shader/辅助图待包 |
| HLMV++ | BV1am421H7Dw可见Submodels/Add (Steam)、Sequence层、FOV和手模重编观察 | 未安装/启动本课查看器；本机原版hlmv文件不等于HLMV++已就绪。此课的组合预览流程可学习，版本兼容仍待实际工具 |
| MareTF | [作者仓库](https://github.com/craftablescience/MareTF)核create/edit/info/watch及格式版本限制 | 未安装/运行；先按已有转换器实际能力复用。作者工具支持多引擎，不能把最新VTF格式默认给L4D2 |
| Nekook | [作者页](https://steamcommunity.com/sharedfiles/filedetails/?id=3262974277)说明挂载目录高于VPK优先级、配置启动游戏/hlmv；页面历史1.5含松散VTF修复 | 未安装/配置。开发挂载不自动作为最终玩家依赖；不改系统PATH、autoexec或游戏文件系统 |
| VSCode三插件 | Source Engine Support、VSCode VDF、Batch Runner由PBR片简介及UI确认，F5为作者绑定 | 未安装/修改编辑器配置，均为开发便利，不是最终VPK依赖 |
| PBR shader与打包脚本 | PBR片05:44明确PBR及MRAO/发光图；06:56后l4d2vpk_configs.py白名单/分支 | 精确NekoShaders版本、完整BAT/Python与传递依赖未取得；不直接执行片段，不据包输出证明无依赖 |
| NekoMDL/USQC作者直接说明 | [Neko发布记录](https://steamcommunity.com/sharedfiles/filedetails/?id=3142607978)列eyeball/eyelid；[USQC flexrules源码](https://raw.githubusercontent.com/Starfelll/L4D2_Utils/master/ultimate_survivor_qc/Compiling%20Files/QCIs/survivors_flexrules.qci)存在直接blink分支 | 只核语义，不下载替换现用模板。该远端文件不当成本项目2026改编USQC v3.8或NekoMDL2.3.0包本体 |

[本批采集脚本](../../../../learning/collect_face_batch_20260909.py)固定六条，分阶段fetch/ocr/probe-audio/asr，ASR单GPU进程；不添加通用工具副本。取证、合成小样、源声明与本机安装状态在[笔记](../../../../learning/notes/2026-09-09-face-review.md)分别记录。

## 路线图A/B/C：版本与适用条件（2026-09-09）

本批复用既有Python/ffmpeg/OCR/large-v3/CUDA与Blender4.5.13，无新软件、插件或运行扩展安装。用户许可Chrome后仅取实际已加载的指定课高清流；不读凭证库。第5条当前登录页仍要求作者充电档，未支付；这是视频访问缺口，不是建模软件安装缺口。

| 项目 | 视频/外部已核身份 | 本机状态与适用条件 |
|---|---|---|
| A组Blender | 3号原帧4.1.0；4号4.5.11 LTS；2号未辨具体补丁 | 保留本机4.5.13主线；静态舰船减面不直接作为Flex角色方案 |
| Quad Remesher | 4号00:24可见1.23，2号亦为可选四边化 | 未安装/购买；重拓扑网格来自其他合法方法亦可学习后续烘焙，不引入AI建模依赖 |
| VTFEdit | 6号P4口述1.3.3，2017课；高清13:20可见导入/格式/mips面板 | 已有普通VTFEdit路径保留，不因录像更改已装版本；Normal Format不是法线专用选项 |
| SP2VTF | 作者“一个橘色的橙子”，推荐者小小少女不饮酒；录像v1.0.7下载页、1.0.8 README与旧三路径UI并存 | 未下载/执行。只读[作者main](https://github.com/ora233-fantaea/SP2VTF)及固定提交281a5eb的scan/convert；新旧架构、真实编码槽、模糊匹配和输出覆盖须按实际包检查 |
| VTFCmd与DLL | SP2VTF底层转换依赖；录像路径来自VTFCmd_BatchScript-Generator_v2.1目录 | 目录名不等于VTFCmd二进制版；已有VTFEdit不证明所需exe/DLL齐备。本批只登记，不安装Steam++或其他网络工具 |
| ATI2N/DXT5nm | 8号L4N1.6.5/PBR演示，MareTF写7.4/ATI2N，DXT5nm需专用通道及解码 | 未安装L4N/MareTF，未原版实测；扩展编码与匹配shader分别查版本，不能凭可写格式证明可运行 |
| C组原生绑骨 | 9/10原帧Blender5.0.1；11原帧5.0.0 | 只迁可核对的原生语义，影片MMD卡顿不作为所有5.x禁用结论；本机4.5.13内存小样仅测明确争议 |
| 手模实录 | 12号Blender4.5.11、CATS4.5.3.2、官模v_arms_mechanic_new；后段Source Tools/SMD输出，Nekook v1.6开发挂载 | 未取得完整作者工程/QC与精确导出插件包；主线GLB不改。表面转权、合骨、局部修权分别执行验证，短游戏观察非全武器验收 |

[本批固定采集](../../../../learning/collect_abc_20260909.py)复用原摄取器和前批fetch函数，明确12项、访问待补跳过及单GPU转写；[高清补证](../../../../learning/capture_abc_hd.py)只接受Chrome实际观察到的指定CID资源，并与原媒体隔离；[语义小样](../../../../learning/test_abc_blender_semantics.py)不保存blend。前批NekoMDL2.3.0/2026模板等缺失项原样保留。

## 路线图D/E/F：物理与修复工具的版本边界（2026-09-09）

只审核13—21的11个实际P；没有安装/升级建模软件、插件、扩展或运行作者exe。原本机环境和前批资源缺口不变，工具存在/视频下载完成不是本机兼容验收。

| 项目 | 本批实际身份 | 状态/条件 |
|---|---|---|
| 碰撞体课 | 13号Blender3.4.1、Hammer/Propper、Source Tools下载页3.2.5、Crowbar日志0.74 | Source Tools网页版本不证明运行插件同版；未安装Propper，不将staticprop汽车配置迁入人物 |
| 自定义ragdoll | 14号Max2019传统SMD，Gmod主演示；15号实际P11 Blender4.1.1/CATS、预先绑定的PHY集合 | 不降级主线；已有Max或CATS文件不证明作者模板齐备。15号完整ragdoll.blend/QCI未取得，教学包只在metadata登记 |
| Crowbar | 16号00:16下载链接0.72，当前[作者releases](https://github.com/ZeqMacaw/Crowbar/releases)列0.74；后者含PHY animatedfriction反编译修复 | 本机仍0.68；学习没有升级。先按输入错误和真实版本评估，不将前端当成各游戏编译器全集 |
| 参考/QC手修 | 17/18号Blender3.6.7、武器reference/idle/layer等传统SMD | 18号简介给QC模板链接，未下载；动画完整性前提保留，不能移植枪手IK到角色 |
| DeltaRepair | 19P1原帧1.3.3，P2原帧1.4.1，界面署名shu、codex；UP不会贴皮の久辞自称代发，简介说AI协作 | 第三方候选，不是本任务/官方软件。`DeltaRepair_v1.4.1.exe`[简介网盘](https://pan.baidu.com/s/1Qm_rd--mvEogKjvLjlPr1g?pwd=cnut)仅登记，未下载、运行或审源码；完整格式/算法与输出覆盖行为未核 |
| RNG传统分支 | 20号2022年VTFEdit/VertexLitGeneric、EntityRandom三帧例；VTFEdit具体补丁未辨读 | 不用另一个2017视频版本补此空缺；旧指南已Obsolete，替代SYS正文受限未审，未安装新材质扩展 |
| 组件控制 | 21号2025-02-09短片，当前简介空，仅游戏菜单与显隐 | 未展示准确控制器/运行版本，不能从作者推断某版L4N；待实际QC/代码/说明，不算完整换装依赖就绪 |

[固定清单脚本](../../../../learning/collect_def_20260909.py)复用既有下载/帧/OCR/单GPU转写管线；[短时补帧/音轨样本](../../../../learning/supplement_def_evidence.py)只处理已存媒体；[高清包装器](../../../../learning/capture_def_hd.py)沿用Chrome实际CID资源检查。13/20两份HD分别1912×1024约23.976fps、1920×1080/60，video-only不替代原音轨；不读取浏览器凭证或保存签名查询串。不是另装通用工具，也没有修改隔壁枪皮项目。
