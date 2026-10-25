# 表情与眼动：按路线、症状定位

用于幸存者脸部表情失效、眼球错位/重复/缺图与原版候选眼动选择。来自2026-09-09指定六课中的前四课及作者简介，详细时间、补档身份和清晰度见[审核笔记](../../../../learning/notes/2026-09-09-face-review.md)。这是审核后的诊断方法，不是可直接粘贴的万能QC。面部形状制作看[工作流第15节](character-workflow.md#15-面部骨骼补制表情与旧xps流程2026-09-09)。

## 先区分要交付的眼动

| 路线 | 要核对的完整链 | 能力边界 |
|---|---|---|
| 传统眼球投影，原版兼容候选 | 左右接收几何/材料 → QC eyeball中心、骨轴与尺寸 → Eyes/EyeRefract及纹理 → 控制器/规则；eyelid需要时另配 | 本批有L4D2录像结果，尚无本机纯原版验收；不能把查看器跟随摄像机当所有游戏注视行为 |
| 使用eyelid驱动眼皮、不做可见虹膜投影的旧模板 | eyelid中引用的eyeball标签与该模板Flex数据保留 | 假眼球可能仅满足本模板眼睑引用，不等于动态虹膜已完成；普通直接Flex眨眼不必强加这套结构 |
| Left4Neko形态键双轴眼动 | 本工程AU61–64等目标形状、L4N控制器分解规则及运行环境 | 保留2026 GLB主线；不要未经同意添加运行依赖，也不把传统投影模板覆盖这些键 |
| 静态虹膜/暂不做眼动 | 正确中性外观、眨眼/嘴形、明确缺少动态眼动 | 是否接受由作品要求决定，缺一个功能不自动重做整个角色 |

NekoMDL是编译器，Left4Neko/NekoShaders是运行扩展，二者不是同一依赖。[作者发布记录](https://steamcommunity.com/sharedfiles/filedetails/?id=3142607978)已有`$NekoModel`支持eyeball/eyelid的条目，因此传统候选不等于“必须Max/SMD”；迁入GLB仍需核实际2.3.0的命名、坐标、NewCommands.qci与运行结果。当前作者[USQC flexrules](https://raw.githubusercontent.com/Starfelll/L4D2_Utils/master/ultimate_survivor_qc/Compiling%20Files/QCIs/survivors_flexrules.qci)把blink直接映射frame01，眼球示例为注释；不能把这个远端版本当成本项目2026改编v3.8已安装。

## 原版候选的四层检查

1. **几何与绑定**：接收面在张眼/闭眼、仰俯/侧视中覆盖眼眶且不穿眼皮；左右有独立材料分配，仍绑定到预期头部基准。Kokkorylien02:20–04:48改现有眼瞳为接收曲面；鱼不吃茄子12:19–14:47由内眼眶边环填面，两者是不同输入的候选。后者非平面多边形还需检查导出三角化、法线和不平整。只清理独立接收面中确实无用的键，不删眼睑、瞳孔表情或L4N眼动键。
2. **声明与坐标**：eyeball标签、绑定骨、实际网格材料名、中心XYZ、眼球尺寸、角度偏移、虹膜尺寸分别核对。材料槽创建后用Select核每只眼真正被Assign；对称数值不替代左右检查。坐标来自导出约定中的模型基准，考虑对象/节点变换、轴和比例，不能一律照抄Blender Global或Max XYZ。用可定位的中心作起点，在工作副本逐项试调。
3. **纹理与shader**：左右VMT可以共享虹膜VTF，但独立材料身份与QC须一致。居中虹膜并保留足够眼白，检查重复接收层、投影尺寸及边界采样。EyeRefract的`$iris`、`$corneatexture`、`$ambientoccltexture`、`$envmap`不是一张basetexture的别名；主图正常仍可能缺辅助图。灰度入虹膜Alpha不等于生成RGB法线，不能把通道一律当透明。
4. **眼睑与控制**：`eyelid ... lowerer <帧> <偏移> neutral <帧> <偏移> raiser <帧> <偏移> ... eyeball <标签>`中的帧来自实际VTA，偏移不是权重。Valve QC Eyes以同坐标系的眼睑Z减眼球中心Z生成位置值；分别测左右上/下眼皮的降低/中性/抬高，匹配本模板帧号和split设置。GLB/Neko的按形状名写法另按版本核，不直接粘这段VTA语法。

一手依据：[QC Eyes数值生成](https://raw.githubusercontent.com/ValveSoftware/source-sdk-2013/master/src/utils/qc_eyes/QC_EyesDlg.cpp)、[EyeRefract参数](https://raw.githubusercontent.com/ValveSoftware/source-sdk-2013/master/src/materialsystem/stdshaders/eye_refract.cpp)、[纹理加载实现](https://raw.githubusercontent.com/ValveSoftware/source-sdk-2013/master/src/materialsystem/stdshaders/eye_refract_helper.cpp)。公开SDK分支用于核语义，不替L4D2实测。引擎[注视目标处理](https://raw.githubusercontent.com/ValveSoftware/source-sdk-2013/master/src/game/client/c_baseflex.cpp)还涉及viewtarget、眼attachment及eyes_updown/eyes_rightleft；相机视差/反射与角色注视控制分开诊断。

## 按症状检查，先定位再改

| 症状 | 优先检查与可采操作 | 避免的误修 |
|---|---|---|
| 一开新键脸就变形加倍 | 关闭新键/临时脸骨姿态做对照；检查双Armature和源混合值；只复原本次通道 | 删除唯一Armature、全清动画、靠反向键抵消 |
| Blender有表情，导出/编译后丢失或整脸错位 | 核导出对象/节点及隐藏元素；SMD/VTA顶点数、索引、坐标、中性帧；GLB目标键名与innode、控制器引用 | 只按列表数字改名；把所有VTA第25帧删空；重导比例“差不多”的脸 |
| 眉嘴动、眼皮不动 | 看是否使用eyelid且其eyeball被注释、标签失配；再查VTA帧/形状数据和规则 | 宣称所有眨眼都必须加假眼球；把滑条存在当变形已导出 |
| 虹膜正常，上覆紫黑格 | 尤其查AmbientOcclTexture指向的ambient.vtf，再查其他辅助图、Patch/include及搜索路径 | 只重做虹膜或坐标；把开发目录缺图靠共享游戏materials补上 |
| 只有一只眼正确/左右共用错投影 | 分别Select材料所分配的面，对照eye_l/eye_r与QC标签、骨和中心 | 仅建立两个空材质槽；按观察者左右误配人物左右 |
| 重复瞳孔/边缘露底 | 查两层均使用眼shader、接收面覆盖、虹膜留白/尺寸、极端方向采样 | 一律缩小虹膜；用无依据的固定1.45倍覆盖 |
| 眼球反向、朝上朝下混乱 | 查绑定骨轴/导出轴、中心和左右材料；检查眼attachment、控制器与模板是否被部分删掉 | 仅“加一套表情”作为必然修复；全局禁止某世界轴旋转 |
| 正视正常，侧视扭曲或眨眼穿出 | 查曲面三角化/法线、眼球中心相对深度和眼睑极值；固定其他参数后小步测试 | 固定Y=-2.4、无视负号谈变大/变小；把不规则曲面靠单参数保证修好 |
| 查看器正常，游戏或最终VPK失效 | 分别核游戏注视输入、shader运行依赖、实际加载文件与包内全部纹理/伴随文件 | 把HLMV滑条或开发挂载成功当原版独立验收 |

Kokkorylien简介“先做表情后拆分”保留为防丢变形器的顺序选择，仍需完整拓扑对应；“表情保证眼追方向”只属其模板现象。鱼不吃茄子只保留一个闭眼形状、上下眼睑重复引用的方式是简化效果，不是二次元通用规范。不要因模板可编译就接受缺嘴形、重复叠加或眼皮穿模。

验收记录拆为：编辑器极值/组合、导出数据、编译/查看器、目标游戏、隔离开发资源后的最终VPK。纯原版目标必须无未声明的运行shader/控制器依赖；只隔离本任务资源，不清共享materials或Steam Cloud。无真实模型与模板时交付可追溯候选方案和具体缺口，不宣称本机原版眼追已验证。
