# 编译、材质、图标、手模与测试

主线依据TC5B5第5–6集及前4集的输入；第8节起补最初的轻语2024指定分P。本文“第N集”指TC5B5，“P N”指BV1Y61RYPERF。详细时间戳见 [source-ledger.md](source-ledger.md)，已知错漏见 [reviewed-corrections.md](reviewed-corrections.md)。

## 1. 选择编译契约

主线是NekoMDL 2.3.0 + 作者改编的Ultimate Survivor QC v3.8 + GLB/glTF。先取得实际模板和`NewCommands.qci`，检查路径及版本，不能用本机旧NekoMDL1.3.2冒充2.3.0。

| 编译输入/功能 | 配套约束 |
|---|---|
| 主线GLB/glTF | 模型对象名/节点名、骨名、形态键名、选中对象、动画条目与QC匹配；`$NekoModel`、`innode`、`$NekoDriverBone`等为该扩展链路 |
| Neko DMX替代分支 | 作者发布说明给出Binary5/Model18，需按实际工具版本核验；不是本课主要演示输入 |
| 默认L4D2/Blender Source Tools | 当前作者源码L4D2预设为Binary4/Model15；SMD表情还需VTA及其QC帧索引。不要携带Neko专用指令 |

默认引擎与扩展编译器的导出预设不能共用一张“万能参数表”。参考：[Blender Source Tools预设源码](https://github.com/Artfunkel/BlenderSourceTools/blob/master/io_scene_valvesource/utils.py)、[NekoMDL作者说明](https://steamcommunity.com/sharedfiles/filedetails/?id=3142607978)。

## 2. 身体QC检查（第5集00:08–05:28）

核对下列映射，而不是只改最后VPK文件名：

- **目标与动画**：模板的`ref_survivor auto`使用各角色相应动画库；显式改用另一角色动画是独立选择。模板变量不是引擎内建QC指令。
- **材料检索**：`$cdmaterials`相对`materials`根；对应真实VMT目录，VMT再引用真实VTF。
- **主模型路径**：模板`custom_model`指向实际`wmodel.glb`，不是视频的Alice目录。
- **脸部与Flex**：含形态键的网格使用匹配的`$NekoModel`与`innode`；多个脸部对象分别声明自身flex/flexpair，同套控制器库避免重复定义。
- **无Flex部件**：按模板用`$bodygroup`及对应节点；存在bodygroup不代表已实现L4N部件开关。
- **VRD**：控制骨、被驱动骨、GLB动画、pose路径与trigger帧一致，参见人物工作流。
- **飘骨**：正确指令为`$jigglebone`、`$definemacro`。先确认宏定义，再按准确骨名调用；不同头发、饰物、耳尾按效果调参数。批量替换只限已确认选区。
- **脚部IK**：模板`foot_ik_fix`、`calf_ik_fix`、`pps_z_delta`用于相应脚/小腿/骨盆修正。先排除T-Pose、骨轴、层级和权重问题，再按实际动作/地面试调；不复制2.5、0.5等示例值。

查看编译BAT后，把编译器、工作目录、输入、输出指向项目构建目录。先编一个目标；保留日志，查缺失文件/节点/骨骼/材质错误，清点MDL及本次实际生成的VVD/VTX/PHY等伴随文件。无需PHY的资产不凭空补文件，有PHY的资产也不能漏掉。

## 3. 材质与纹理（第5集05:36–13:28）

先确定作品运行环境：原版L4D2材质与NekoShaders `PBR`/`NekoToon`不是无依赖互换。用户要纯原版兼容时采用相应原版材质方案；不要因为录像用了Neko就默认替用户安装扩展。

建立逐材质记录：网格/材质槽 → shader → 颜色/法线/蒙版输入及通道 → 处理输出 → VMT引用路径 → VTF实际文件。VMT是配置，VTF是纹理容器；转换格式不等于完成材质。

### 通道与透明

- 第5集的**绝区零示例**已经由作者更正：源`_M`的**G是Metalness，R是Material ID**。输出给该PBR的MRAO则为**R=Metalness、G=Roughness、B=AO**。源G到目标R不是矛盾，不能把此源通道表泛化给所有游戏/版本。
- 确認原法线编码与DirectX/OpenGL约定再转换，不按贴图颜色猜通道。RNM合并基础/细节法线，使用原材质的蒙版、tiling和强度；示例7×7与4096分辨率不是默认。
- `$nocull 1`通常意味着关闭背面剔除，使单层背面可见；视频07:20把开关讲反。按目标shader用单面样例正反面验证，不对所有材质启用双面。
- 连续透明选项`$translucent`与硬切`$alphatest`处理不同需求；检查叠层排序、深度和阴影。Alpha既可能是透明，也可能被自发光/高光等复用，不能全材质套一份VMT。
- 示例脸Alpha 10%服务于拆分眼睛反光片，不是所有脸都应半透明。

### Neko版本与材质差异

- 录像用NekoShaders2.6.6，但更新字幕指出2.7.3已修复PBR Flex。不要固化“有表情禁止PBR”的旧限制；按实际shader版本测试。
- 该PBR版本的`$emissiontexture`/`$emissiontint`与NekoToon的`$emission`语义不同；参数不跨shader复制。
- NekoToon的`mask1/mask2`、MatCap模式、lightwarp色彩空间、描边与`$darknesslimit`均按该版本模板定义处理，不与MRAO通道混淆。不需要描边时明确关闭，不能把模板默认外观当要求。
- `$nodecal`/高顶点模型问题是版本/分支兼容检查，视频32768数字不足以证明所有输入的统一硬限制；按实际导出后顶点、编译器说明和游戏测试确认。
- 生成VTF时按颜色/数据贴图/法线/透明需求选格式、flags与mipmap；本课未完整展示每类编码设置，不编造统一最佳预设。

原图、处理中间图和最终材质目录分开保存，先检查处理结果，再复制入包根。教程中的Unity步骤只为读取那个VRC材质，不是所有模型的必经过程。

## 4. 身体预览（第5集13:36–15:52）

教程用Crowbar-Starfelll与HLMV++，并提醒原版Crowbar与该查看器的组合存在`View as Replacement`问题；未来按实际组合验证，不声称任意Crowbar/HLMV均有同一故障。

配置正确查看器/游戏搜索路径；打开模型后检查骨架、材质、Flex滑条对应的真实变形、VRD/飘骨和多个动作。启用IK与Ground看脚底和膝踝；修改后重新导出编译。材质可搜索不代表必须覆盖游戏`materials`，使用独立命名空间和明确的测试暂存资源。

## 5. 图标（第6集00:08–01:52）

分别制作大厅、普通头像、倒地图标；倒地图标还需对齐血条背景/血量数字区域。教程在HLMV++中选择双持手枪倒地动作（字幕称`incap elite`）、调视角和纯色背景后截PNG。按动作名称/效果查找，不使用固定序列编号。

本课未给完整像素规格、八名角色VGUI映射或抠图过程。执行时从**当前目标游戏资产或已审核模板**读取路径、文件名、尺寸、Alpha与VMT要求。图标包尚未取得时不得声称已配置完成。最终分别在大厅、普通HUD和倒地HUD观察透明边缘与布局。

## 6. 独立FPS手模（第6集02:00–14:16）

第一人称arms由武器模型动作驱动，不把身体的Proportions Trick直接套到arms。先选目标角色/计划支持的武器与原版手模基准；Bill只是一种参考。

1. 从身体工程另存手模副本，保留手掌、手指、袖子及必要饰品；按原版参考粗对齐、裁切，保留原身体工程。
2. 可用镜像约束辅助对齐，但先验证左右命名、LOCAL轴与反向配置。视频04:48脚本硬编码`Armature`和旧`.select=True`，不能原样运行；4.5使用`select_set(True)`并设置活动对象/模式。
3. 按UpperArm → Forearm → Hand → Fingers → Thumb调整。看虎口、指节和手掌轮廓，不把示例轴或缩放数值硬编码。每根手指均检查，视频省略项不等于无需处理。
4. 确认约束/姿态后在副本应用为保持网格的Rest Pose，合并到目标原版手模骨架并检查权重、父级和变形。
5. 按需要修袖口/补面，检查法线、UV和穿模；缩袖只改对应衣料，不能连手掌一并任意缩放。
6. 导出独立`varm.glb`或项目命名文件，QC里的`innode`对应实际对象名，输出路径对应目标`models/weapons/arms/...`。身体和手模使用各自QC/资源清单。
7. 静态HLMV双臂预览只证明基本加载；之后在真实支持的武器/物品动作里检查持握、换弹、推击、开火、投掷、近战和较大视野下的遮挡。

## 7. 打包与游戏验收（第6集14:32–18:32）

部署目录与封装VPK是两件事。按目标模型、材料、图标路径部署到独立`package/staging`，填写真实作者和资产署名，再用官方VPK或已核实工具封装。八人包需要各目标的模型/图标映射，不能只改外层包名。

教程`distribute_pack.py`没有讲解源码，终端可见删除目录；取得实际脚本后先检查完整删除、移动、覆盖和输出目标。不得在原始Asset/模型目录运行自动清理；不要覆盖已有游戏配置或同名插件包。

只在用户要求安装/测试时部署到游戏，先识别冲突包和松散测试资源。测试辅助地图/相机与最终角色VPK分开；不覆盖`autoexec.cfg`，需要命令时先比较后合并。

验收记录应包括：

- 构建：日志与完整输出文件、内部替换路径、实际编译版本。
- 第三人称：站立、走跑、蹲跳、倒地、受击/救援等所需动作；肩肘、膝踝、脚底、衣物、VRD与飘骨。
- 第一人称：实际测试的武器和物品集合，指节/握枪/换弹/推击/袖子遮挡。不能写“兼容所有武器”。
- 表情与界面：嘴部/眼皮/眼动、多个面部网格同步、大厅/普通/倒地图标。
- 材质：明暗、手电、透明叠层、背面、自发光与不同shader的一致性。
- 包完整性：让最终VPK独立加载，排除游戏里的松散素材替它补漏造成假通过；不夹带原版参考、源码备份或测试相机配置。

TUMTaRA和`sb_takecontrol ellis`是视频测试环境里的例子，不是要求修改正常联机环境。按错误资源来源区分地图/Director与模型错误，不能看到红字就归咎于人物MOD。

## 8. 2024补充：材质分组、法线与比例IK

### 同贴图不等于同材质（P9/P10）

P9 00:49–03:21用双层裙子、单层头花和连续透明区域说明：**先按剔除、透明、shader及通道需求分类，再合并确认相同的材质**。两层反向面可能要保留单面剔除，单层且背面外露的布片可能要双面；不能只因同用一张贴图就合并。Face Orientation用于定位背面，不是自动反转所有红面。名称后缀只能提供线索，按几何、动画极值和材质实际检查。

P9 05:22–05:38删静态bodygroup表情部件只因本例转用形态键；先确认自己的替代表情/附件确实不用。09:00–09:19要求材质名`face`服务于作者假眼追QC引用，不能扩成所有脸的固定命名。

P10 00:22–00:47的VTFEdit Reloaded批转换可作基础转换途径；检查输入后缀、递归范围、输出和自动VMT。源PNG保留，VTF/VMT写独立目录。材质名→VMT→VTF路径建立映射，多个VMT可共用同一VTF。03:51–04:41的`cloth`/`cloth1`正是共用衣服图但分别`$nocull 1/0`的实例。

P10的`VertexLitGeneric`、`lightwarp_anime_skin`、`$phongboost 0.04`、`$phongexponent 5`、固定Fresnel/half-Lambert和`$nodecal`是这套二次元模板外观，不是全部材质共同前提，也不替换已有Neko shader条件分支。精确lightwarp需实际文件与许可，不能从截图重新造同名资源。

- `$alpha 0.3`是P10眼部覆盖片示例的整体透明倍率；纹理Alpha全白只说明源图该通道无透明区域，不代表材质最终必不透明。
- `$alphatest`以阈值保留/丢弃片元，不等于连续半透明；`$allowalphatocoverage`改善覆盖边缘而非替代普通混合。需要连续透明时评估`$translucent`及排序/手电/深度；硬切边缘按实际蒙版调阈值，不固定0.7。P10 04:50–05:19的“是否同时有透明不透明区域”仅是粗略选型提示。
- P10的夜光/RNG只是外链提及，未演示，不登记成已掌握的专项步骤。学习不执行05:54起向游戏根目录复制材料。

参数语义与阈值测试经[Valve shader声明](https://github.com/ValveSoftware/source-sdk-2013/blob/master/src/materialsystem/stdshaders/vertexlitgeneric_dx9.cpp)、[渲染实现](https://github.com/ValveSoftware/source-sdk-2013/blob/master/src/materialsystem/stdshaders/vertexlitgeneric_dx9_helper.cpp)核查；这是SDK2013分支依据，L4D2组合仍需目标环境检查。

### 面部自定义法线（P16）

这是可选风格化处理，不是给带Flex的原脸细分拓扑，也不是烘焙法线贴图：

1. 为要调整的脸部顶点建专用遮罩组；`face`只是示例，与同名材质不同。
2. 临时UV Sphere覆盖头部，调整成适合脸型的光滑球顶/柱状源；细分和平滑施于该源。原脸保留拓扑、UV、权重与形态键。
3. 原脸Data Transfer的Source指向该源，仅启用Face Corner Data→Custom Normals，以遮罩组限制范围。P16 02:48实际为Nearest Corner and Best Matching Face Normal（`NEAREST_POLYNOR`）；其他映射只能作为另行测试的替代，不冒充录像步骤。
4. 看侧脸和不同光照及表情混合，在导出副本应用Data Transfer，**保留Armature修改器**；仅在已烘焙且无引用后去掉临时源。检查导出/重新导入后的自定义法线以及Flex极值。
5. Blender4.1起Auto Smooth改为Smooth by Angle相关资产/操作，4.5不再使用`Mesh.use_auto_smooth`。本机4.5.13内存小样已验证Data Transfer仅法线应用后保留Basis/TestFlex、8顶点及自定义法线；这不是人物实模效果验收。

参考[Blender4.5 Data Transfer](https://docs.blender.org/UATEST/manual/en/4.5/modeling/modifiers/modify/data_transfer.html)、[4.1平滑更新](https://developer.blender.org/docs/release_notes/4.1/modeling/)。P16结尾只可见SMD导出0错误/3警告，没有本P完整编译或游戏测试证据。

### Proportions平移与真实缩放（P14）

**只对匹配的传统Proportions Trick模板**：P14 00:11–01:42整体平移只更新proportions骨架动画，保留原网格与Define Bones；其原生Rest Pose后骨网分开是有意维持原绑定输入，不是作者在演示CATS可互换。执行前核验实际QC如何使用比例修正动画；不套到任意GLB工程，也不误改为所有平移必须重建原网格。

P14 01:52–04:28改变人物真实尺寸是另一分支：若要保持武器骨大小，先对准确武器骨设Inherit Scale=None，再用Pose根骨、世界原点3D Cursor轴心缩放，CATS保持网格固定姿态；同步重导网格/骨架，在VRD工程应用相同倍率后重生成数据并重新Define Bones。None只阻断父骨缩放继承，不阻断整个Armature对象缩放。`Shift+S → Cursor to World Origin`为原生功能，无需新增插件。

### 脚底接触与独立IK末端（P15）

先排除错误T-Pose、尺寸、权重、脚轴与鞋底偏移；按模板已有修正选项处理，别同时叠加不明的偏移。P15高跟鞋例先抬proportions 2单位改善站姿，再复制左右Foot为独立IK末端向下2单位，原Foot继续承载蒙皮，`$ikchain`末端改到实际副本名。`rfoot/lfoot`链名和对应`$ikautoplaylock`引用保持一致；2单位和`.001`均为示例，不是常量。

该流程即使不为新末端显式Define，也仍须核对父级、导出保留与最终骨预算；不要把P15的127说法覆盖项目128保守基线，冲突见纠错资料。它不替代主线USQC已提供的足IK选项，不是任何陷地都要加骨。

至少对比原版/改前/改后的站、蹲、走跑及换枪过渡。作者接受的弯腿/瞬间陷地不直接成为验收豁免；短腿模型可另选匹配动作/骨架，但不能擅自放大或全局禁IK来掩盖问题。

## 9. 2024第一人称手臂细化（序号10；P19）

P19补充原第6节的掌宽、掌弧、多视角手指对齐和独立腕VRD。仍先从身体另存arms副本，不携带身体Proportions修正。按肩部顶点组圈出的范围必须逐面确认；保留足够上臂/袖口，零权重骨先查attachment、IK、程序骨与动画用途。视频“删除225骨”不是可执行删骨配方。

本例身体工程Bill却用Zoey arms作对齐参考，最后输出Bill arms；这不要求其他目标也选Zoey。记录参考模型、输出替换位与实际武器动画契约，不能只看参考文件名。

P19 03:48–04:10的`Inherit Scale=Fix Shear`和取消指根继承旋转是**临时摆姿副本**的技巧；它们改变骨骼继承，不是永久全骨架设置。保留原值、准确选区，按当前局部轴调UpperArm/Forearm/Hand和各手指。Fix Shear不消除所有可能的剪切。[Blender4.5骨骼关系](https://docs.blender.org/manual/id/4.5/animation/armatures/bones/properties/relations.html)

05:44–09:55音乐快放仍展示逐指/虎口和多视角修形；操作顺序可参考，不能从加速过程推导通用角度。09:58–11:20在副本用保持网格的方式固定Rest Pose后，以官方arms为CATS Base合入自定义骨架，检查权重、父级、遗留约束及修改器，再分别处理袖子jiggle与腕部修形。

### 传统手模导出与程序骨

P19 13:59–18:44是完整的传统输入组合：Source Tools **SMD/Z Up**、集合`arm`、动作`idle`，对应`arm.smd`、`anims/idle.smd`、骨骼/材质/jiggle的QCI和`$proceduralbones "survivorarm.vrd"`。名称由实际QC匹配，不是格式保留字；不替换主线GLB/+Y Up和`$NekoDriverBone`的配置。

腕修形先明确左右Hand驱动及辅助骨，准备中性/正/负方向样本，再生成传统VRD。P19 15:57–16:08作者指出左右配反，**18:40最终为L_Hand→handl、R_Hand→handr，trigger帧1/2/3**；18:24的全1是未设置完的中间状态。骨名、±90°/45°、3帧/影响角90°都按模型重新核对。不要从单张中途截图建立程序骨映射。

袖子jiggle参数从手模尺寸/局部轴重新评估，不默认照搬身体。限制摆动要修改最终生成的QC数据，不把任意Blender约束当成游戏会实时运行的约束。P19结尾编译/HLMV只证明录像示例可加载；真实交付仍执行第7节的实际武器、物品、袖口及视野检查。

## 10. 传统QC模块化、定义骨骼与特殊资产（序号13–14）

来源：轻语2024 P22/P23/P17/P18，完整审核见[序号13–16笔记](../../../../learning/notes/13-16-review.md)。保留上文GLB/Neko主线，不把下列SMD模板结构插进USQC。

P22把Flex、bodygroup、材质路径、attachment、hitbox、骨定义、VRD、jiggle、动画和碰撞分为独立QCI供多个替换位共用。按**真实可共用的内容**拆分：`$modelname`是输出替换路径，`$model`的标签、SMD文件名、`$cdmaterials`和运行时动画引用分别核对。带Flex的`head.smd/head.vta`及假眼追`face`引用配套，避免QCI包头/大括号重复。删除LOD、texturegroup、复用附件/物理参数只因该例不用或仍匹配，不能成为默认清理。

P22 05:48–10:53的传统动画换位同时检查IK链、autoplaylock、目标序列顺序和ragdoll位置。该模板在显式/声明序列后、动画库`$includemodel`前放reference及proportions的subtract/delta/autoplay段（08:48）；Francis/Louis的ragdoll位置不能按其他角色抄。缺IK只是闪退候选原因，须依据实际日志和动画依赖定位。

P23 00:08–02:25临时骨定义QC引用proportions与所需`$bonemerge`列表；反编译列表可能漏腿链。插件此时生成的是保留骨名表，不是最终`$definebone`坐标。使用实际参考的必需骨，含IK/附件/程序关系，检查骨表输出后再接入主QC；不将场景所有控制骨一并保留，也不把bonemerge当作Blender权重合并。

### Bill静态尸体

P17从完成模型**另存副本**，摆姿并检查地面/背墙边界；将所需闭眼/混合表情烘焙为基形，再在该静态副本移除其他键、烘焙骨架姿态。按实际复杂度合并或保留网格，核实导出到尸体单骨参考后的刚性位置。视频04:08为`$mostlyopaque`，不是VMT透明开关；它不能生成Alpha或代替材质配置。输出例为`survivors/NamVet/namvet_deathpose.mdl`，按当前目标资产复核盒、绑定、材料与背部接触；保留主线BDP.glb另一分支。

### Francis／Zoey light

P18演示Zoey一转八模板直接套Francis light后的脊柱拉伸。采用匹配T-Pose的Francis参考、对齐核心骨并特别核对脊柱、合骨后重导ref/proportions和骨定义。原生Rest Pose只用于尚未蒙皮的参考骨架，不推翻此前对带Flex角色使用保持网格方式的要求。检查对象名与Armature数据名、Base/To Merge方向；解决`.001`名称冲突不删除不相关Action。新骨轴/父级可能使VRD基准失效，重查样本与中间姿态；jiggle仅在骨名、轴、尺寸和层级未变时复用。此结论限录像传统light模板，不宣称所有扩展流程都必须同法。

## 11. VGUI与工坊发布的补充条件（序号15–16）

P20给出的普通头像/大厅1:1、倒地图标宽高2:1是布局比例，不是完整像素/路径规格。按目标实际模板保持血条与数字区域；检查PNG实际Alpha和VTF转换后边缘，截图中印出的棋盘格不算透明。只换VTF、不新建VMT适用于复用原版同名VGUI材质引用；自定义路径需匹配VMT。保留源PNG，不依赖编辑器自动缩放证明画质。

P21包根是并列的`models`与`materials`，不是包一层`compiled 0.74`；复制身体与FPS全部必要伴随文件，核查编译器自动追加目录，防止`models/models`。根目录`addoninfo.txt`填写真实标题、作者、版本、替换范围和AppID550。包内列表封面`addonimage.jpg`、角色VGUI和工坊外部Preview Image是三件不同资源，不能互相代替。

Crowbar Publish流程：选定目标游戏和本人的新建/更新条目，指定最终VPK与预览，填写说明、实际标签、更新说明及用户选择的可见性，执行授权发布后检查日志和实际条目。更新要对应原条目ID；失败先查看服务器结果与现有条目，不能盲点Publish产生副本。2020课的VTFEdit转JPEG、右键打包扩展和加速器不是强制前提。[Crowbar官方发行记录](https://github.com/ZeqMacaw/Crowbar/releases)

**不要沿用BV1it4y1S7Dg 04:38–05:27的整库清理**：Steam Cloud及`userdata/<id>/550/remote`包含用户数据，05:04作者也用红字提示cfg/喷漆。先按具体错误查网络、账户、条目和工具状态；不得把删云文件当默认上传修复。[Steam Cloud官方说明](https://partner.steamgames.com/doc/features/cloud)

## 12. 可选材质效果：夜光、描边、动态帧与渐变（序号18）

来源/时间与纠错依据见[四课审核笔记](../../../../learning/notes/18-review.md)。这些武器/配件演示只提供材质机制，不把武器绑定/路径带入人物。

- **蒙版夜光**（BV1sfRGYWEGK 02:20–05:14）：在对应VMT加匹配shader的`$selfillum`与`$selfillummask`引用；单色灰蒙版均匀控制发光贡献，局部发光按UV画蒙版。黑白不是模型透明度，灰度90%、512尺寸不固定；已知材料映射的纯材质修改不必反编译/重编模型。自发光不产生照亮周围环境的光源。
- **外壳描边**（BV1SyyWYKE3K 00:40–04:40）：独立副本、专用材质、翻面与法线扩张，导出独立bodygroup；保留相同骨架、蒙皮和必要Flex。检查自交、边缝、面数和远近视角，别全局启用nocull破坏壳的剔除效果。12:40–13:12仅在壳上投影UV，让TextureScroll沿统一纹理方向滚动；不等于屏幕空间等宽描边。最终12:32换UnlitGeneric，不能继续把selfillum/Phong残留参数当生效必要项。
- **多帧纹理**（BV1rC3F6AEGx 10:04–19:39）：确定循环首尾，去掉重复端点；固定投影/遮罩/静态装饰逐帧烘焙为同UV同尺寸图片，按明确数字次序生成多帧VTF。用AnimatedTexture分别指定纹理变量和帧变量，BaseTexture配$frame，其他槽核实际shader。播放周期约N/fps；录像45帧/16fps只是例子。按尺寸×编码×帧数×mips预算与测试，不采用1K120/2K60/4K30为硬阈值。UV边缘膨胀按岛间隔和mip观察，非无条件拉满。
- **双层Alpha渐变**（BV1dS421X7QV 01:36–06:32）：给需要效果的副本区域独立材质，用Sine驱动覆盖层$alpha；保留底层与源工程。真正键名`sineperiod`，不是字幕timeperiod；timeoffset以秒计。min/max超0–1是例外效果，不默认复制-1/1.99；共面几何、透明排序、手电和Flex另测。同SMD或“材质列表靠后”都不保证永远覆盖正确。

PNG可保留RGBA；TGA仅是某些辅助通道工作流的选择。Alpha纹理不必恒为无Alpha的两倍容量，按实际VTF编码和mips核对。无紫黑不证明辅助蒙版路径正确，逐项确认。人物身体/FPS和各替换位按需求分别测试，不以录像未做W模为交付豁免。参数依据：[Valve材质声明](https://raw.githubusercontent.com/ValveSoftware/source-sdk-2013/master/src/materialsystem/stdshaders/vertexlitgeneric_dx9.cpp)、[Sine源码](https://raw.githubusercontent.com/ValveSoftware/source-sdk-2013/master/src/game/client/mathproxy.cpp)、[AnimatedTexture源码](https://raw.githubusercontent.com/ValveSoftware/source-sdk-2013/master/src/game/client/baseanimatedtextureproxy.cpp)。

## 13. 多角色适配和转换（序号19）

来源：TC5B5旧BV1Hi4y1q7GM P23/P24/P25/P27与Starfelll BV1ymT16pEPL，见[审核笔记](../../../../learning/notes/19-review.md)。

传统八人包首先识别**原模型动画基底**，不是原输出替换位。P27 06:38–09:27的Rochelle替换模型实际使用Zoey动画；检查原QC/include与reference/proportions，再选择对应基底→目标序列表。移植时保留有效Flex、VRD、jiggle、attachment、碰撞及额外动画，路径同步；先编一个目标验证，再批编其余。更换人体轴/基准须重查程序骨。FPS可共享已匹配的输入，但八个输出路径及实际持握均需验证。

Light用独立reference，Francis缺匹配参考造成拉长不是不可修复；按第10节重匹配。旧P24直接用T-Pose当Bill尸体只算占位，不能替代尸体姿态交付。替换后的序列/ragdoll位置与比例修正按最终完整模板，不能混抄录像中对照用的旧模板片段。

分包二选一：公用材质依赖包+各角色模型/图标包，或每个角色自含材质。前者声明依赖/版本，后者检查共用路径冲突；不默认同时安装两套。批量Pack的`Parent of child folders`要求每个子目录都是独立完整包根。排除light/尸体时同步资源表与描述。映射表中一代大厅`select_*`与二代`s_panel_lobby_*`不同，普通/倒地使用目标内部角色名；实际表和原帧在笔记中，执行仍核游戏引用。

L4N2.34配套转换短片展示`l4n_magic_converter.exe`、身体/FPS输入、参考目录和目标列表。必须使用与**输入动画基底**匹配的参考八人组；默认Zoey参考不套任意来源。工具随L4N分发与输出是否需要L4N运行是两件事，检查实际转换器、参考、最终材料/资产依赖后再给兼容承诺。未拿到真实BAT不照截图重建并执行；不额外安装运行扩展。

对照原MOD记录继承缺陷与新回归，署名原作者/转换作者并核许可；截图“原模也穿模”不免除披露。VGUI测试要排除替代HUD遮蔽，八个角色分别检查第三/FPS、表情、材质、包依赖和必要特殊资产。

## 14. Max手模与Patch材质补充（序号20）

McQueen最终篇BV1LVzqYTE6F 10:56–12:13为**Skin Wrap转Skin**，不是保留自定义蒙皮的合骨路线。副本先对齐模型/官方参考、烘焙摆姿，再Wrap指向官模、Weight All Points、Convert to Skin，检查后移除本次Wrap与参考。Autodesk说明典型用途为低分辨率控制高分辨率；不要采纳视频相反的高→低必优解释。错权重点查指间邻近、对应、参考质量与设置。[Autodesk Skin Wrap](https://help.autodesk.com/cloudhelp/2026/ENU/3DSMax-Modifiers/files/GUID-1B3C4662-8C42-4F02-BD1B-204CD491166B.htm)

12:13–20:46逐指摆姿检验后去除邻指误权，必要时同一指节环参考合理点，检查皮肤/手套重复缝顶点与归一化；不跨关节复制一圈固定值。thumb辅助骨是否重刷依据真实驱动，不设永久禁改。Ellis参考、保持原手型比例与局部缩放是例子/美术取舍，不保证兼容任意武器；最终官模骨契约与制作中临时摆姿旋转分开。

BV1JDYXexEw5 21:03–24:45用Patch材质引用共用基VMT并替换贴图。核include的VMT后缀/位置与basetexture的纹理路径；只有同shader/通道语义的材料共用基配置。录像18:51关闭mips省空间不适合作为所有人物纹理默认；真实格式为RGBA8888而非ASR的RGB888，按Alpha/法线等需求选择编码。

最终篇21:24–22:41要求Test_Hand通过后把Body、custom_model、cdmaterials同步回生产V_arms，身体亦用实际生成输入，不能留示例路径。release脚本只在匹配目录布局中工作，拿到本体先审阅复制/删除/覆盖。30:17–30:36清空hl2/materials的意图是排除松散文件替包补漏，但只能隔离本任务已知测试资源，不能删除整个共享materials。中文图标输入名与动态VGUI选项是脚本约定，非游戏固定路径/已掌握动态VGUI。详见[序号20审核](../../../../learning/notes/20-review.md)。

## 15. 感染者的编译、特殊资产和验收（序号21）

仅用于明确选择的感染者工程，来源为[2021四P审核](../../../../learning/notes/21-review.md)。不同普通感染者/男女/地图版本、Tank、Witch/新娘及一代特感等应从实际原版资产列清单。每项核modelname、材质、动画序列/ragdoll位置、proportions/reference和完整伴随文件；不是只改文件名就保证兼容。P1 33:15–35:07提醒编译折叠可能丢手指，也出现hitbox引用未定义骨：修保留骨表与引用，不默认删盒。低清长QC不可辨读处等待真实模板，不拼万能代码。

普通感染者/Witch的示例用VertexLitGeneric并以`$allowdiffusemodulation "0"`处理随机染色（P1 52:37–54:17、P3原帧50:48），作为需在目标游戏核实的材质候选，不能把整套环境遮蔽/风格参数一起强套。P1 56–58分的translucent造成幽灵外观后撤回，未解决的连续半透不能当已验证方案。Tank示例普通材质的成功不保证所有透明/着色通道。多帧眼口按前述AnimatedTexture测试，不能声称由游戏角色表情驱动。

附件按模型类型检查：fallen survivor的物品、防暴警棍，Smoker身体舌头/长舌效果/缠绕独立模型三部分，Spitter口水`$attachment "mouth"`（P4 09:12红字补充）及Witch眼部特效。缺骨、缺attachment或位置未随新体型调整可能让效果从原点/错误位置发出；是否改坐标由实际接触点决定，不照抄腰/嘴位置。

Boomer爆炸大尸块与小碎片是独立资产范围。可保留原版并注明；不采用P4 14:16–14:38的零缩放退化网格作为通用隐藏法。修改时用正确替代/目标支持的隐藏机制。Tank倒卧参考与`$collisionjoints`要符合真实物理基准，不随意转90度或删除碰撞遮盖错误；LOD、Flex、jiggle、hitbox仅在确定不需要且无依赖时移除。

验收逐项覆盖目标变体、跑动/攻击/特殊技能、舌头或口水等效果起点、骑乘接触、燃烧和死亡/尸块；实际请求涉及可玩感染者时另验FPS。录像没制作/没显示的内容不标通过，作者接受的膝部穿模、眼特效错位和僵硬尸体也不自动成为交付标准。

## 16. McQueen2023旧模板与手模撤回意见（BV1ug4y1j7Lj）

本节P1–P10仅指[2023十集](https://www.bilibili.com/video/BV1ug4y1j7Lj/)，[完整审核](../../../../learning/notes/2023-mcqueen-review.md)有高清原帧。仅选此传统Max/SMD路线时使用；P10后续意见优先于同例P8早期偏好，但不覆盖其他已验证的GLB/CATS手模方案。

### QC、参考与材质

P4 18:12–20:00的Wunderboy SMD Exporter v1.7分Reference SMD（网格）和Sequence SMD（骨动画）；两类不因扩展名相同而互换。该ui人物模板按真实动画来源生成参考：高清P4 25:36说明要求对齐后的官方骨架输入`tz.smd`，对应人物BAT/Perl生成`ref`，再放回SMD目录。`tz`是脚本文件名，不是Source保留字，也不是修复所有Flex失效的口令。Definitions、proportions、ref与网格各自按实际QC引用同步；未取得BAT/PL与模板时只记录流程，不重造并运行猜测脚本。

P4 15:32–15:58是Zoey动画→Ellis输出，不是二次元一律用Zoey。按输入基准、目标替换位和实际动作库区分；教程目录包含light/Bill尸体文件不等于本套完成它们的制作/验收。定义骨阶段曾出现错误游戏选择，执行时核工具实际指向L4D2及项目构建输出，不照中间画面配置。

P4 08:00把自动生成的LightmappedGeneric换VertexLitGeneric；11:24的`toon_light`供`$lightwarptexture`使用，改变光照明暗映射，不生成描边几何。Phong/Fresnel等按目标风格和贴图通道配置，不全材质照抄。4096是该转换器防缩小设置示例，不要求放大每张纹理；未用法线可省对应引用，有源法线/蒙版则保留并验证。P5 00:27–01:15向hl2放松散材质只说明该查看器搜索路径，不能随意往游戏根放文件或让它替VPK补缺失。

### 两种手模方法必须连同P10看

P8从**原始模型的另存副本**开始，按官方`v_arms_mechanic_new`参考对齐；不是直接套身体proportions。裁切检查实际FOV、袖口和上臂截面，不固定“越短越好”。

| 方法 | 本片操作与来源 | 审核后的用途 |
|---|---|---|
| Skin Wrap→Skin | P8 17:12–22:13；自定义网格固定摆姿、Wrap控制对象选官模、Weight All Points、Convert to Skin、查邻指误权 | 适合在官模骨架上重建权重；输出Skin后去掉仅本次Wrap/参考。需要逐指修权，不是免修工具 |
| 原Skin封套＋父级嫁接 | P8 22:13–28:40逐骨挂官模并恢复封套，29:10–36:24刷权；26:39漏存封套后返工 | 保留此旧例知识，**不再因P8称更好就默认选用**；需要核该模板的保留/折叠骨与武器动画契约 |

P10 **07:11–08:24、12:26–13:33**指出直接嫁接在某些武器中出现拉扯，而HLMV预览看不出来，改推荐Skin Wrap后修权。早期“第一/第二”口述有混乱，以具体操作名和最终复述记录；不推断所有保留原权重的现代合骨路线都失败，也不把Wrap说成兼容所有武器。

Skin Wrap从已蒙皮控制网格计算目标新权重，Convert to Skin要求控制对象已有Skin；保持对象/单位/基准正确，检查指间串权与未赋权点。[Autodesk说明](https://help.autodesk.com/cloudhelp/2026/ENU/3DSMax-Modifiers/files/GUID-1B3C4662-8C42-4F02-BD1B-204CD491166B.htm) P8 19:48赋1仅用于已确认刚性指段，虎口/指关节需要渐变，不能按“某指力气大”决定蒙皮。

P8 36:28–42:24分别导arms网格和参考sequence；`survivor_Arms_Bonemerge.qci`中放jiggle是作者组织习惯，不是格式要求，也不豁免手模骨预算。袖子参数按实际链、尺寸、局部轴与持握调整。至少覆盖多类原版武器、用户声明的自定义武器、投掷/医疗/近战、推击与换弹；记录通过的集合。P9有限游戏观察未能提前发现P10的问题，不能拿一次演示替全套验收。

### VGUI、元信息和发布

P9 01:51–02:13展示的三类HUD命名与现有映射资料一致；大厅/普通/倒地分别按目标内部名，512×512只作该头像例值，不当所有VGUI硬限。18:45–19:14替换倒地轮廓后重做Alpha，保留血条布局，去绿边；Alpha边缘可灰阶，不要求硬二值。20:36取消自动VMT仅用于复用原版材质引用，21:04作者自己选择保留源图备份。

addonimage继续用已核的JPEG方案，和角色VGUI、工坊Preview分开；P9“任意格式”不作为保证。addoninfo按真实内容写作者/替换位/版本/类型，清理本次拷入的重复或无关条目，不复制Sound=1或示例nick等中间状态。修改描述中的Ellis不改变模型内部替换路径。

P9 29:36–30:48只演示Publish草稿字段，必填内容未完整、Publish灰色，没有新条目上传成功证据。Save as Template是保存发布预设，不是上传。实际发布仍需用户指令、合法素材和最终包，按用户选择可见性并核服务器结果；学习不发布、不关注/投币/收藏。

## 17. HLMV++联动预览与PBR开发资源（2026-09-09）

来源：[HLMV++手模V模预览](https://www.bilibili.com/video/BV1am421H7Dw/)与[Blender PBR流程](https://www.bilibili.com/video/BV1kaxCz6Egb/)，均Starfelll；[逐段审核](../../../../learning/notes/2026-09-09-face-review.md)。这是预览/材质迭代知识，AWP示例的枪械绑定与路径不迁入人物模板。

### 武器V模与arms组合

1. 核查看器/游戏搜索路径、当前构建版本。以目标武器V模型为主模型，在**Submodels**页通过Add Submodel或录像00:16/02:08的**Add (Steam)**载入相应arms；先用官模基准对比，再换自己的arms。不要把自定义arms静态打开就当正在播放武器动画。
2. **Sequence**中选择该武器真实存在的idle/deploy/reload等动作，核叠加层、播放速度、帧、姿态参数和FOV；02:16原帧可见多个layer。看虎口/指节/腕部、袖口、穿插和视野遮挡。修改后重编并确认实际重载了新文件，不能只凭编译成功文字。
3. 身体主模型挂W武器是另一类预览，01:12–01:36为示例；Force attach等挂接设置不能掩盖错误骨架/attachment。02:48紫色材料不是已通过。记录测试武器/序列，不宣称所有武器兼容，仍在实际游戏验证动画事件、持握和运行环境。

这补上旧课仅展示静态arms的空白，不推翻McQueen2023 P10“部分武器回归”的警示。本批只看了操作证据，没有安装或运行HLMV++实测人物。

### 材质迭代与最终包依赖

先固定逐材料映射：Blender源图/烘焙通道→转换后的VTF→VMT引用→引擎实际加载路径。纯纹理/参数调整通常走保存/烘焙、转图、材质重载；网格/骨架/QC变化另导出编译。PBR片03:28旧紫→03:44新红说明保存与引擎刷新不同；06:56附近`RESULT: SUCCESS`与`HLMV not found`可同时出现，自动预览未成功不抹成全部通过。

05:44原帧的shader是**PBR**，使用颜色、MRAO、发光图与`dev/flat_normal`占位。这是扩展材质链，不是Blender节点原样进入原版L4D2；确定NekoShaders/Left4Neko等实际依赖和版本，纯原版另选已验证shader。数据通道、Alpha、法线方向、压缩与mips分别确认，不照BAT把所有纹理DXT1/全部无mips；`@REM`/注释中的invert-green、watch等不算已经启用。

[MareTF作者说明](https://github.com/craftablescience/MareTF)支持create/edit/info与watch，格式版本仍按目标引擎，不能因支持7.6就给L4D2使用新版专属编码。Source Engine Support、VSCode VDF、Batch Runner及F5绑定是开发配置；先复用已有功能，不作为玩家依赖或强装插件条件。

[Nekook作者说明](https://steamcommunity.com/sharedfiles/filedetails/?id=3262974277)明确挂载内容优先于VPK。记录开发挂载根和资源来源；最终包须在不由该开发目录补漏的环境单独验。Nekook开发启动不自动变成最终玩家依赖，真正的运行shader/控制器依赖则不能省略。

打包按实际依赖递归核VMT/Patch include、虹膜/cornea/ambient/envmap、颜色/MRAO/发光/法线和模型伴随文件；内置引擎资源确认目标存在，自定义资源放任务命名空间。视频06:56–07:28白名单/variants筛选与输出只证明它运行了打包，未取得完整脚本，不能照截图运行或认为后缀白名单等于依赖扫描。源PNG/PSD/GLB、BAT/Python、编辑器配置和测试启动器保留在开发目录，不因和VMT同文件夹就全塞入VPK。眼部专项排查见[面部眼动诊断](face-eye-diagnostics.md)。

## 18. 纹理重烘焙、VTF编码与mipmap

来源：[路线图A4/B6–8逐条审核](../../../../learning/notes/2026-09-09-abc-review.md)。B5只取得充电试看，**以下mipmap原理的补充来源为官方资料，不是B5已学内容**。原版/扩展分支继续沿第3节，题材为AI角色或枪械不改变人物范围。

### 重展UV后的基础色迁移

Blendergo4.5.11演示：保留有正确UV/材质的源，重构/重拓扑副本作目标，两者实际表面重合；目标新展UV、排岛并检查Overlap/交叉/接缝，给目标各实际使用材质设置活动的新图像节点。不能只在UV编辑器选图、把原图误作烘焙写入目标，或用黄边颜色代替确认活动对象。

先选源，最后确保低模为活动目标，使用Cycles→Diffuse仅Color，关闭Direct/Indirect，开启Selected to Active。此流程用来迁移基础色，源上临时断开其他通道的做法只在烘焙副本操作；复杂/金属shader先隔离目标通道，不破坏主材质。GPU是例中设备，非基础色烘焙必要条件。

挤出与射线距离决定投射范围，不实际给最终网格增加体积；根据表面距离、薄层、衣物/指缝调整，不能把1%模型高度、0.01/0.05或“黑斑就加大”当公式。先查UV、法线、选错目标、漏射/射到邻层，再改距离；必要时独立cage须匹配低模拓扑。UV岛距和烘焙margin共同按最终分辨率/mips检查，片内16px只是例值。[Blender4.5烘焙](https://docs.blender.org/manual/sv/4.5/render/cycles/baking.html)

基础色完成后保存新图像、重新加载复查。法线、粗糙度、金属、AO、Alpha等按独立通道语义处理，不把颜色图烘焙当全套PBR/蒙皮/Flex恢复；法线另核切线空间、通道方向与数据色彩空间。片尾仍有袖口错色/接缝，源缺陷会被继承，不把“80%视觉完成”当剩余通道可删的依据。

### 编码、mips与flags分开决定

VTF是纹理容器，格式、尺寸、帧/面/mip数和flags共同决定结果；VMT定义如何使用它。几何LOD与mipmap不同：前者换网格，后者提供不同纹理分辨率。人物表面通常需要缩小采样时的mips，不能沿旧课全关以省空间；固定屏幕UI/数据查找纹理按真实采样用途另定。

完整二维方形逐级减半mip链的像素总量约为顶层的4/3（约多33%，由1＋1/4＋1/16…计算）；这不是“开mips更省存储”。压缩纹理每级按4×4块向上取整，另加VTF头/缩略图/多帧等，不能把PNG文件大小当显存占用。[微软mip缩小采样说明](https://learn.microsoft.com/en-us/windows/win32/opengl/gltexparameterf)只补通用原理，不把OpenGL接口带入Source材质配置。

| 需求 | 候选编码与检查 |
|---|---|
| 不透明基础色，允许有损 | DXT1/BC1候选，4×4块8字节；检查渐变/文字/边缘，不能当无损 |
| 连续Alpha或辅助灰度数据 | DXT5/BC3候选，4×4块16字节；按实际shader与通道精度核对。BC1的一位Alpha不等于连续灰阶 |
| 对块压缩伪影敏感 | RGB888/RGBA8888等目标支持的未压缩格式，按是否需Alpha选择；容量与质量权衡，非全贴图默认 |
| 法线 | 保持方向、分量与shader解码匹配；普通RGB法线、DXT5nm和ATI2N不可互相改后缀冒充 |

[微软块压缩说明](https://learn.microsoft.com/en-us/windows/win32/direct3d10/d3d10-graphics-programming-guide-resources-block-compression)支持块容量/小mip填充与有损特性，[GPU块压缩和PNG区别](https://learn.microsoft.com/en-us/windows/apps/develop/win2d/bitmap-block-compression)支持存储区分；这些不是L4D2所有格式支持表。Mips减少缩小采样伪影仍须引擎实际观察，不保证FPS。颜色/数据的sRGB、Normal Map、No Mipmap/No LOD等标志按目标引擎与图用途核；枚举存在不等于都应该勾选。

### VTFEdit与SP2VTF的同名标签不能互抄

御琪幽然2017 P4演示VTFEdit1.3.3：File→Export导出可编辑图、View→Mask查看透明效果，编辑后File→Import→Save As，再Tools→Create VMT。PNG支持无损RGBA；TGA可方便保存单独Alpha，但编辑器未显示“Alpha1”不能证明PNG有损/无透明。Alpha数据也不必作为透明使用，保持源数据和shader语义。

高清13:20的**Normal Format=DXT1**是常规/无Alpha图像的格式项，**不是法线贴图质量设置**；右侧Generate Normal Map是另一个操作。检查Alpha Format、实际输出格式、Resize/Clamp和mip数，不能把作者“不懂就全默认”作为新项目规则；自动VMT仍核真实shader与相对路径。

SP2VTF录像为作者“一个橘色的橙子”的测试版，由小小少女不饮酒推荐：三个路径是VTFCmd.exe、源图目录、VMT目录；载入列表→逐行确认输入→设置尺寸/编码→转换后重开VTF。与原生VTFEdit不同，03:28 UI的**Color旁注basetexture，Alpha旁注bumpmap**，因此Alpha栏不是自动替带透明底色选择DXT5的保障。本例实转19个base、0个bump，法线只口述可用。

执行前需检查准确发行版和VTFCmd及其DLL，使用独立源副本/输出暂存目录；程序可能在源旁生成/清理同名VTF，并覆盖目标。片中v1.0.7下载页、带1.0.8的README和三路径运行UI分开记；当前main已为Tauri版，不能用旧搜索缓存PySide6介绍替代真实版本。

所查当前核心[scan.py](https://github.com/ora233-fantaea/SP2VTF/blob/281a5eb601cffed4d0cb9eaab9855b5b47f27a80/sp2vtf-tauri/src-tauri/resources/python-embed/site-packages/sp2vtf_core/scan.py)允许前缀/后缀模糊匹配，[convert.py](https://github.com/ora233-fantaea/SP2VTF/blob/281a5eb601cffed4d0cb9eaab9855b5b47f27a80/sp2vtf-tauri/src-tauri/resources/python-embed/site-packages/sp2vtf_core/convert.py)把base/normal的格式分别取Color/Alpha，且输出按VMT同目录＋纹理引用stem组成。故需核实际目的地、同名冲突与每行通道，不能据勾选或README认为已经完整解析跨目录/Patch/proxy依赖。此处是静态补证，不代表录像二进制同实现或整套程序已验证。

`_Normal_OpenGL`文件名不自动翻G；所查转换函数没有这一变换。`_Roughness`命名与Phong指数也不构成物理等价转换。先明确输入来源和目标shader，再转方向/通道。多套渐变、AnimatedTexture多帧及特殊材料按实际能力另处理，不让此工具成为完整人物材质的强制入口；Steam++不是转换技术依赖。

### L4N1.6.5：ATI2N与DXT5nm条件分支

Starfelll短片展示PBR shader在RGB888、普通DXT5、DXT5nm及ATI2N之间切换。仅作为允许相应运行扩展的法线候选：

- 录像给ATI2N的MareTF命令为`maretf create Normal.png --version 7.4 --format ATI2N`。本例输入为DirectX法线；OpenGL输入先核是否需要翻G，不能重复反转。
- DXT5nm使用原法线R→A、R/B置黑、保留G后转DXT5，配该shader的`$dxt5nm 1`；A承担法线X，不再可兼任另一蒙版。不是任何DXT5法线加一行就正确。
- 普通图、ATI2N和DXT5nm只留对应有效`$bumpmap`/解码设置，别复制录像切换中的重复行。21.3MB/64MB是该样例，质量比较不保证所有纹理同样排序；底色色带还需另查。

[MareTF作者](https://github.com/craftablescience/MareTF)支持格式/版本、`--invert-green`与`--no-mips`等，但**可写VTF不等于原版L4D2可读**。VTF7.6/Strata等新分支不自动迁入此工程。本片未完成纯原版兼容、全部flags或不同人物材质实测；未允许扩展时不默认升级为该方案。

## 19. 原生表面转权的FPS手模实录分支

来源：[鱼不吃茄子BV12pT56uEE8](https://www.bilibili.com/video/BV12pT56uEE8/)，[高清审核](../../../../learning/notes/2026-09-09-abc-review.md)。Blender4.5.11/CATS4.5.3.2、`v_arms_mechanic_new`官模参考；与第6节保留蒙皮合骨、第16节Max Skin Wrap是不同的具体转权操作，不能互换名称。

本例输入已有可摆姿的自定义arms蒙皮。先在副本用Pose调整掌宽、指节、指尖、虎口、拇指和腕，再以雕刻细调**表面对应**，不是只让骨头看起来重合。官模与目标同处、同基准，必要时区分左右/指部转权选区以减少邻指误投；用户造型与完全贴合官模之间按变形质量取舍，不能擅改手型。保留转权前阶段。

25:00使用Weight Paint→Weights→**Transfer Weights**，活动目标为自定义body。25:03–25:06高清补帧显示映射“最近的面顶点”，创建数据/物体变换、按名称/全部层、替换1.000；**不是最近面插值的录像证据**。按当前UI核源/目标层和覆盖范围，确认全部所需变形组真正传入；最近面插值可作为其他输入的待验证替代，不冒充本片按钮。[Blender转权说明](https://docs.blender.org/manual/sv/4.5/sculpt_paint/weight_paint/editing.html)

随后按合骨流程使目标由正确官模骨架驱动，逐项查Armature、同名组、父级、helper/末端骨。纹理/蒙版等非变形组不随“全部层”盲覆盖；不要把传递权重与CATS合骨合并成一个无需检查的步骤。

26:48–42:12逐腕/掌/指查权，结合顶点选区与锁组局部平滑；错误指组先清再平滑正确渐变，模糊不能修正错误投射或自动恢复无权重点。改权后对比屈伸、张合、腕扭转和相邻指，Limit Total/归一化后再测，不只看彩虹图。

42分后的SMD/QC输出继续按其传统契约；已有GLB主线只采对齐/转权/修形思路，不换成旧SMD模板。录像47分为Nekook开发挂载、Hand Tester和有限持枪测试，不能证明独立VPK、全武器或本机验收通过；最终仍按第7节记录真实支持的动作集合与包依赖。

## 20. 碰撞网格与关节布娃娃：先分资产和模拟端

来源：路线图13的汽车碰撞、14的Max/Gmod两P、15实际P11的Blender/Gmod模板，[时间点与版本审核](../../../../learning/notes/2026-09-09-def-review.md)。这批补物理概念和条件分支，不替换已有幸存者GLB/QC主线或Bill尸体资产流程。

| 要解决的问题 | 检查对象 | 不可替代它的东西 |
|---|---|---|
| 单个静态/刚性道具的接触外形 | 碰撞代理网格、`$collisionmodel`、输出PHY及实体类型 | 可见网格面数、人物ragdoll关节表 |
| 人物倒地后关节式物理 | 分骨刚体、`$collisionjoints`、PHY骨映射/父级/约束 | hitbox、render bounds、只给整体做Convex Hull |
| 受击区域 | 目标模型hitbox与游戏逻辑 | 碰撞凸件或viewport包围盒 |
| 尸体在各客户端不同/扭曲 | 真实实体生成与模拟端、服务器/客户端model＋PHY对应 | 只按地图里出现或“死亡mod”名称判断 |

普通碰撞体制作可从独立低细节副本开始，按接触轮廓分成若干闭合凸壳；13号用Propper粗块或Blender分区Convex Hull，车顶/车体/轮子分别处理。渲染与physics须同轴、同单位、同导出原点；物体显示对齐后仍核节点变换。平滑着色不能修复开口/退化网格，删细节/材质仅限碰撞副本，不删角色渲染数据。`$concave`允许组合多个凸件，不是任意凹壳都可用；19个凸件和mass1500是汽车示例，不能套人体，更不向人物加`$staticprop`。[VDC物理QC附录，索引可读](https://developer.valvesoftware.com/wiki/Physics_Entities_on_Server_%26_Client?uselang=ru)

新增人物刚体时，匹配该骨真正驱动的可见区域；14号脚趾由原foot碰撞块拆分，原脚块相应缩短，避免相邻刚体深度互穿引发抖动。各块保持正确骨名/刚性绑定/父级，先静置检查，再用HLMV Physics Test按关节局部轴调限制、Generate QC后回读真实内容。最终需游戏落地、关节极值、附件、外力和穿模测试；预览里能拖动不算全部通过。

15号的Append PHY是从教师`.blend`取**已有权重的碰撞集合**，不是直接导入引擎二进制`.phy`。模板摆姿、静置与合骨必须同步；新建网格仍要明确绑定。模板中的qz/VRD与ragdoll.qci条件单独核对，不把删qz块或mass40/inertia10等示例值当默认。

物理参数分开理解：mass是总质量设置，jointmassbias偏置体积分配的质量，不是计算优先级；inertia是转动惯量缩放，damping与rotdamping分别约束线性/角运动。根骨须与物理父级/约束匹配。`$jointcollide`存在指定配对后限制碰撞集合的语义，不能只当“追加一对”；与noselfcollisions/默认配对及实际引擎分支一起验证。14号作者称配对Gmod有效、L4D无效仅是其案例记录，不写全版本断言。

**分别查三种预算**：导出/编译骨表、PHY刚体数、凸分解件数。14号“再加16/8”是已有基础人体的余量说法；[Valve SDK2013头文件](https://raw.githubusercontent.com/ValveSoftware/source-sdk-2013/master/src/game/shared/ragdoll_shared.h)的24由[运行代码](https://raw.githubusercontent.com/ValveSoftware/source-sdk-2013/master/src/game/shared/ragdoll_shared.cpp)按solidCount检查，仅证明公开分支，不当L4D2/Gmod通用上限。15号07:39导出206骨/MDL128警告不能照口述忽略；编译可能折叠，但须核日志、最终骨表和真实引用，不能据SMD节点数自动删用户骨。

掉落附件是特殊物理分支：活体眼镜可跟Head骨，掉落物理节点才可能单独根化；不能断开角色Head。空jiggle块只是14号保留骨的技巧，不是飘动配置或跨编译器保证。作者给L4D删rootbone且仅一个独立刚体的限制只作待验证配方，不改普通人物模板；先查源PHY和反编译问题，禁止用删根掩盖约束错误。

client ragdoll主要在各客户端独立模拟，server ragdoll由服务端模拟/同步；不意味着前者别人看不到、后者天然更精确。Gmod keep corpses/物理枪只是具体演示，[Facepunch客户端接口](https://wiki.facepunch.com/gmod/Entity:BecomeRagdollOnClient)的限制不直接迁入L4D2。地图尸体、玩家死亡、静态Bill资产各自识别；跨端PHY/骨映射不一致先修一致性，不清共享资源。本批未核八角色全部物理规格，也未做本机人物布娃娃验收。

## 21. 反编译参考/动画/QC：先诊断基线，再选择修复

来源：路线图16—19，[逐条审核](../../../../learning/notes/2026-09-09-def-review.md)。17/18及DeltaRepair主要是武器例，只迁Source通用诊断，不复制枪骨、枪手IK、lookpose或删除指令到人物QC。

1. 保留原MDL及真实存在的VVD/VTX/PHY/ANI和反编译输出。记录Crowbar版本、目标gameinfo、studiomdl与查看器路径；Crowbar前端不等于编译器。Preview/View可分别比对，不是HLMV++子模型联动。不要因“材质放根目录”污染游戏共享搜索路径。
2. 对照原模型可见动作、导入reference与逐Action结果，区分参考坐标错、绑定基准错、加算动作孤立查看、QC重建错、数据真正缺失。**delta是加算语义，不是损坏标志**；[Valve studio.h](https://raw.githubusercontent.com/ValveSoftware/source-sdk-2013/master/src/public/studio.h)对此有明确标记。绝对动作、加算层和subtract中性帧必须匹配，不能只靠文件名猜。
3. 若有同源健康姿态，可在副本恢复网格与骨架基线；17号用了idle，18号idle仍坏而改找其他健康动作，所以idle/run并不保证完好。只解除本次Action关联并保存原动作，不全清动画。网格烘焙、Rest Pose、重建Armature顺序一致；带形态键/约束的人物继续用工作流安全分支，不盲Apply唯一Armature。
4. 逐项审QC与修复后SMD的对应。保留所需definebone、bonemerge、attachment、活动/事件、fps、混合层、poseparameter、IK、序列顺序与proportions。18号按layer是否完整调整delta、用usesource重建枪手touch、重建三帧lookpose只是其输入策略，不是全删`0_`/IK/骨定义规则。
5. 输出新目录，编译至项目build，对照原始/修复的中性帧、首尾/事件帧、混合、持握、附件、Flex/VRD与真实游戏动作，再报告具体通过范围。一个Blender姿态或短持枪演示不能证明数据全恢复、人物兼容或多人一致。

[Crowbar0.74作者记录](https://github.com/ZeqMacaw/Crowbar/releases)修复过PHY含animatedfriction时漏读editparams、出现无父骨旋转约束的反编译问题。遇此症状先核版本、PHY配套与日志，不能一见Pelvis无父级错误就删rootbone/约束；本机0.68没有因此升级，也不保证升级能解决全部动画问题。

DeltaRepair是**可选第三方候选工具**：19号P1实际1.3.3，P2实际1.4.1；当前简介为代发，界面署名shu、codex，不等于本任务/官方产品作者。其输入为原MDL、动画目录、参考SMD/time、delta/corrective配对，P2另有逐骨偏移与QC重建。允许手动选中性参考，不固定idle_raw或time0；90度偏移仅是该枪示例。P2 03:44语法为`delta`及`subtract "a_idle_1" 0`，不是ASR拼出的“deltasub”。

本批未取得/运行exe或源码，因此算法、全部格式与骨架兼容、覆盖行为未确认。将来确需使用时先审实际包来源/版本/输出目的地，用新目录保留原件；生成成功仍执行上述对照。不得声称可恢复所有丢失数据、修所有delta或省略IK/游戏检查，也不以工具下载困难阻塞已有诊断。

## 22. RNG与组件控制：先确定随机对象和运行契约

来源：路线图20的L4D2武器材质课与21的82秒效果演示，[音画/高清审核](../../../../learning/notes/2026-09-09-def-review.md)。均是用户选用的表现分支，不自动加入人物基础制作。

20号实际将三张同尺寸图导成多帧VTF，再在VertexLitGeneric里以EntityRandom、scale2.99写`$frame`。有效帧索引从0开始，片内5.99示例对应六帧而非五帧；scale是随机值缩放，N−0.01为旧例的避上界惯例，不是帧数声明或严格等概率证明。先核每张尺寸、顺序、Alpha、实际编码/mips及导入后的全部帧；把1024图放大到2048修了该例尺寸冲突，不增加细节，也不要求一律2K。

多帧VTF只是容器：VTFEdit播放预览、AnimatedTexture连续驱动、EntityRandom选帧与运行时skin/bodygroup是不同机制。保留用户原shader、光照/透明通道和其他Proxies，避免多个代理争写`$frame`；无需像录像演示那样删除旧VMT后重建。

| 需求/机制 | 已核语义 | 必须另验 |
|---|---|---|
| EntityRandom选帧 | 本片实际使用；旧作者实验解释为实体关联取值，不是逐关循环计数 | 身体/light/尸体/FPS实体是否相同、何时重建、各客户端与V/W一致性 |
| UniformNoise | 公开代码在每次OnBind取随机值；直接驱动帧可能持续变化 | 若要保持需明确锁存/更新条件；不是天然每实体或每地图一次 |
| 条件锁存结果 | LessOrEqual等选择保留/更新某材质变量；保存结果不代表上游停止随机调用 | 材质状态共享、重新载入/换图、初始化哨兵及贴图槽同步 |
| 几何组件/材质皮肤切换 | bodygroup几何、skin/texturegroup材质选择、Alpha隐藏不是同一层 | 实际QC、控制脚本/扩展、输入绑定、多人状态与最终包依赖 |

依据为[原社区RNG指南](https://steamcommunity.com/sharedfiles/filedetails/?id=668958242)及[Valve mathproxy实现](https://raw.githubusercontent.com/ValveSoftware/source-sdk-2013/master/src/game/client/mathproxy.cpp)。前者在2022录像里已标**Obsolete**，不是Valve官方文档；EntityRandom解释为该作者实验来源，未声称已读L4D2对应实现。后者只核UniformNoise/条件算子，不证明闭源游戏全部proxy行为。替代SYS指南正文本次未取得，不把旧长代码包装成2026现行方案。

四关黄/蓝/粉/蓝只能说明录像样例的三帧可见，不能承诺每换地图必换、不连续重复或联机同步。人物应用时先写清“谁随机、何时更新、哪些材料共用结果、谁必须一致”，再在目标运行分支验证；RNG不等于按按钮换装。

21号仅展示游戏内组件勾选与显隐，未展示QC、导出、控制代码、安装或准确依赖版本。登记为**效果审核完成；制作方法、运行依赖和多人一致性未覆盖**。不凭作者其他视频推断必用某版L4N，不把菜单外观当bodygroup实现证据，紫黑中间状态也不算材质验收。需要实作时先取得与作品匹配的组件/QC和控制说明，再选择原版支持或经用户明确允许的扩展方案。
