# 来源账本：原1–21、McQueen2023、六条补课与补充路线图

截至2026-09-08，已按用户会话“汇总求生之路2人物Mod教程”（`01a07e44-93d1-75c0-bf52-8f0c938810c0`）的学习顺序处理1–21。三批来源、证据质量和编译路线独立保留。第二批序号7–12不等于合集第7–12P；轻语2024合集两批合计19个指定P，不是23P全学完。去重按BVID+分P+CID，不因标题相同覆盖旧证据。各批的“本轮”指该批历史执行，不表示第三批重新下载软件或重复实模验证。

其后指定McQueen2023 `BV1ug4y1j7Lj`完整10P，见第四批；不是给旧序号重新编号，也不是重复学习序号20的2024/2025九片。前四批61条、62069秒记录保留。2026-09-09新增六条表情/眼动/调试补课见第五批，累计67条不同视频/分P、69397秒（19小时16分37秒），不等同于实际连续观看时长。

同日后续路线图A/B/C新增11条完成音画证据审核，另1条待完整媒体，见第六批；该批结束为78条、76973秒。随后按用户新指定范围审核D/E/F的13—21，共11个实际P、7086秒，见第七批。**当前累计89条已审视频/分P、84059秒（23小时20分59秒）**；其中路线图21只完成效果审核，制作步骤/准确运行依赖未覆盖。第六批5号的504秒仍未计入，可选22也未计入。这里的完成是所列取证方法下的证据/知识审核，不是所有制作能力/真实游戏验证均已完成。

## 第一批：序号1–6（保留原记录）

2026-09-08按用户指定会话“汇总求生之路2人物Mod教程”的序号1–6处理。没有扩展序号7及以后；视频引用的其他教程仅登记为线索，不算已学内容。

六集作者均为TC5B5，元数据总时长 **4387秒（73分07秒）**。取得公开720p完整媒体，逐集校验时长，生成 **550张8秒常规采样帧、48张联系表**，以及关键处额外补帧。已按时间线查看全部联系表，讲解页、参数及冲突处打开原帧复核。不是逐帧连续播放；OCR也不是人工校订字幕。第1集00:16明确无配音，各集未取得可用字幕轨，因此没有把背景音乐转写成教程文字。

| 序号 | 原视频与时长 | 当前CID | 常规帧/联系表 | 本轮知识提取与审核 |
|---|---|---:|---:|---|
| 1 | [教程简介及模型导入 / BV1u2fVBvEEQ](https://www.bilibili.com/video/BV1u2fVBvEEQ/) · 04:02 | 36183017172 | 30 / 3 | 00:16–00:56主路线与版本；01:20–02:08不同输入/工具；02:16–03:52导入、比例、贴图。重点纠偏盲删骨、强制商业FBX、混用SMD |
| 2 | [面部表情和骨架骨骼 / BV1u1fVBKEfM](https://www.bilibili.com/video/BV1u1fVBKEfM/) · 08:13 | 36183084968 | 62 / 6 | 00:16–04:16表情、眼动及Left4Neko；04:32–08:08分类和轴向。重点纠偏Save/Apply Shape Key、AU近似映射、固定旋转和64+64模板预算 |
| 3 | [网格分离和T-Pose / BV1g1fVBKEqz](https://www.bilibili.com/video/BV1g1fVBKEqz/) · 09:14 | 36183149133 | 70 / 6 | 00:16–02:56分离和材质；03:04–09:12映射、官模/手模参考与Rest Pose。重点纠偏经验顶点数、预设盲套、向游戏目录解包 |
| 4 | [权重转移和VRD / BV1wwf5BsEkk](https://www.bilibili.com/video/BV1wwf5BsEkk/) · 17:01 | 36541759511 | 128 / 11 | 00:16–04:24合骨嫁接；04:40–10:32GLB动作与NekoDriverBone；10:40–16:59清理、导出、Bill尸体。重点纠偏VRD路径/Action/帧、Selected Objects、骨表与权重分开查 |
| 5 | [模型编译和贴图处理 / BV1AFf5BdEsq](https://www.bilibili.com/video/BV1AFf5BdEsq/) · 16:00 | 38014486727 | 120 / 10 | 编译模板、贴图通道、材质与预览；重点复核07:20 nocull开关反说、09:44–09:52金属度通道自更正、NekoShaders版本差异 |
| 6 | [图标、手模、测试 / BV1pFf5BdEDc](https://www.bilibili.com/video/BV1pFf5BdEDc/) · 18:37 | 36183279780 | 140 / 12 | 图标素材、独立FPS手模、打包与游戏观察；重点纠偏硬编码骨名/旧Python选择API、未讲明的打包清理脚本、测试覆盖不足 |

## 可回溯的原始资料与笔记

每个BVID对应本项目`learning/<BVID>/`中的metadata、完整媒体、media_probe、frames、sheets、全画面OCR。第4、5集CID与早期合集可能不同，复学时以实际媒体CID比对，不能仅凭BVID就假设旧资料相同。

- [第1集提取/审核](../../../../learning/notes/01-review.md)
- [第2–3集提取/审核](../../../../learning/notes/02-03-review.md)
- [第4集提取/审核](../../../../learning/notes/04-review.md)
- [第5–6集提取/审核](../../../../learning/notes/05-06-review.md)

补充读取了第5集当前技术评论及作者回复：作者明确其贴图脚本主要针对绝区零或VRC，并未写MMD通用脚本；Toe骨无权重也可能影响IK。该补充只用于收窄适用范围，不从不完整评论还原缺失故障案例。

## 外部一手核查入口

- Blender：4.5形态键、修改器、Rest Pose、glTF导出和对象选择API，用于复核真实操作语义。
- Valve Source SDK 2013：骨骼/权重数据结构、程序骨类别、材质标志。只能证明其代码分支，L4D2实际结果还需对应编译器与游戏确认。
- NekoMDL作者发布说明：GLB morph、DMX版本、额外QC、分支差异；不把编译器扩展等同于游戏引擎能力扩展。
- 具体直接链接与采纳结论见 [reviewed-corrections.md](reviewed-corrections.md)；工具来源与实际安装状态见 [toolchain.md](toolchain.md)。

## 第一批实际验证与后续实模边界

视频媒体提取、时长检查、抽帧、OCR和skill结构验证属于本轮实际执行。Blender4.5.13已下载校验并运行；场景预检脚本在合成网格中验证了四骨影响与无权重定位、修正后通过。

用户本轮没有提供要制作的角色模型，作者工程/图标包也未取得。因此没有生成真实人物VPK，没有完成2.3.0模板实模编译、Left4Neko眼动或游戏内验收。后续按用户选定角色与输入工程继续，不把视频里的成品当成本机交付。

用户已要求暂缓处理下载不顺的工具/软件，缺失项只登记在工具表。独立只读前向测试确认技能能区分原版兼容目标与Left4Neko/NekoShaders依赖；本批没有覆盖“把任意现有眼动键变成纯原版动态眼动”的完整制作方案，这一分支需要将来的指定材料或实模补充，不自动扩展第1–6集范围。

## 第二批：序号7–12（2026-09-08）

开始前检查本账本和`learning`已有元数据：仅有第一批六个BVID，没有BV1Y61RYPERF或下列CID学习记录，因此本批不重新处理TC5B5。确切范围由原会话最后的编号学习顺序确定，共13个分P，其他P及“可追加”的手模实录未扩学。

来源：[最初的轻语《【求生之路2】新-纯blender流程人物mod制作教程》](https://www.bilibili.com/video/BV1Y61RYPERF/)。BVID **BV1Y61RYPERF**，作者UID34945948，合集发布时间**2024-10-05 18:47:21 +08:00**（1728125241）；这个日期不当成每P独立上传/换稿日期。视频界面为Blender4.2.2 LTS、CATS4.2.1.3、Crowbar0.74、VTFEdit Reloaded等，详细组件状态见工具链。

| 学习序号 | 指定分P与标题 | 当前CID | 元数据时长 | 8秒帧 / 联系表 | 核心审核点 |
|---|---|---:|---:|---:|---|
| 7 | [P4 骨架合并（权重嫁接）](https://www.bilibili.com/video/BV1Y61RYPERF/?p=4) | 26151880544 | 03:19 | 25 / 3 | 00:03–03:12保留MMD蒙皮、对齐官方骨、最终Base方向；脊柱预设只限示例 |
| 8 | [P6 VRD、飘动骨骼轴向调整和重命名](https://www.bilibili.com/video/BV1Y61RYPERF/?p=6) | 26151946033 | 06:09 | 46 / 4 | 02:40的127预算冲突；04:13–05:11轴向转换/无约束简化需限定 |
| 8 | [P7 飘动骨骼轴向plus](https://www.bilibili.com/video/BV1Y61RYPERF/?p=7) | 26151945816 | 02:59 | 23 / 2 | 00:21–01:46不同输入的roll/局部轴；01:50–02:13范围包含0而非严格正负 |
| 8 | [P12 VRD数据生成](https://www.bilibili.com/video/BV1Y61RYPERF/?p=12) | 26152075449 | 07:41 | 58 / 5 | 00:57–06:58样本、驱动映射、trigger混合范围；07:28确认为传统survivor.vrd |
| 8 | [P13 飘动骨骼数据生成](https://www.bilibili.com/video/BV1Y61RYPERF/?p=13) | 26152075578 | 04:57 | 37 / 4 | 分参数组生成$jigglebone；04:14–04:54作者区分yaw/pitch范围与圆锥约束 |
| 9 | [P8 形态键表情处理](https://www.bilibili.com/video/BV1Y61RYPERF/?p=8) | 26152012179 | 12:49 | 96 / 8 | 示例删层不泛化；04:10–06:17 VTA帧而非数字键名；10:23–10:55 Join as Shapes |
| 10 | [P19 第一人称手臂制作](https://www.bilibili.com/video/BV1Y61RYPERF/?p=19) | 26152797093 | 19:47 | 149 / 13 | 独立arms、掌指对齐、Fix Shear条件；16:00配反自更正及18:40最终帧1/2/3；传统arms VRD |
| 11 | [P5 模型大小注意事项](https://www.bilibili.com/video/BV1Y61RYPERF/?p=5) | 26151879933 | 00:57 | 7 / 1 | 00:07–00:53短腿/原版动作匹配风险，不默认擅改比例 |
| 11 | [P14 移动和缩放注意事项](https://www.bilibili.com/video/BV1Y61RYPERF/?p=14) | 26152076314 | 04:31 | 34 / 3 | 00:11–01:42仅proportions平移与01:52起真实缩放分支；原生游标回原点纠错 |
| 11 | [P15 陷地修复](https://www.bilibili.com/video/BV1Y61RYPERF/?p=15) | 26152992849 | 04:28 | 34 / 3 | 高跟鞋proportions/复制足IK末端；新骨计预算；127/128并列、不豁免过渡穿地 |
| 12 | [P9 材质处理](https://www.bilibili.com/video/BV1Y61RYPERF/?p=9) | 26152079178 | 09:36 | 72 / 6 | 00:49–03:21单/双面及透明冲突先分组；face命名为假眼追模板所需 |
| 12 | [P10 基础材质编写](https://www.bilibili.com/video/BV1Y61RYPERF/?p=10) | 26152010574 | 06:12 | 47 / 4 | 保留PNG；VertexLitGeneric模板与通道条件；03:51–04:41 nocull正解；Alpha测试不是连续半透 |
| 12 | [P16 二次元脸部法线处理](https://www.bilibili.com/video/BV1Y61RYPERF/?p=16) | 26152079196 | 04:30 | 34 / 3 | 00:04–04:25临时球源、遮罩、Data Transfer仅法线，保留Armature与Flex；末尾3警告未展开 |

### 第二批实际提取与观看范围

13P元数据总时长 **5275秒（87分55秒）**；完整公开720p媒体逐P用ffprobe核对，实测与整数元数据相差均小于3秒。生成 **662张8秒常规帧、59张常规联系表**及关键处额外补帧。四个分工均已按完整时间线看完所属联系表，操作面板、参数、QC和自更正处另查原帧。不是逐帧连续观看，OCR不是字幕。

这些视频有实际配音：全部13P使用**本机已有faster-whisper large-v3**转写，完整读取讲解并与画面交叉审核；不再沿用TC5B5六集无配音的判断。P4/P5/P6/P8/P9/P10/P14/P15/P19查询字幕轨为空；P7/P12/P13/P16字幕未单独查询，元数据如实标示，不复制其他P状态。

P19约05:44–09:55画面标“听歌time/少女加速中”；保留全段画面操作证据，ASR成品排除与**05:43–09:58**重叠的两个音乐/边界不确定片段，并在JSON写`excluded_intervals`，剩131个讲解片段。视觉标识边界由1秒补帧确定，不假装是精确音轨分界。

中途view连接失败的P7/P12/P13/P16已通过复用同次取得的准确pages元数据、针对CID取得公开playurl补齐；P19一次备用CDN Range续传补齐111,558,368字节且通过时长检查。**目前没有未取得的指定媒体**。下载不顺工具的待办不包括这些已经补齐的媒体，不再反复请求它们。

### 第二批知识落点与可追溯笔记

证据根为`learning/BV1Y61RYPERF/P04/`等13个独立目录，保留metadata、完整media、probe、frames/index、sheets、OCR、ASR。新增审核笔记沿用项目`learning/notes`，没有另建同名skill：

- [序号7/11：对骨、体型、proportions、足IK](../../../../learning/notes/07-11-review.md)
- [序号8：轴向、VRD、jiggle](../../../../learning/notes/08-review.md)
- [序号9/10：表情和手模](../../../../learning/notes/09-10-review.md)
- [序号12：材质、VMT和面部法线](../../../../learning/notes/12-review.md)

通过的工作规则已写回原`character-workflow.md`和`compile-materials-testing.md`；明确纠错与路线/模板差异写回原`reviewed-corrections.md`；原SKILL入口和`video-learning.md`增加路由及分P/配音摄取说明。第一批知识保留，尤其不把旧课SMD/VTA、传统VRD、proportions局部重导覆盖2026 GLB/Neko路线。新增来源注明2024日期、当前CID、分P时间戳和适用条件。

外部一手核查使用Blender4.1变更、4.2/4.5操作文档、Blender Source Tools导出源码，以及Valve公开骨表、姿态插值、jiggle和VertexLitGeneric实现；具体直接链接在主题参考、纠错表和上述笔记。外部推导不标作作者原话，也不用SDK2013代码替代L4D2实模测试。

### 第二批本机验证与待办

本机执行了13P媒体校验/抽帧/OCR/ASR；原摄取脚本原地增加明确分P与显式本地ASR入口，无新运行时或模型下载。另在Blender4.5.13内存合成网格验证“带Basis/TestFlex的网格仅应用Data Transfer自定义法线”后键数和顶点数保留，法线存在；没有保存/改造角色工程。

2024作者配套工具包、完整QCI/预设、lightwarp及精确插件版本仍待实际文件核查，入口和提取码见`toolchain.md`；本批未下载、安装、购买或反复尝试工具。2026缺失组件继续保留原记录。作者视频中的编译/HLMV/游戏结果不是本机实模结果；未据这些截图宣称纯原版动态眼动已完整复现。

写回后验证：skill-creator结构校验通过（Windows Python以`-X utf8`读取中文文件）；摄取脚本语法及参数入口通过；11份skill/参考/本批笔记的本地Markdown文件链接通过；13P的BVID/分P/CID与账本、媒体时长、OCR和ASR存在性全部一致，无遗留`.part`被误作成品。

独立只读前向验证也通过：给出“现有4.5 GLB/Neko工程、P8眼形、P14抬高、P16脸法线、纯原版目标”的组合请求，读取更新skill的代理保持GLB命名/编译契约，不用数字键直接覆盖AU，不把proportions例外普遍化，只细分临时法线源，并明确原版眼动控制仍需完整模板核验；没有执行角色或游戏改动。

## 第三批：序号13–21（2026-09-08）

先读取原账本及本机已有metadata，再读取用户指定原会话的编号列表。原账本已覆盖1–12共19条媒体，本次新范围是**32条视频/分P**，没有重复提取/学习已记账CID。轻语2024同BVID只新增P17/P18/P20/P21/P22/P23；TC5B5旧2024合集只取P23/P24/P25/P27。序号20按该会话系列展开9片（含预告、工具补充、未剪版和2025补充），未剪与最终篇重叠知识合并审核，但原媒体分别保留。感染者只取指定2021合集4P；视频另引的手模、Witch VRD及后续推荐没有扩学。

### 精确来源清单与审核覆盖

以下时间是当前API整数时长，抽帧间隔以秒计；“帧/表”仅常规采样，不含关键处额外补帧。各BVID的完整标题、作者UID、简介、pubdate、pages/CID保存在`learning/catalog13-21/<BVID>.json`和每P的metadata；合集pubdate不作为每P上传/换稿日期。

| 序号 | 视频/分P | 当前CID | 时长 | 间隔；帧/表 | 核心实际内容/审核落点 |
|---|---|---:|---:|---:|---|
| 13 | [BV1Y61RYPERF P22 从0开始的qc修改](https://www.bilibili.com/video/BV1Y61RYPERF/?p=22) | 26152865036 | 13:08 | 8；99/9 | 02:42–04:11按需LOD/Flex；05:48–10:53动画、IK和proportions顺序 |
| 13 | [同合集P23 定义骨骼qc](https://www.bilibili.com/video/BV1Y61RYPERF/?p=23) | 26152143326 | 02:44 | 8；21/2 | 00:08–02:25骨名保留表不等于definebone坐标/蒙皮合并 |
| 14 | [同合集P17 bill尸体](https://www.bilibili.com/video/BV1Y61RYPERF/?p=17) | 26152141870 | 05:31 | 8；42/4 | 静态副本烘焙表情/姿态；04:08 mostlyopaque并非VMT Alpha |
| 14 | [同合集P18 弗朗西斯light模型编译](https://www.bilibili.com/video/BV1Y61RYPERF/?p=18) | 26152142551 | 05:54 | 8；45/4 | 匹配Francis参考、重导定义/比例，查VRD基准 |
| 15 | [同合集P20 VGUI](https://www.bilibili.com/video/BV1Y61RYPERF/?p=20) | 26152142015 | 02:18 | 8；17/2 | 比例不代替规格、棋盘格不等于Alpha；保留源PNG |
| 16 | [同合集P21 封包和创意工坊发布](https://www.bilibili.com/video/BV1Y61RYPERF/?p=21) | 26152142862 | 04:41 | 8；35/3 | 包根、伴随文件、addoninfo/封面/工坊preview分别核 |
| 16 | [BV1it4y1S7Dg 撬棍上传MOD流程](https://www.bilibili.com/video/BV1it4y1S7Dg/) | 231966778 | 05:43 | 8；43/4 | 2020上传UI；04:38–05:27清云/remote删库法不采纳 |
| 17 | [BV1ms421g7yz 人物MOD工具](https://www.bilibili.com/video/BV1ms421g7yz/) | 1566627936 | 18:16 | 24；46/4 | 00:30–17:33映射、Action/VRD、选中与全部、jiggle、表情配方 |
| 17 | [BV17X4y1v73d P1 T pose](https://www.bilibili.com/video/BV17X4y1v73d/?p=1) | 1178656525 | 06:56 | 8；52/5 | 旋转/子级映射、修正预设；15度手腕和继承设置仅示例 |
| 17 | [同视频P2 骨骼位置对齐](https://www.bilibili.com/video/BV17X4y1v73d/?p=2) | 1178659843 | 00:42 | 8；6/1 | 在T-Pose基础启用位置映射；ASR为空，以画面为据 |
| 18 | [BV1sfRGYWEGK 全局蒙版夜光](https://www.bilibili.com/video/BV1sfRGYWEGK/) | 28791344277 | 06:47 | 8；51/5 | 02:20–05:14发光蒙版不是几何透明度 |
| 18 | [BV1SyyWYKE3K 一致性描边](https://www.bilibili.com/video/BV1SyyWYKE3K/) | 26412191330 | 14:41 | 8；110/10 | 外壳/投影UV不是屏幕等宽；12:32最终UnlitGeneric；PNG纠错 |
| 18 | [BV1rC3F6AEGx 动态贴图](https://www.bilibili.com/video/BV1rC3F6AEGx/) | 40341866790 | 22:10 | 24；56/5 | 10:04–19:39烘焙帧序、VTF、AnimatedTexture；不采固定帧数硬限 |
| 18 | [BV1dS421X7QV 两渐变](https://www.bilibili.com/video/BV1dS421X7QV/) | 1628546556 | 08:25 | 8；63/6 | 01:36–06:32覆盖层Alpha/Sine；sineperiod与秒单位；游戏对白不采 |
| 19 | [BV1Hi4y1q7GM P23 八人包MDL](https://www.bilibili.com/video/BV1Hi4y1q7GM/?p=23) | 1436467938 | 14:20 | 8；108/9 | 不同目标的序列/比例/reference与light资产 |
| 19 | [同合集P24 动画和比尔姿势补充](https://www.bilibili.com/video/BV1Hi4y1q7GM/?p=24) | 1527104259 | 03:06 | 8；24/2 | 01:49–03:04 T-Pose尸体仅占位，与轻语P17对照 |
| 19 | [同合集P25 分包与测试](https://www.bilibili.com/video/BV1Hi4y1q7GM/?p=25) | 1436467865 | 13:21 | 8；100/9 | 共享材料依赖/独立包两分支，逐目标VGUI映射 |
| 19 | [同合集P27 别人Mod转八人](https://www.bilibili.com/video/BV1Hi4y1q7GM/?p=27) | 1436467983 | 29:03 | 24；73/7 | 06:38–09:27实际动画基底不等于替换位；light拉长不豁免 |
| 19 | [BV1ymT16pEPL L4N2.34生还者转换](https://www.bilibili.com/video/BV1ymT16pEPL/) | 39679429731 | 03:45 | 8；28/3 | 转换器、身体/FPS及参考组；不据附带工具推断运行依赖 |
| 20 | [BV1QxvYeoEVp McQueen工具篇](https://www.bilibili.com/video/BV1QxvYeoEVp/) | 500001634858919 | 07:50 | 8；59/5 | 历史Max/FBX工具链、路径和商业插件非通用前提 |
| 20 | [BV1PLvreqEtf 2024预告](https://www.bilibili.com/video/BV1PLvreqEtf/) | 500001632522630 | 01:53 | 8；14/2 | 系列路线/效果展示，不当实际制作验证 |
| 20 | [BV1y1iueSE5o 工具补充](https://www.bilibili.com/video/BV1y1iueSE5o/) | 500001635751966 | 01:43 | 8；13/2 | 补充工具配置条件，与本机已安装状态分开 |
| 20 | [BV1CSaDeWEkG 模型预处理](https://www.bilibili.com/video/BV1CSaDeWEkG/) | 500001641502948 | 27:23 | 24；69/6 | FBX/MMD、CATS/精简/合骨和导出；125/127/10万不是普遍硬限 |
| 20 | [BV1JDYXexEw5 模型前置处理](https://www.bilibili.com/video/BV1JDYXexEw5/) | 500001646297429 | 25:12 | 24；63/6 | Max嫁接/VTA模板、NekoVTF/Patch、自更正假眼路径 |
| 20 | [BV1yXbwejEqC VRD/飘动](https://www.bilibili.com/video/BV1yXbwejEqC/) | 25937707511 | 19:40 | 24；50/5 | Neko读姿态SMD；17:23–17:36重力蓝轴说法纠正 |
| 20 | [BV1UxUKYFECq 手模/封包原声未剪](https://www.bilibili.com/video/BV1UxUKYFECq/) | 26743213815 | 91:11 | 24；228/19 | 29:51–61:04 Skin Wrap/逐指刷权；生产路径纠错，保留重复素材证据 |
| 20 | [BV1LVzqYTE6F 手模/UI/打包最终篇](https://www.bilibili.com/video/BV1LVzqYTE6F/) | 27089046116 | 32:01 | 24；80/7 | Wrap方向纠错、21:24–22:41生产路径；拒绝清空hl2材料目录 |
| 20 | [BV1MyXXYuEmy 2025补充](https://www.bilibili.com/video/BV1MyXXYuEmy/) | 28635956869 | 29:34 | 24；74/7 | 4.0层级递减、4.3拇指/Editable Poly、选骨修复与足VRD取舍 |
| 21 | [BV15y4y1b7z2 P1 小僵尸](https://www.bilibili.com/video/BV15y4y1b7z2/?p=1) | 322236724 | 69:04 | 24；173/15 | 对骨/QC变体、多帧眼口、染色/半透失败、66:22起物品附件 |
| 21 | [同合集P2 tank](https://www.bilibili.com/video/BV15y4y1b7z2/?p=2) | 332057401 | 61:55 | 24；155/13 | Tank基准/比例/倒卧物理参考；未制作FPS，任意方向不合格 |
| 21 | [同合集P3 witch](https://www.bilibili.com/video/BV15y4y1b7z2/?p=3) | 332032294 | 60:02 | 24；150/13 | Witch/新娘、染色材料、眼部效果；VRD只提及未完整演示 |
| 21 | [同合集P4 六种特感](https://www.bilibili.com/video/BV15y4y1b7z2/?p=4) | 333767844 | 19:34 | 24；49/5 | 各特感差异、09:12 mouth漏讲字幕、变体/尸块/碰撞；拒零缩放 |

作者和发布时间（北京时间日期，来自本次API而非录制桌面日期）：轻语2024合集2024-10-05，猫嘤猫嘤猫上传课2020-09-04，织梦者の手工具课2024-06-05，轻语T-Pose两P 2023-06-28；冰糖燉雪离夜光2025-03-10/动态2026-07-27，映入红瞳的小云雀描边2024-10-22，Mfffffish渐变2024-07-27（桌面录制日期7月26日）；TC5B5旧合集2024-01-18，Starfelll转换2026-07-05，轻语感染者合集2021-04-04。

メジロ_McQueen九片按上表次序为2024-08-01、2024-07-30、2024-08-02、2024-08-07、2024-08-11、2024-09-20、2024-11-13、2024-11-29、2025-03-01。TC旧合集当前简介提示已有2026新版，故旧多角色路线保留条件，不覆盖本项目2026 GLB主线。各冲突同时记录源时间、模板/模型适用条件和采纳决定。

### 第三批实际提取与可信度

32条元数据总时长**37713秒（10小时28分33秒）**。取得完整公开媒体，ffprobe实测与整数元数据时长均相差小于3秒；27条720p，2020Crowbar上传课与感染者四P共5条360p。本批没有未取得的指定媒体。

生成**2196张常规帧、199张常规联系表**，主代理按完整时间线逐张查看全部联系表；QC/参数、作者自更正、红字及模型示例处查看原帧/补帧。本批未用分工代理。8/24秒采样与连续逐帧观看不同，短暂操作可能需将来按实际工程再定位；低清不能辨读的长代码留待实际模板，不编造补齐。

除L4N短演示外31条完成本地large-v3 ASR阶段并读取底稿，但不等于31份可靠字幕：T-Pose P2为空，渐变课三条为游戏英语/音乐不采；T-Pose P1、工具课、部分Max/感染者长段有重复、超长、时间越界等，均不把该文字/跨度当已验证讲解。仍以画面、可辨短讲解和外部一手依据交叉审核。平台字幕本批未查询，metadata明确记录而非假记“无字幕”。

OCR只有轻语P22/P23完整，P17保留部分中间结果；其余以人工视觉读联系表/原帧为主，不声称全32条OCR齐备。`transcript.partial.json`保留为明确未完成的原始检查点，不能代替最终转写或覆盖证明。具体可靠性限制见各笔记及[视频学习规范](video-learning.md)。

### 第三批写回位置

审核记录仍放原项目`learning/notes`，通过知识写回原skill及原有六个主题参考，没有另建同名skill：

- [13–16：QC、Bill尸体、light、VGUI、发布](../../../../learning/notes/13-16-review.md)
- [17：人物工具与T-Pose自动化](../../../../learning/notes/17-review.md)
- [18：蒙版夜光、描边、动态纹理、双渐变](../../../../learning/notes/18-review.md)
- [19：多角色适配与转换](../../../../learning/notes/19-review.md)
- [20：McQueen九片含2025版本修复](../../../../learning/notes/20-review.md)
- [21：感染者四P及未覆盖项](../../../../learning/notes/21-review.md)

原`character-workflow.md`增加自动化、Max及明确指定的感染者分支；原`compile-materials-testing.md`增加QC/特殊资产、VGUI发布、可选材质、多角色、Max手模及感染者验收；原`reviewed-corrections.md`保存旧说法/冲突和条件。原`SKILL.md`更新入口而不更名，`toolchain.md`记录来源/当前版本与未取得组件，`video-learning.md`明确长实录采样和ASR/OCR质量。

外部核查仅采用直接一手资料：角色工具与BoneAnimCopy作者仓库、Crowbar官方发行、Steam Cloud文档、Valve公开材质/代理/jiggle代码、W3C PNG、Autodesk Skin Wrap和MQTool作者仓库；直接链接放相应主题/纠错笔记。公开SDK2013不等于L4D2/Neko分支实测，新版仓库README也不等于完整源码审计或已安装版本。

### 本机验证与尚待实作的边界

本批只执行媒体校验、抽帧/选定OCR/本地ASR和知识文件更新；原摄取脚本增加ASR关闭前文条件化及明确中间检查点，批次脚本复用原入口。没有新工具/模型下载、没有安装或执行作者脚本、没有真实人物/感染者编译、VPK部署、游戏测试或工坊发布。前两批的Blender合成小样是历史记录，不在本批重复冒记。

作者完整QC/QCI、Max工具/预设、L4N转换器参考及感染者模板等仍待实际文件；既有2026/2024包缺口保留。用户要求下载不顺就记待办，本批未为其反复尝试。感染者FPS、Witch完整VRD、纯原版动态眼动完整复现，以及低清未能读清的模板内容不标已解决；这不改变本次指定媒体已经提取和审核的事实。

第三批写回后校验通过：原skill的quick_validate（Windows Python `-X utf8`）有效；原摄取脚本与本次批次脚本语法、原参数入口通过。32个BVID/P/CID去重键唯一，逐项与账本/metadata核对一致，媒体实测最大时差1.067秒、文件大小与probe相符、全部常规帧存在，无`media.mp4.part`混作成品；2196帧/199表、31份ASR文件及2份完整/1份部分OCR与上述声明一致。13份skill/参考/本批笔记的48个本地Markdown链接均有效。此项验证不包含角色实模编译或游戏效果。

## 第四批：McQueen2023完整10P（2026-09-08）

来源：[《求生之路2人物模组制作教程》BV1ug4y1j7Lj](https://www.bilibili.com/video/BV1ug4y1j7Lj/)，作者**メジロ_McQueen**，UID454130937。开始先读本账本并搜索现有skill、笔记及metadata，没有本BVID/这10个CID记录；已学同作者2024/2025系列为独立来源，所以不重学旧片，仅对重叠知识合并审核并保留出处。

公开API确认当前10个分P，总长**14694秒（4小时4分54秒）**。合集pubdate=1682928047，即2023-05-01 16:00:47 +08:00；P10另有ctime=1683341614，即2023-05-06 10:53:34 +08:00。ctime字段独立保留，不以合集日期冒充各P上传/换稿日期。完整返回在`learning/BV1ug4y1j7Lj/catalog.json`，每P metadata有作者、简介、CID、page、part、duration和来源说明。

| 分P与原标题 | CID | 元数据时长 | 常规帧/联系表 | 核心提取与审核 |
|---|---:|---:|---:|---|
| [P1 模型的预处理](https://www.bilibili.com/video/BV1ug4y1j7Lj/?p=1) | 1114894867 | 12:46 | 96/8 | 02:16–07:52 CATS/形态键检查与分离；04:31固定顶点数不泛化；08:43腕对称修正仅示例；FBX中转 |
| [P2 对骨操作](https://www.bilibili.com/video/BV1ug4y1j7Lj/?p=2) | 1114916937 | 24:23 | 61/6 | 00:13绿色Morpher误说；06:38仅XYZ Pivot位置对齐；脊柱/指序与22:49漏接修复 |
| [P3 飘动骨骼的轴向调整以及权重的嫁接](https://www.bilibili.com/video/BV1ug4y1j7Lj/?p=3) | 1114916999 | 21:35 | 54/5 | 01:35先存Skin封套、折叠副本；05:15局部轴；18:17–20:19按骨名/顶点索引分别匹配 |
| [P4 SMD导出和贴图处理以及QC编写](https://www.bilibili.com/video/BV1ug4y1j7Lj/?p=4) | 1114920941 | 27:55 | 70/6 | VTF/VMT、Zoey动画→Ellis；19:12 SMD exporter1.7；21:49–25:36定义骨、tz.smd及Perl ref模板条件 |
| [P5 VRD的编写](https://www.bilibili.com/video/BV1ug4y1j7Lj/?p=5) | 1114942872 | 27:28 | 69/6 | 06:23 SourceOps非SourceIO；手写helper_bones.vrd父空间基准/样本；23:33–26:53深蹲未完全修复 |
| [P6 飘动骨骼的编写](https://www.bilibili.com/video/BV1ug4y1j7Lj/?p=6) | 1114923500 | 20:06 | 51/5 | 分组jiggle参数；03:22“49”限模板未证实；17:05–17:34手骨误选后改袖骨；跑动仍须调 |
| [P7 表情的制作](https://www.bilibili.com/video/BV1ug4y1j7Lj/?p=7) | 1114934696 | 18:39 | 47/4 | 01:38蓝色Morpher可用；03:12 defaultflex25/0–25；抬眼2/4留中性；VTA/控制器对应 |
| [P8 手摸的制作（俩种方法）](https://www.bilibili.com/video/BV1ug4y1j7Lj/?p=8) | 1114952266 | 42:48 | 107/9 | 17:12 Wrap→Skin、22:13原Skin嫁接；26:39漏封套返工；刷权、FPS导出；必须结合P10撤回 |
| [P9 补充VPK内容以及打包上传工坊](https://www.bilibili.com/video/BV1ug4y1j7Lj/?p=9) | 1114949023 | 31:08 | 78/7 | 三类VGUI、倒地图Alpha、包根与addoninfo；29:36只是Publish草稿讲解，不是成功上传 |
| [P10 对视频内容的一些补充](https://www.bilibili.com/video/BV1ug4y1j7Lj/?p=10) | 1119983849 | 18:06 | 46/4 | 00:42模板获同意分享；PMX命名/FBX；07:11及12:26后撤回直接手模嫁接偏好；材质/修复条件 |

### 实际取证与高清补证

初始经公开播放接口取得10份完整360p音画，P1每8秒、其余每24秒抽帧，共**679张常规帧、60张联系表**；主代理按各P时间线查看全部联系表。随后用户指出已登录Chrome能1080p并明确许可调用，实际页面各P显示1080P60，已读取的视频解码尺寸1920×1080。借助该已授权页面观察到的媒体资源，取得**10份完整1080p60画面流**，单独保存在各P `hd/video.m4s`，共**5,280,213,574字节**；原低清媒体及学习记录未覆盖。

HD每P保留media_probe、provenance及关键帧，共**73张高清选点/补帧**。QC、程序骨、Morpher、Skin/Wrap面板、导出与作者纠错处已据高清原帧复核，高清截图不是作者模板本体。此次是全时间线抽帧概览＋全ASR底稿＋高清关键处审核，不是四小时逐帧连续观看，也不把高清补证重复计算成20P。

平台字幕未查询，未做全片OCR。全部10P共**3295个未经校订的本地ASR片段**：P1/P3用原large-v3 float16逐段入口，其余8P用已有BatchedInferencePipeline/int8_float16/batch4，单GPU进程。底稿全部读取但不等于3295条准确字幕：P2部分长片段定位粗、P3末段越界，P9 25:20–27:20和P10约13:33–13:49有重复/幻听；不作为有效叙述或准确边界。英文骨名、tz而非ASR的tj、工具名与模板数字以画面校正。

### 原文件写回与冲突保留

- [十P逐段审核笔记](../../../../learning/notes/2023-mcqueen-review.md)：每P的实际内容、时间段、原说法、采纳条件与未涵盖项。
- 原[character-workflow.md](character-workflow.md)第14节：封套/父级嫁接、按名与按索引的区别、SourceOps父空间VRD、Morpher颜色及VTA默认帧25。
- 原[compile-materials-testing.md](compile-materials-testing.md)第16节：tz/ref旧模板、lightwarp、两种手模方法及P10回归、VGUI/发布边界。
- 原[reviewed-corrections.md](reviewed-corrections.md)：保留19组旧说法/自更正/冲突条件；包括P2对P7的Morpher、P8对P10的手模和其他系列默认帧差异。
- 原SKILL入口、[toolchain.md](toolchain.md)、[video-learning.md](video-learning.md)同步路由、版本/待办、补充课优先和用户授权高清补证方法。未另建同名skill，也未修改其他项目skill。

外部一手核查为Autodesk Morpher/Skin封套/Skin Wrap、SourceOps实际坐标操作源码、SourceIO/CATS作者资料与Valve公开骨表/jiggle实现；链接紧邻主题/纠错结论。不能把今日源码当成录像实际插件版本，也不能将公开SDK2013当L4D2所有分支实测。

### 待办与验证边界

本批视频音画与高清补证已取得，无未下载的指定媒体。仍待**ui人物模板2022稳定版完整包、实际Max SMD/VTA插件、完整QC/QCI、BAT/PL及其Perl依赖**；Wunderboy作者页访问失败后未反复尝试，旧分享口令只登记。P10的许可声明不替代实际资源包授权范围核验。原2026/2024待办全部保留，未为本课安装/升级/购买软件。

没有真实角色输入的编译、VPK部署、游戏测试或工坊发布。P5手腕VRD、P7完整眼追/RNG、本套light/Bill尸体实作不标为新学成能力；其他来源已有对应知识继续保留。

写回检查：quick_validate通过，两个本批证据脚本语法通过；10个去重键唯一且与元数据/账本一致。媒体与HD全部通过时长探测，最大元数据时差**1.066秒**，无遗留`.part`冒充成品；679帧/60表/73高清帧/10份ASR与本节一致。此项检查仅针对证据与技能文件，不是角色实模验收。

## 第五批：表情、眼动与调试六条（2026-09-09）

范围由[本批任务清单](../../../../learning/next-batch-2026-09-09.md)限定。开始按BVID+P+CID搜索原账本、笔记和本地metadata：P11只存在于旧合集pages目录，不是已学分P；其他五条没有学习证据。按原顺序独立获取并审核，没有重学整套27P或追看简介中的其他视频。

当前view响应、精确作者UID/简介/pubdate/pages保存于`learning/catalog-face-20260909/<BVID>.json`；所有实际媒体均在`learning/<BVID>/Pxx/`，包含metadata、media.mp4、media_probe、frames/index、sheets和全画面OCR。当前CID/时长与清单一致，无换稿覆盖。总时长7328秒（2:02:08），实际媒体共734,983,040字节，五条720p、一条360p，最大元数据时差0.934秒。

| 序号/视频 | 作者；发布日期 | CID | 时长；分辨率 | 间隔；帧/表 | 审核落点 |
|---|---|---:|---|---|---|
| 1 [BV1Hi4y1q7GM P11](https://www.bilibili.com/video/BV1Hi4y1q7GM/?p=11) 利用面部骨骼制作表情形态键 | TC5B5 UID5421387；合集2024-01-18 | 1436467405 | 25:27；1280×720 | 24；64/6 | 01:22复制修改器、01:23.5应用副本为键、01:39复位；眉/眼/唇/下颌补键和22分起近似配方 |
| 2 [BV1rP411W7iN P1](https://www.bilibili.com/video/BV1rP411W7iN/) 第6章表情、眼球追踪、贴图参数 | 原作MLUIdgb；补档UP账号已注销 UID412572446；2023-08-12 | 1231736700 | 32:58；1280×720 | 24；83/7 | Max2019脸骨/VTA；18:48 EyeRefract；QC Eyes高度测量；31分取消隐藏重导的自修复 |
| 3 [BV1SY4y1L7Uo P1](https://www.bilibili.com/video/BV1SY4y1L7Uo/) 动漫人物眼球追踪 | Kokkorylien UID2100612；2022-07-18 | 776502561 | 14:50；852×360 | 8；112/10 | 覆盖曲面、左右材质、虹膜留白、游戏展示；当前简介的ambient.vtf及方向/变形器问题；长QC待文件 |
| 4 [BV1ZSpQzJEAV P1](https://www.bilibili.com/video/BV1ZSpQzJEAV/) 二次元面部适配 | 鱼不吃茄子 UID5946944；2025-09-20 | 32504218854 | 37:45；1280×720 | 24；95/8 | Mix成键、内眼眶填面、材料实际分配、负Y符号、eyelid帧和位置值纠错 |
| 5 [BV1am421H7Dw P1](https://www.bilibili.com/video/BV1am421H7Dw/) HLMV++手模V模动画预览 | Starfelll UID644686972；2024-05-06 | 1533626100 | 03:05；1280×720 | 8；23/2 | Submodels/Add (Steam)、武器主V模＋arms、Sequence层、重编及缺材质状态 |
| 6 [BV1kaxCz6Egb P1](https://www.bilibili.com/video/BV1kaxCz6Egb/) Blender PBR流程打通L4D2 | Starfelll UID644686972；2025-10-09 | 32947307223 | 08:03；1280×720 | 8；61/6 | 烘焙→MareTF→VMT→引擎重载；PBR扩展；Nekook开发挂载与最终VPK依赖区别 |

### 实际审核覆盖

438张常规帧、39张常规联系表按完整时间线全部查看；关键原帧逐项打开。P11额外12张选点原帧和一张半秒联系表捕获短菜单，不计入上述常规数量。逐点记录在[人工复核索引](../../../../learning/catalog-face-20260909/reviewed-evidence.json)。不是逐帧连续观看，也没有把360p放大当高清源码。

六份OCR完整，但文字仍为机器底稿，不冒充校订字幕。六条各做30–60秒音轨样本；第2/3/4条讲解与画面吻合，三份全文ASR共1495段（376/262/857）已读并对照。第1/6条样本无有效文字，第5条疑似歌曲，不作为讲解，未做这三条全片ASR；空样本不证明全片无配音。平台字幕未查询。当前模型没有直接音频听审输入，因此方法如实记录为视觉＋本地ASR，而非逐句听审。第2条长跨度ASR的按钮时点以原帧补正；第3条09:15以后仍有作者评论配音，不误删成游戏对白。

### 写回、外部核查与本机验证

[六条详细笔记](../../../../learning/notes/2026-09-09-face-review.md)保存时间/操作/纠错/条件，原SKILL入口、character-workflow第15节、compile-materials-testing第17节、reviewed-corrections和工具/学习规范已更新；新增独立内容足够的[face-eye-diagnostics.md](face-eye-diagnostics.md)，没有另建同名skill。

外部直接依据包括Blender4.5修改器、Valve QC Eyes/C_BaseFlex/EyeRefract、NekoMDL作者、USQC作者实际flexrules、MareTF与Nekook作者说明，链接紧邻笔记和主题结论。VDC三页访问受限，没有声称读到其正文；公开SDK只用于校正语义，不冒称L4D2全部分支实测。

本机新增验证仅为4.5.13内存合成三角面两种捕获方法，结果见[blender-capture-test.json](../../../../learning/catalog-face-20260909/blender-capture-test.json)，未使用真实角色、未写blend。媒体处理复用原提取器，只有本批固定清单调度和小样脚本新增；未下载/安装建模插件、运行扩展或ASR依赖，未游戏部署/工坊发布。

未完成能力仍是：本机纯原版动态眼追、实际2.3.0/2026模板编译、HLMV++实模联动、隔离开发资源后的最终VPK验收、LOD性能与标准人物工程。Kokkorylien低清长QC及三位作者的实际VMT/QCI/辅助图包仍待文件核查；鱼不吃茄子片内明确略过材质完整写法。媒体本身六条均已取得，不将这些复现缺口写成“未下载视频”。

写回检查通过：skill-creator quick_validate有效；本批三个脚本语法及采集参数入口通过；六个去重键与当前catalog/metadata/账本一致，438帧/39表/6份OCR/3份ASR数量和文件完整，无遗留media.mp4.part冒充成品。原SKILL、七份参考及本批笔记共9份Markdown的84个本地文件/目录链接有效。逐项结果见[validation.json](../../../../learning/catalog-face-20260909/validation.json)。这些检查不包含真实人物编译或游戏运行。

## 第六批：后续路线图A/B/C（2026-09-09）

只处理[路线图](../../../../learning/supplemental-video-roadmap-2026-09-09.md)序号1—12，按BVID＋实际P＋CID核去重，原67条无同键完成记录。没有重学旧来源；实际P4以独立目录取证，没有扩学它的其他6P。D/E/F/O未处理，候选清单保持候选语义。

### 逐条状态与审核落点

当前API响应保存在`learning/catalog-abc-20260909/<BVID>.json`，每项metadata含作者UID/简介/pubdate/pages与获取日期；多P合集日期不冒作各P上传时间。清单12项标称8080秒（2:14:40），**已完成11项7576秒（2:06:16）**。下表“帧/表”为原公开媒体的常规采样，非高清全片逐帧。

| 路线图序号与入口 | 作者；日期 | 实际P / CID | 时长；间隔；帧/表 | 状态与实际新增审核 |
|---|---|---|---|---|
| 1 [LOD概念 / BV1ipfHYCEwT](https://www.bilibili.com/video/BV1ipfHYCEwT/) | 地精今天建模了吗；2025-01-26 | P1 / 28052882543 | 01:41；8；13/2 | 已审；几何LOD/切换区分，01:10统一UV说法收窄，不承诺必省显存 |
| 2 [五种减面 / BV1xH4y1B7rz](https://www.bilibili.com/video/BV1xH4y1B7rz/) | Zimon3D；2023-11-08 | P1 / 1324980775 | 01:47；8；14/2 | 已审；反细分/Collapse/重构/人工拓扑选型，保UV不等于保Flex/蒙皮 |
| 3 [LOD网格 / BV1v3USYbEnZ](https://www.bilibili.com/video/BV1v3USYbEnZ/) | 霸王奉先；2024-11-21 | P1 / 26873431952 | 05:29；8；41/4 | 已审；Blender4.1静态舰船、统计/副本/Apply，不等于Source LOD接入 |
| 4 [重拓扑纹理迁移 / BV1bBbK6kE14](https://www.bilibili.com/video/BV1bBbK6kE14/) | Blendergo；2026-09-07 | P1 / 41663923455 | 09:58；8；75/7 | 已审；4.5.11基础色重烘焙、活动对象/图像、距离与片尾残缺；非全部PBR恢复 |
| 5 [mipmap与编码 / BV11G41187Zu](https://www.bilibili.com/video/BV11G41187Zu/) | Paper朱；2022-08-09 | P1 / 798681987 | 标称08:24；完整采样无 | **待补、未学**；公开流仅30.100313秒，授权Chrome仍要求作者充电档。官方原理补证不冒充本片 |
| 6 [VTFEdit / BV1Ax411s78S](https://www.bilibili.com/video/BV1Ax411s78S/?p=4) | 御琪幽然；合集2017-08-02 | P4 / 21101872 | 17:18；24；44/4 | 已审；1.3.3导入导出/Mask、PNG错说与BMP自更正、Normal Format与法线区分 |
| 7 [SP2VTF / BV17qhP6pEMV](https://www.bilibili.com/video/BV17qhP6pEMV/) | 小小少女不饮酒；2026-08-24 | P1 / 41220968358 | 09:39；8；73/7 | 已审；作者身份/版本分层、Color/Alpha真实槽、19base/0bump、模糊匹配/覆盖风险 |
| 8 [法线压缩 / BV1zuHizBE8c](https://www.bilibili.com/video/BV1zuHizBE8c/) | Starfelll；2025-09-11 | P1 / 32315278589 | 02:04；8；16/2 | 已审；L4N1.6.5/PBR、ATI2N与DXT5nm，输入方向与匹配解码，非原版通用保证 |
| 9 [绑骨刷权 / BV1z5zQBGEyQ](https://www.bilibili.com/video/BV1z5zQBGEyQ/) | Paper朱；2026-01-26 | P1 / 35604401980 | 24:07；24；61/6 | 已审；5.0.1空组/活动对象/投射/关节环线；任意rig非Valve，18:40绝对权重解释修正 |
| 10 [修复人物权重 / BV1nGzQByEWK](https://www.bilibili.com/video/BV1nGzQByEWK/) | Paper朱；2026-01-27 | P1 / 35604596365 | 04:19；8；33/3 | 已审；5.0.1抬臂串权与局部修复，不把所有尖点都解释成需Ctrl减权 |
| 11 [权重粘连 / BV1DszsBSEZc](https://www.bilibili.com/video/BV1DszsBSEZc/) | Zimon3D；2026-01-22 | P1 / 35542205934 | 01:16；8；10/1 | 已审；5.0.0耳机误受前臂组影响，逐邻骨定位，赋0与Remove区别 |
| 12 [手模转权实录 / BV12pT56uEE8](https://www.bilibili.com/video/BV12pT56uEE8/) | 鱼不吃茄子；2026-06-29 | P1 / 39497697505 | 48:38；24；122/11 | 已审；4.5.11/CATS4.5.3.2，25:00原生转权/最近面顶点、逐指修形，有限挂载测试 |

### 音画与高清证据质量

11份完整公开媒体共462,100,457字节，均通过时长校验；502张常规帧/49张联系表全部按时间线看完。原媒体有横屏720p、两条720×1280竖屏，6号仅576×360；实际尺寸逐项在media_probe中，不统一标为高清。11份OCR完整但仅作定位底稿。

9条配音课全文ASR共2076段读取并校对；英文工具/骨名、源目标顺序与“面数/部件”混词以原帧为准。8/12只有分布音轨样本ASR，没有可靠叙述，幻听剔除出知识；没有全片逐句听审、没有把空样本当全片无配音证明。平台字幕未查询，详见[逐条笔记](../../../../learning/notes/2026-09-09-abc-review.md)。

用户明确授权Chrome后，为4/6/7/8/12取得5份完整高清video-only流，共708,190,326字节；保存于各P的`hd/video.m4s`，原音画不覆盖。分辨率为1920×1080/30、1680×1048/30、1916×1076/30、1920×1080/60、1920×1080/60，77张选点/短按钮补帧中实际打开的关键帧单列于[复核索引](../../../../learning/catalog-abc-20260909/reviewed-evidence.json)，不把保存77张自动说成全部已逐张审核。12号25:03/25:06短面板明确“最近的面顶点”，纠正按粗概览猜测最近面插值的风险。

5号试看文件保留为`preview-only.mp4`；没有media_probe完成标志、没有完整帧/OCR/ASR，不计入以上数量。[访问缺口](../../../../learning/catalog-abc-20260909/BV11G41187Zu-access-pending.json)记录公开标记与授权Chrome页面结果，不执行充电支付或绕过。已取得11条不列入媒体待下载。

### 写回与实际验证

原SKILL增加路由与78条/1项待补的真实范围；工作流第16–17节补减面/数据契约和无蒙皮/错权重诊断；编译参考第18–19节补基础色烘焙、VTF/mips、SP2VTF/法线扩展与原生转权手模。原纠错表保存原说法/时间/采纳条件；工具链与学习规范同步版本、试听限制及授权高清流程。候选路线图未改成已掌握清单，前批结论保留。

外部补证为Blender4.5官方缓存段落、微软mips/块压缩资料、MareTF说明及SP2VTF作者固定提交的scan/convert实现；逐条区分视频原话、当前文档和静态代码。源码存在与README说法不证明发行包已安装/完整审核，精确链接见笔记。无新工具/插件/模型/运行扩展安装。

本机仅执行证据处理及[4.5.13内存语义测试](../../../../learning/catalog-abc-20260909/blender-semantics-test.json)，验证带键减面报错、单骨相对权重和赋0/移除成员差异。没有角色工程改造、编译、VPK部署或游戏测试。后续缺口仍是实际人物LOD接入/性能、匹配2.3.0模板与标准人物/纯原版眼动验收；不由本批观看自动补齐。

本批验证结果由[validation.json](../../../../learning/catalog-abc-20260909/validation.json)记录：验证身份/时长/文件与本地链接及skill结构，不替代真实人物验收。采集失败阶段的fetch-status保留历史状态，5号的最终访问结论以独立access-pending记录为准。

## 第七批：后续路线图D/E/F，序号13—21（2026-09-09）

范围来自[原候选路线图](../../../../learning/supplemental-video-roadmap-2026-09-09.md)和用户本次指定，不是历史第三批同名序号。开始以BVID＋实际P＋CID核原账本/笔记，无同键已完成记录；没有重新学习前78条、没有扩学相关合集或可选22。路线图历史候选清单保持原样，第六批5号仍待完整媒体。

### 逐条状态与审核落点

当前API原响应在`learning/catalog-def-20260909/<BVID>.json`，精确作者UID/简介/pubdate/pages随metadata保留；所有当前CID/标称时长与路线图一致。9个条目、11个实际P均有完整媒体，合计7086秒（1:58:06）；合集日期不冒作每个P上传日期。第21条状态特列，不称完整换装课。

| 路线图入口 | 作者；日期 | 实际P / CID | 时长；间隔；帧/表 | 审核状态与新增落点 |
|---|---|---|---|---|
| 13 [普通碰撞体 / BV1rM411H7Rh](https://www.bilibili.com/video/BV1rM411H7Rh/) | HerobrineAce；2023-03-17 | P1 / 1057537436 | 13:37；8；102/9 | 已审；汽车collisionmodel、Propper/凸壳、同坐标基准；非人物collisionjoints，数值/材质删除范围收窄 |
| 14 [自定义布娃娃 / BV1wu411V72i P1](https://www.bilibili.com/video/BV1wu411V72i/?p=1) | CCCrino；合集2023-07-17 | P1 / 1199969181 | 19:41；24；50/5 | 已审；Max2019脚趾/眼镜、质量/约束、Physics Test，16/8余量、空jiggle/删根和jointcollide条件 |
| 14 [客户端/服务器布娃娃 / P2](https://www.bilibili.com/video/BV1wu411V72i/?p=2) | CCCrino；同合集 | P2 / 1199962343 | 02:35；8；20/2 | 已审；模拟/同步区别，具体实体生成和跨端PHY对应，不泛化所有地图尸体 |
| 15 [Blender布娃娃 / BV1iZ421M7rx P11](https://www.bilibili.com/video/BV1iZ421M7rx/?p=11) | CCCrino；合集2024-06-28 | P11 / 1598985178 | 11:15；8；85/8 | 已审；片内P8、4.1.1已绑定PHY集合、07:39导出206/128警告、模板qz/VRD/参数条件 |
| 16 [Crowbar基础 / BV1Vd4y1d7tp](https://www.bilibili.com/video/BV1Vd4y1d7tp/) | Kevne；2022-08-22 | P1 / 811076120 | 05:32；8；42/4 | 已审；0.72下载与前端/目标编译器区分、独立Preview/View；已有基础合并，发布边界 |
| 17 [参考错位修复 / BV1bKy5Y3Eh8](https://www.bilibili.com/video/BV1bKy5Y3Eh8/) | 映入红瞳的小云雀；2024-10-21 | P1 / 26393839397 | 06:31；8；49/5 | 已审；3.6.7同源健康参考、Armature/Rest Pose顺序；不套枪骨/Z=-65到人物 |
| 18 [QC条件修复 / BV1Kw1xYqEHv](https://www.bilibili.com/video/BV1Kw1xYqEHv/) | 映入红瞳的小云雀；2024-10-26 | P1 / 26476284330 | 15:31；24；39/4 | 已审；idle也会坏、绝对/加算语义、保人物IK/骨定义/序列契约；有限武器例 |
| 19 [DeltaRepair用法 / BV1NJbW6UEJA P1](https://www.bilibili.com/video/BV1NJbW6UEJA/?p=1) | 不会贴皮の久辞，代发；合集2026-09-06 | P1 / 41643805049 | 05:50；8；44/4 | 已审；实际UI1.3.3、原MDL/参考帧/delta/corrective输入，通修说法不采，exe未取得/执行 |
| 19 [2026.9.7更新 / P2](https://www.bilibili.com/video/BV1NJbW6UEJA/?p=2) | 同UP；P2标题2026-09-07更新 | P2 / 41661632047 | 06:13；8；47/4 | 已审；UI1.4.1、逐骨偏移/手选中性参考/QC输出，delta＋subtract原帧核字，不改原件 |
| 20 [RNG材质 / BV19Y411K786](https://www.bilibili.com/video/BV19Y411K786/) | 洛兮菌；2022-06-10 | P1 / 743108815 | 29:59；24；75/7 | 已审；多帧规格、三帧EntityRandom2.99、实体值/UniformNoise/锁存区别；Obsolete与关卡/同步误读 |
| 21 [组件开关 / BV1osNSeqEzK](https://www.bilibili.com/video/BV1osNSeqEzK/) | Starfelll；2025-02-09 | P1 / 28297268726 | 01:22；8；11/1 | **效果审核完成，制作方法未覆盖**；菜单/显隐可见，无QC、准确运行依赖或多人一致性证据 |

### 音画审核的真实覆盖

564张常规帧/53张联系表按完整时间线全部查看；11份OCR完成，只作定位底稿。关键原帧及15号07:39短警告补帧单列[人工复核索引](../../../../learning/catalog-def-20260909/reviewed-evidence.json)，不把常规概览说成逐帧连续观看。

7份全文ASR共1798段已读取：14P1/P2为423/74，15为112，16为155，19P1/P2为125/89，20为820。15号长跨度段落的按钮时点由原帧补正，19号工具名和delta/subtract以界面文本为准，不将机器合词写成命令。11项均做初始音轨样本；13/17/18/21另有分布20秒ASR样本，没有可靠教学叙述，歌词/幻听不入知识。没有全片直接音频听审，不把空样本当全片无配音证明；平台字幕未查询。

在本路线图对话已有用户Chrome许可下，为13/20获取页面实际加载的两份完整高清video-only流，共200,679,627字节。13为1912×1024、24000/1001fps；20为1920×1080、60fps。19张选点保存，实际打开9张HD，其他不自动算逐张看过；15号另存10张密集原帧、实际打开2张。原公开媒体/音轨保持不变，签名查询串不入长期出处记录。Chrome只有相关课程取证，没有订阅、付费或读取凭证库。

### 写回与验证边界

[逐条笔记](../../../../learning/notes/2026-09-09-def-review.md)保存观察、时间、版本、条件、纠错与未覆盖内容；原SKILL更新路由和真实累计，原编译参考新增20—22节，纠错表、工具链和视频学习规范同步。碰撞/关节物理、健康参考/delta诊断、RNG和组件控制分支进入主题，而不是只把候选标题抄到账本。旧规则已存在的Crowbar/导出常识合并，不重复造一份技能。

外部补证为Valve公开ragdoll/studio/mathproxy源码、Facepunch客户端接口、Crowbar作者0.74发布说明、旧RNG作者指南；各自限定来源和分支。VDC部分正文403，只采用可见索引附录；替代SYS指南正文受限未审。未取得DeltaRepair exe/源码或教师完整模板，不假定算法、骨预算、原版兼容或完整换装运行依赖已核。

本机只做媒体/ASR/OCR与文件检查，未做角色工程修改、编译、游戏部署、工坊订阅/发布或新软件/扩展安装。后续真正需要的ragdoll模板、原始QC/动作和控制机制另核；之前NekoMDL2.3.0/2026模板、人物LOD/原版眼追与标准工程验收缺口保留。

[本批验证报告](../../../../learning/catalog-def-20260909/validation.json)检查11个身份键、完整媒体时长/大小、帧/表/OCR/ASR/HD文件和本地链接、四个证据脚本语法及skill结构。它验证取证一致性，不自动证明人工知识判断或真实人物游戏验收。
