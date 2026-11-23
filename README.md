# Switch 2 Connect
### 在 Windows 上通过系统蓝牙、ESP32-S3 N16R8 或 USB 使用受支持的 Switch 2 手柄、NSO GameCube 手柄及 Mobapad M12 Pro

这是基于上游 v3.4 的简体中文分支。运行汉化版源码可参照下方的[源码运行](#源码运行)，页面顶部的下载链接指向上游发布版。

<p align="center">
 <a href="https://github.com/TommyWabg/Switch2Connect/releases/download/v3.4/Switch2Connect_v3.4.exe"><img width="200" alt="应用图标" src="https://github.com/TommyWabg/Switch2Connect/blob/main/resources/images/icon.png" />
</p>
<p align="center">
  <a href="https://github.com/TommyWabg/Switch2Connect/releases"><img src="https://img.shields.io/github/v/release/TommyWabg/Switch2Connect?style=flat-square&color=9be1e6&labelColor=e4896e" alt="发布版本"></a>
  <a href="https://github.com/TommyWabg/Switch2Connect/releases/download/v3.4/Switch2Connect_v3.4.exe"><img src="https://img.shields.io/github/downloads/TommyWabg/Switch2Connect/total.svg?style=flat-square&color=9be1e6&labelColor=e4896e" alt="下载总量"></a>
  <a href="https://github.com/TommyWabg/Switch2Connect/blob/main/LICENSE.md"><img src="https://img.shields.io/github/license/TommyWabg/Switch2Connect?style=flat-square&color=9be1e6&labelColor=e4896e" alt="许可证"></a>
  <br>
  <a href="#系统要求"><img src="https://img.shields.io/badge/platform-Windows%2010/11%20App%20%7C%20ESP32--S3%20N16R8%20Firmware-287cff?style=flat-square&color=9be1e6&labelColor=e4896e" alt="平台：Windows 10/11 应用及 ESP32-S3 N16R8 固件">
</p>
<p align="Center">
  <a href="#microsoft-store-版本">
    <img width="150" alt="Microsoft Store" src="https://github.com/user-attachments/assets/19016267-e0e0-428c-aa07-7878a10db9e8">
  </a>
</p>
<p align="center">
  <a href="https://ko-fi.com/tagayama">
    <img width="200" src="https://storage.ko-fi.com/cdn/brandasset/v2/support_me_on_kofi_beige.png?_gl=1*1ndc5yc*_gcl_au*MTAzOTY3NTA1Ni4xNzgyODE2Nzkx*_ga*MTQ5NTE2MDk5MC4xNzgyODE2Nzky*_ga_M13FZ7VQ2C*czE3ODQzMDg3NDckbzQ0JGcxJHQxNzg0MzA5NTQxJGo1OSRsMCRoMA.." alt="ko-fi">
  </a>
</p>

## 选择版本并开始使用

### Microsoft Store 版本

#### 优点
* 通过商店分发并签名，可减少 Windows Defender 或其他杀毒软件将应用识别为恶意软件或不可信下载的情况。
* 支持自动更新。

#### 缺点
* 应用内不提供 WinUHid 驱动安装程序。需要使用 [WinUHid_Manager.exe](https://github.com/TommyWabg/Switch2Connect/releases/download/v1.8_MicrosoftStore/WinUHid_Manager.exe) 单独安装。
* 新版本的审核和分发最多可能需要 3 天。

#### 关于 WinUHid 的重要说明
为遵守 Microsoft Store 的打包和驱动分发政策，商店版**不会附带或安装 WinUHid 驱动**。这并非手柄或硬件兼容性问题。

但商店版可以检测并使用另外安装且运行正常的 WinUHid 驱动。

如果未安装 WinUHid，或安装不完整：
* WinUHid 驱动模式不可用。
* IR 鼠标原始输入模式不可用。
* 相关控件不会显示。
* 商店版不会弹出 WinUHid 安装提示。

#### 开始使用 Microsoft Store 版本

1. 从 **[Microsoft Store](https://apps.microsoft.com/store/detail/9N6VDZ4GWHH1?cid=DevShareMCLPCS)** 下载并安装 Switch 2 Connect。
2. 如需使用 WinUHid 相关功能，下载 **[WinUHid_Manager.exe](https://github.com/TommyWabg/Switch2Connect/releases/download/v1.8_MicrosoftStore/WinUHid_Manager.exe)** 安装或修复 WinUHid 驱动。
3. 启动应用并按界面提示完成设置。如果 Windows 要求安装受支持的驱动，请允许管理员权限提示。
4. 长按 SYNC 键打开 Switch 2 手柄；如果手柄已经配对，按任意键即可。**不要**在 Windows 蓝牙设置中手动配对手柄，应用会自动通过 GATT 发现设备。
5. 在应用底部的设置面板中配置可用的驱动模式、按键布局、陀螺仪灵敏度和自定义按键映射。

<p align="Center">
  <a href="https://apps.microsoft.com/store/detail/9N6VDZ4GWHH1?cid=DevShareMCLPCS">
    <img width="150" alt="Microsoft Store" src="https://github.com/user-attachments/assets/19016267-e0e0-428c-aa07-7878a10db9e8">
  </a>
</p>

### GitHub 版本
#### 优点
* 功能完整，内置 WinUHid 检测和安装指引。
* 可以直接获取最新版本。

#### 缺点
* 未签名，因此 Windows Defender 或其他杀毒软件可能提示下载来源不可信，或误报为恶意软件。

  ***说明：**v1.7 之后的所有版本都会提交给 [Microsoft Security Intelligence](https://www.microsoft.com/en-us/wdsi/filesubmission) 审核，以消除误报。请求通常会在新版本发布后的一到两天内处理。*

* 不支持自动更新。

#### 开始使用 GitHub 版本
1. 从上游 [v3.4 发布页](https://github.com/TommyWabg/Switch2Connect/releases/tag/v3.4)下载 **[Switch2Connect_v3.4.exe](https://github.com/TommyWabg/Switch2Connect/releases/download/v3.4/Switch2Connect_v3.4.exe)**。
2. 启动应用。如果尚未安装 WinUHid，系统会弹窗询问是否安装；如果在设置中选择了 USBIP 驱动模式，也会提示安装 USBIP 驱动。点击**是**并允许管理员权限提示。
3. 安装完成后，设置窗口会自动关闭，应用主界面随即打开。
4. 长按 SYNC 键打开 Switch 2 手柄；如果手柄已经配对，按任意键即可。**不要**在 Windows 蓝牙设置中手动配对手柄，应用会自动通过 GATT 发现设备。
5. 在应用底部的设置面板中配置驱动（WinUHid / ViGEmBus / USBIP）、按键布局、陀螺仪灵敏度和自定义按键映射。

## 源码运行

在 Windows 上安装 64 位 Python 3.12 和 Git。首次从源码编译 PyBluez 还需要 Microsoft C++ Build Tools。在项目根目录执行以下命令。

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe src\gui.py
```

安装依赖后，也可以双击 `RUN ME.bat` 启动。使用 ESP32-S3 N16R8 桥接器时，请先将固件升级至 v3.4。

## 从 v2.9.1 升级到 v3.4

| 版本 | 主要变化 |
| --- | --- |
| [v3.4](https://github.com/TommyWabg/Switch2Connect/releases/tag/v3.4) | 新增 Mobapad M12 Pro 支持。修复 Windows 蓝牙 GATT 服务缺失时的恢复流程、ESP32 槽位残留上一个手柄的数据，以及 M12 初始化失败后未重试的问题。 |
| [v3.3](https://github.com/TommyWabg/Switch2Connect/releases/tag/v3.3) | 修正 Switch 2 模拟的体感轴向、陀螺仪比例和偏置，解决窗口隐藏等情况下输入报告降到约 65 次／秒的问题。 |
| [v3.2](https://github.com/TommyWabg/Switch2Connect/releases/tag/v3.2) | 降低 USBIP DualSense 的 CPU 占用，修复后台状态轮询的事件句柄泄漏，修正 Eden 等模拟器直连虚拟 Switch 1 Pro 手柄时的输入和陀螺仪。 |
| [v3.1](https://github.com/TommyWabg/Switch2Connect/releases/tag/v3.1) | 改善 SDL3 原生振动的短脉冲播放，加入 ESP32 串口积压诊断和蓝牙断开超时处理。 |
| [v3.0](https://github.com/TommyWabg/Switch2Connect/releases/tag/v3.0) | 新增 SDL3 原生振动和应用内陀螺仪“始终启用”，修复振动积压及 USBIP 清理时误断开其他软件设备的问题。 |
| [v2.10](https://github.com/TommyWabg/Switch2Connect/releases/tag/v2.10) | 修复支持原生 DualSense 的游戏将普通声音误送到虚拟手柄的问题，保留音频触觉反馈。 |

## 功能介绍

* **原生支持 Windows 10：**支持 Windows 10 22H2 和 Windows 11。Windows 11 的低功耗蓝牙轮询率最高可达 70 Hz；受系统 BLE 驱动实现限制，Windows 10 最高为 20 Hz。
* **低延迟蓝牙模式：**将 Windows 低功耗蓝牙连接设置为 ThroughputOptimized 模式，以缩短连接间隔和手柄输入延迟。
* **ESP32-S3 N16R8 低延迟连接：**支持将 ESP32-S3 N16R8 开发板用作 BLE 桥接器，轮询率最高可达 133 Hz。应用提供固件安装与修复、通过 SYNC 键配对手柄，以及已与桥接器绑定的手柄重连功能。
* **有线手柄支持：**支持通过 USB 连接的 Switch 2 Pro 手柄和 NSO GameCube 手柄，轮询率最高可达 500 Hz。**有线 Pro 手柄**菜单提供 HidHide 管理、自动发现控制和单次手动扫描。对于 NSO GameCube 手柄的振动，应用会自动选择可用的 USB 接口，并在必要时回退到兼容路径。
* **Mobapad M12 Pro 支持：**通过系统蓝牙或 ESP32-S3 N16R8 连接时可自动识别 M12 Pro，支持 Joy-Con 2 的按键、摇杆、鼠标模式、陀螺仪、加速度计和振动。单侧 M12 Pro 可以与另一侧的 Joy-Con 2 合并使用。
* **多种驱动与模拟后端：**支持 WinUHid、ViGEmBus 和 USBIP。WinUHid 可模拟 Xbox One、PS4 和 PS5 手柄；ViGEmBus 可模拟 Xbox 360 和 PS4 手柄；USBIP 可模拟通过 USB 连接的 Switch 2 Pro 手柄和 DualSense。应用会检测 WinUHid 和 ViGEmBus 是否缺失或安装不完整，并提供安装、修复和卸载操作。获得 UAC 授权后，可在应用内下载并安装 ViGEmBus。
* **选项卡式设置界面：**设置分为手柄映射、模式切换映射和陀螺仪设置三个选项卡。
* **DualSense 音频触觉反馈：**基于 USBIP 的 PS5 模拟模式会为支持 DualSense 音频触觉的游戏提供四声道音频播放端点。同时支持 DualSense 音频触觉、标准 PS5 振动、Xbox 振动转换，以及将自适应扳机反馈转换为左右扳机各自独立的 HD Rumble 输出。
* **Xbox One 脉冲扳机支持：**在 WinUHid Xbox One 模拟模式中，LT 和 RT 的 Xbox 脉冲扳机力反馈值会转换为 Switch 2 的高频 HD Rumble 输出。普通手柄振动会作为相同的单声道信号发送到手柄两侧；脉冲扳机反馈则分别叠加到左右两侧的高频信号中，以呈现对应扳机的效果。
  * **脉冲扳机设置：**在 WinUHid Xbox One 模拟模式中，**脉冲扳机设置**按钮位于**振动模式**旁。浮动设置窗口可以启用脉冲反馈、选择动态或固定频率、调整强度并设置固定频率档位。
  * **动态频率：**启用后，输入的脉冲强度同时决定输出频率和振幅。停止后的衰减阶段，频率仍会随当前逐渐降低的输出强度变化。
  * **固定频率：**关闭动态频率后，可用**频率**滑块独立设置脉冲输出频率，不受输入强度影响。
  * **释放衰减：**收到脉冲扳机停止命令后，当前输出会在 90 毫秒内线性衰减至零。同侧的新命令会立即取代尚未完成的衰减。
* **原生体感支持（PS4/PS5 模式）：**切换到 PS4 或 PS5 模式后，通过 DS4 或 DualSense 协议报告原生体感数据，改善与 Steam Input 及支持 DualShock 4 或 DualSense 陀螺仪功能的游戏的兼容性。
* **Cemuhook UDP 服务器：**通过 `127.0.0.1:26760` 向兼容应用发送手柄体感数据。在陀螺仪直通设置中选择 Cemuhook 即可启用。
* **Cemuhook 陀螺仪灵敏度调节：**陀螺仪直通面板提供 1–5 档灵敏度滑块。该设置只对经 Cemuhook UDP 协议发送的水平旋转（偏航）轴应用线性倍率。
  * **第 1 档：**实体 Switch 2 Joy-Con 旋转 360 度时，虚拟 Switch 1 Joy-Con 也旋转 360 度。
  * **第 5 档：**匹配真实 Switch 1 Joy-Con 的灵敏度。
* **实时切换按键布局：**可直接在界面中切换**任天堂布局**（匹配实体按键标识）和 **Xbox 布局**（标准 PC 按键位置）。
* **NSO GameCube 手柄布局映射：**在 Xbox、PlayStation 和 Switch 模拟模式中保持一致的 ABXY 布局映射。Xbox 布局按按键的实体位置映射，Switch 布局按输入功能映射。
* **1000 Hz 插值：**Switch 2 右 Joy-Con 和 Pro 手柄通过 1000 Hz 插值循环实现更平滑的陀螺仪动作；**陀螺仪鼠标**和 **Joy-Con 鼠标**也以 1000 Hz 输出，减少卡顿和延迟。向第三方模拟器等外部应用传递体感数据时，应用同样以稳定的 1000 Hz 高频率发送，但不会插入合成的中间帧，而是提高实时实体数据的发包频率，以避免人为增加延迟。
* **应用内陀螺仪控制（鼠标、右摇杆和方向盘）：**可以用陀螺仪瞄准，也可以选择右摇杆或方向盘模式。方向盘模式读取加速度计测得的手柄绝对倾角，并将其映射到左摇杆 X 轴。与鼠标模式不同，右摇杆和方向盘模式使用单独的应用内陀螺仪映射范围，所有按键默认保持常规手柄输入，避免模拟手柄时意外触发鼠标点击。
* **九轴鼠标模式（磁力计辅助）：**结合陀螺仪、加速度计和磁力计数据，减少偏航角累计漂移，使长时间游玩时的鼠标移动更贴近手柄的实体朝向。磁场和航向可靠时会逐步施加磁校正，不可靠时则暂停校正。
* **六轴鼠标模式：**仅使用陀螺仪和加速度计，不进行磁校正，因此不受附近磁干扰影响。无论手柄如何倾斜，鼠标移动都会保持相对于水平面的方向；长期偏航漂移仍取决于陀螺仪校准和传感器精度。
* **摇杆辅助：**允许右摇杆与陀螺仪瞄准同时使用。
* **应用内陀螺仪始终启用：**可以在应用内陀螺仪面板打开“始终启用”，无需映射按键。它相当于额外的点按触发器，已映射的按键仍可切换状态。开启时可单独设置触发死区和减敏。多个触发器同时启用时，采用最近开启且仍处于启用状态的触发器设置。
* **应用内陀螺仪触发死区：**可在应用内陀螺仪映射弹窗中配置。可指定一个或多个按键，在应用内陀螺仪启用时施加专用触发死区，并调整死区大小、按下及松开后的陀螺仪暂停时间，以及松开后死区效果的持续时间，减少按键操作或手柄振动引起的误动作。
* **应用内陀螺仪触发减敏：**可在同一映射弹窗中指定按键，按自定义百分比降低陀螺仪灵敏度，并设置松开按键后的减敏持续时间，便于更平稳地瞄准或转向。
* **应用内陀螺仪锁定：**在保持应用内陀螺仪模式的同时暂停陀螺仪控制，支持按住和点按两种触发方式。
* **陀螺仪直通：**
  * **九轴辅助：**借助磁力计处理体感数据，减少直通陀螺仪输出中的偏航累计漂移。校正力度会根据动作和磁场可信度调整；条件不可靠时暂停，磁场恢复后逐步继续。关闭后仅使用陀螺仪和加速度计。
  * **水平锁定：**补偿横滚，保持水平参考方向，并抑制横滚输出。
  * **可调软死区：**为应用内陀螺仪和体感直通分别提供软死区滑块。达到设定阈值后，输出从零开始变化，避免突然跳变。
* **陀螺仪校准：**点击**校准陀螺仪**，计算并永久保存传感器偏差，以消除陀螺仪漂移。
* **磁力计校准：**点击**校准磁力计**以提高九轴精度。按“8”字形移动手柄完成校准，界面中还提供[视频教程](https://youtu.be/J_cZnPcW-Yw?si=QWSizI49NQ_5OkA7)的快捷链接。
* **双 Joy-Con 陀螺仪（DJG）：**将左右 Joy-Con 合并使用时，可融合两侧体感数据，减少反复调整握持位置时的瞄准卡顿。系统将一侧设为提供方向和重力参考的“主侧”，另一侧设为辅助加速的“副侧”。副侧的动作幅度阈值为 30；只有主侧超过该阈值时，副侧才参与加速。副侧加速最多为主侧动作的 2 倍，反方向动作会被忽略。关闭主侧陀螺仪后，副侧会接管控制。
  * 打开**双 Joy-Con 陀螺仪（DJG）**面板。
  * 将 **DJG** 开关切换为**开**，启用融合引擎。
  * 将**主侧**设为**左**或**右**。主侧提供主要的方向和重力参考，副侧提供加速。
* **DJG 触发映射：**额外按键映射设置中提供专用的 **DJG** 选项。
  * 可将 DJG 操作分配给任意可用的额外按键，作为 DJG 功能的实体触发键。
  * 游戏中按下该键时，会执行当前 DJG 控制模式和触发设置指定的操作。
* **DJG 控制模式：**提供三种模式，用于决定映射的 DJG 触发键在游戏中的行为。
  * **切换主侧：**互换左右 Joy-Con 的主侧与副侧角色，切换时强制启用两侧。
  * **切换陀螺仪侧：**关闭当前使用的陀螺仪，仅启用另一侧 Joy-Con 的陀螺仪，并自动同步主侧设置。
  * **单侧切换：**独立切换一侧 Joy-Con 的陀螺仪跟踪状态。映射在左 Joy-Con 上的 DJG 触发键控制左侧陀螺仪，映射在右 Joy-Con 上的则控制右侧。选择**主侧：左**或**右**可指定主要一侧；选择**主侧：无**则直接合并两侧已启用的体感输入，并仍可用 DJG 操作分别管理两侧。
* **DJG 触发方式：**提供两种触发行为。
  * **点按切换：**每按一次按键，切换一次 DJG 状态。
  * **按住：**按下时切换 DJG 状态，松开时恢复原状态。
* **各手柄独立的摇杆死区：**可分别设置 Pro 手柄、Joy-Con 和 NSO GameCube 手柄的左右摇杆死区。每类手柄单独保存数值，也可以选择联动或分开调整左右摇杆。
* **完整的手柄重映射：**所有按键，包括 GL、GR、SL_L、SL_R、SR_L、SR_R、NSO GameCube L/R 模拟扳机点击、Home、截图和 Chat 等额外按键，都可以映射为 Switch 或 PlayStation 输入、应用内控制、Windows 控制、鼠标点击或录制的自定义输入。摇杆也可映射为左右摇杆、WASD、鼠标控制或自定义输入。映射界面按类别组织弹窗，便于选择。
* **Joy-Con 红外传感器映射：**左右 Joy-Con 的红外传感器都可作为独立实体输入。每侧可以单独设置功能映射、触发阈值、红外鼠标灵敏度、鼠标按键映射和滚动。红外鼠标的输出方式跟随当前配置档案中的鼠标输出设置。
* **高级自定义输入映射：**可录制键盘按键、鼠标点击和手柄按键的任意组合，并映射到单个输入。支持**点按**（短暂触发录制的组合）和**按住**（持续保持该组合直到松开按键）两种模式。
  * 打开下拉菜单，选择**自定义**。
  * 同时按住需要组合的键盘按键、鼠标按键和／或手柄按键。
  * 松开所有输入后，录制会自动停止并保存。
  * 点击旁边的切换按钮，选择**点按**（触发一次）或**按住**（按住手柄按键期间持续保持）。
  * 点击 **X** 删除自定义输入，恢复默认映射。
* **模式切换映射系统：**使用应用内陀螺仪映射存储区作为另一层按键映射。可通过专用映射操作启用模式切换层，支持**按住**（按住期间生效）和**点按**（切换开关）。两种操作共用状态机制：在点按已开启模式切换时，按住操作会临时反转其状态。此外，还可根据每个配置档案的陀螺仪控制设置，在进入应用内陀螺仪模式时自动应用模式切换层。
* **按模拟模式分类的映射：**Xbox、PS4、PS5 和 Switch 2 模拟模式分别保存按键映射和振动设置，切换模拟模式时加载对应配置。
* **按配置档案选择键鼠输出：**每个档案都可独立选择 Win32 API 或 WinUHid 虚拟 HID 输出。键盘映射可使用虚拟 HID 键盘；每个已连接手柄的陀螺仪、摇杆、红外传感器、映射的鼠标按键和滚动可使用独立的虚拟 HID 鼠标。WinUHid 不可用时使用 Win32 API 输出。
* **自定义映射档案系统：**可创建、重命名、导入、导出、重置、删除和切换多个配置档案。每个档案会持久保存按键映射、模拟模式和驱动设置。专用弹窗还可设置“切换档案列表”和“档案切换组合键”，提供三种切换方式：
  * **档案切换组合键：**录制自定义触发输入，并为各档案指定对应的组合输入。同时按下触发输入和目标档案的组合输入，即可立即切换。单独使用时，这些输入仍执行常规映射。
  * **自动切换档案：**触发输入停止活动 2 秒后，自动切换到“切换档案列表”中勾选的档案。
  * **手动切换档案：**打开选择提示，用左右摇杆或方向键上下浏览已勾选的档案，再用当前 Xbox／Switch 布局中的 A 确认、B 取消。
    * **自动／手动模式设置：**点击“切换档案”按钮，在弹窗中选择自动或手动模式。
  * **配置导入与导出：**可将所选档案导出为 `.yaml` 文件，或从中导入。导入时可保留现有档案，并解决应用程序分配重复的问题。省电设置、驱动状态、窗口位置和设备缓存等与本机相关的信息仍保存在当前安装中。
  * **手柄数据迁移：**导入或导出配置时，可以包含校准数据等手柄专属设置。
* **按应用程序分配档案：**可根据当前前台应用自动切换档案。将一个或多个 `.exe` 文件绑定到档案后，这些应用获得焦点时，对应档案会自动启用。
* **动态拆分与合并：**无需重启，即可将一对合并的 Joy-Con 拆分为两个独立手柄，或将单个 Joy-Con 合并为一个统一的虚拟手柄。
* **竖握／横握模式切换（V/H）：**单个 Joy-Con 可通过 V/H 按钮在标准竖握和侧向横握之间切换。
* **记住每个 Joy-Con 的握持方式：**应用会记录每个单独 Joy-Con 的竖握或横握偏好，按其蓝牙 MAC 地址关联，并保存到 `config.yaml`。
* **双 Joy-Con 陀螺仪侧选择（左／右）：**将一对 Joy-Con 作为单个虚拟手柄使用时，可手动选择由左侧或右侧提供体感数据，方便按自己习惯的手使用陀螺仪瞄准。
* **可调振动强度：**振动强度可在 0–10 之间调整。
* **振动频率滑块：**选择转换后振动输出使用的频率。
* **振动延迟设置：**以毫秒为单位设置延迟，使振动与游戏音频同步。
* **振动模式选择：**可以切换 Xbox 风格振动、Switch HD Rumble 和 SDL3 原生振动。
  * **Xbox 模式：**面向普通 PC 游戏，通过动态频率缩放和高频遮罩模拟传统双马达手柄的振动。
    * 强度 5 ＋ 频率 10：模拟 DualSense Edge 手柄的触感。
    * 强度 10 ＋ 频率 10：模拟 Xbox Elite Series 1 手柄的振动。
  * **Switch 模式：**模拟原生 Switch HD Rumble（LRA）体验。跳过自定义频率缩放和遮罩，将原始频率数据直接发送给手柄，获得更紧致、柔和且细腻的触感，适合任天堂游戏模拟。
  * **SDL3 原生模式：**在 Switch 2 模拟模式下，将 SDL3 的 HD Rumble 信号直接发送给 Pro 手柄和 Joy-Con，仅应用 SDL3 自身的振幅上限。此模式下强度和频率滑块不生效，NSO GameCube 手柄也不支持。建议用于基于 SDL3 的平台和游戏。
* **通过振动识别手柄：**每个玩家槽位都有专用的**振动**按钮，可通过实体反馈快速确认多人游戏中各 Joy-Con 对应的玩家。
* **触觉反馈与系统集成：**支持振动反馈，包括连接成功时的确认振动；还可将截图键映射为 Windows 原生截图快捷键（`Win + PrtScn`）。
* **一键断开连接：**每个已连接手柄的界面区域右上角都有 **X** 按钮，可直接断开指定手柄，无需关闭手柄电源。
* **自动断开选项：**提供**关闭**、**空闲**和**绝对时长**三档。
  * **空闲：**根据实体按键和摇杆输入，自动断开长时间闲置的手柄，同时保留正在使用的手柄连接。
  * **绝对时长：**按手柄连接到应用的总时间计时，达到时限后断开。
* **驱动管理：**对当前选用的 WinUHid、ViGEmBus 或 USBIP 后端提供安装、修复和卸载操作。驱动状态综合活动设备、驱动存储中的软件包、服务注册情况和运行时可用性判断，而不只依赖已保存的配置。
* **ESP32-S3 N16R8 驱动管理器：**提供固件安装、修复和删除、BOOT 与 OTG 状态监测、重连处理和刷写诊断。刷写端口可自动检测或手动选择 COM 口；应用优先选择已验证的 ESP32-S3 设备，记住跨重启和 COM 口变化的选择，并避免选中无关串口设备。
* **省电模式：**
  * **关闭：**保留手柄输入、体感、振动、扫描和后台状态检查等全部功能。
  * **自动：**降低空闲时的 CPU 占用，同时保留按键、摇杆、扳机、体感控制和手柄扫描。HD Rumble、音频触觉和脉冲扳机反馈可能延迟、中断或偶尔丢失。
  * **完全：**保留按键、摇杆、扳机和非体感映射；关闭振动输出、陀螺仪直通、应用内陀螺仪、DJG、红外鼠标和摇杆鼠标移动。暂停定期 ESP32 及有线／HidHide 状态检查。连接 1 个 Pro／NSO GameCube 手柄或 2 个 Joy-Con 后，自动手柄扫描会暂停。
* **开机启动：**随 Windows 自动启动应用。
* **启动时最小化：**启动后直接进入系统托盘。
* **最小化到系统托盘：**将应用窗口隐藏到 Windows 系统托盘。
* **手柄导航界面：**可用左摇杆或方向键浏览应用界面。所选控件会显示白色边框；使用鼠标操作或按 B 退出导航模式后，边框会隐藏。
  * **活动窗口焦点：**打开浮动窗口或弹窗时，导航范围保持在当前活动的顶层界面内。
  * **返回选中位置：**按 B 关闭活动浮动窗口后，选中位置会返回打开该窗口的控件。重新进入导航模式时，会恢复上次选中的控件。
  * **界面控件操作：**按 A 激活按钮或打开下拉菜单；按 B 关闭已打开的浮动窗口或退出导航模式。
  * **文本输入调整：**可用右摇杆，或按住 A 并使用左摇杆来调整输入框中的数值；持续按住时，调整速度会加快。
  * **滑块和时间输入调整：**可用右摇杆，或按住 A 并使用左摇杆来调整。
* **记住窗口位置：**保存并恢复主窗口的位置。
* **应用内界面缩放：**主窗口底部提供 1.0×–2.0× 的缩放滑块，选择的比例会自动保存并恢复。
  * **适配显示器：**根据当前显示器分辨率和可用工作区域自动调整窗口。
  * **适配内容：**必要时自动加宽窗口；内容超过可用高度时提供滚动。
* **独立可执行文件（`.exe`）：**已包含所需的 Python 运行环境和应用依赖，无需另外安装 Python。

## 已知限制

* **暂不支持 Amiibo：**尚未实现 Amiibo 功能。
* **暂不支持 Switch 2 Pro 手柄音频：**不支持通过无线连接传输该手柄耳机接口和麦克风的音频。
* **NSO GameCube 手柄陀螺仪暂不可用：**目前无法正确解码其陀螺仪数据。
* **NSO GameCube 手柄振动制动和强度调节暂不可用：**目前尚不清楚振动马达制动命令，因此无法正确实现基于 PWM 的振动强度控制，只支持基本的马达开关控制。
* **暂不支持 Switch 2 Joy-Con 充电握把背键：**充电握把的背部按键不可用。
* **实体手柄兼容范围：**上游目前支持任天堂官方 Switch 2 手柄和 Mobapad M12 Pro，暂无支持初代 Switch 实体手柄及其他第三方手柄的计划。
* **Mobapad M12 Pro 限制：**电量始终显示为满格，无法读取磁力计数据。

## 系统要求

* **操作系统：**Windows 10 22H2 或更新版本，或 Windows 11。
    * *说明：*为获得更好的体验，**强烈建议使用 Windows 11**。它的低功耗蓝牙轮询率最高可达 **70 Hz**；由于系统 BLE 驱动支持的限制，Windows 10 最高为 **20 Hz**。
* **蓝牙硬件：**稳定连接和低延迟表现需要蓝牙 5.0 或更新版本。如需达到 133 Hz，强烈建议选配 ESP32-S3 N16R8，以在 PC 上获得接近 Switch 2 主机的体验。
* **驱动：**模拟 Xbox One、PS4 和 PS5／DualSense 手柄需要 [lurebat 的 WinUHid 驱动](https://github.com/lurebat/WinUHid)；模拟 Xbox 360 和 PS4 手柄需要 [nefarius/ViGEmBus](https://github.com/nefarius/ViGEmBus)；模拟 Switch 1 Joy-Con／Pro 手柄、Switch 2 Pro 手柄和带音频触觉的 PS5／DualSense 手柄需要 [usbip-win2 驱动](https://github.com/vadimgrn/usbip-win2)。
    * *自动安装：*应用会自动检测所选驱动（WinUHid、ViGEmBus 或 USBIP）是否缺失，并引导一键安装（需要管理员权限）；ViGEmBus 还可由应用自动下载并安装。

### ESP32-S3 N16R8

<img width="447" height="235" alt="ESP32-S3 N16R8 指南" src="https://github.com/user-attachments/assets/6bb295fb-bc2c-4cb4-b859-ead65429ee64" />

* **ESP32-S3 N16R8 固件安装指南：**

1. 按住 ESP32-S3 N16R8 开发板上的 BOOT 按钮。
2. 按住 BOOT 按钮的同时，用 USB-C 线将开发板的 OTG 接口连接到电脑。
3. 在应用中点击 **[ESP32-S3 N16R8 驱动]**。
4. 点击**[安装]**，等待安装完成。
5. 拔下开发板，然后重新插入。
6. 对之前通过系统蓝牙配对的手柄按下 SYNC 键，使其重新连接。

* **ESP32-S3 N16R8 选购指南：**
1. 只选择明确标注 **ESP32-S3 N16R8** 的开发板。这表示板上有处理复杂任务和手柄连接所需的 16 MB Flash 与 8 MB PSRAM。避免购买标注为“N8R2”“N8R8”或普通“ESP32”的开发板。
2. 如果需要内置 PCB 天线，选择 **ESP32-S3-WROOM-1**，它适合普通塑料外壳，接线即可使用。只有在使用金属外壳，或需要外置天线扩展蓝牙／Wi-Fi 范围时，才选择 ESP32-S3-WROOM-1U。
3. 确认开发板带有 **OTG USB 接口**，常见于双 USB-C 接口设计。数据传输和固件安装都必须使用 OTG 接口。

## Steam 用户的重要设置
本应用可模拟 Xbox One 和 PS4／PS5 手柄。如果 Steam Input 再次覆盖按键布局，按键可能被重复对调，导致游戏内操作错乱。

**请按以下步骤保持布局一致：**
1. 打开 **Steam > 设置 > 控制器 > 显示高级设置**。
2. 确认**为 Xbox 控制器启用 Steam Input** 已**开启**。
3. 将 **PlayStation 控制器支持**设为**已启用**，不要选择“仅在不支持的游戏中启用”。
4. 之后由 Switch2Connect 负责切换按键布局。

## 陀螺仪校准指南

为提高精度并消除光标漂移，请按以下步骤校准六轴陀螺仪：
1. **静置手柄：**将 Pro 手柄放在完全平整、稳定的表面上。**校准过程中不要触碰或移动手柄。**
2. **开始校准：**点击设置面板中的**[校准陀螺仪]**按钮。
3. **等待倒计时：**界面会显示校准倒计时（如 `Calibrating (2..)`）。
4. **完成：**按钮显示 `Calibration Done` 后，软件已计算并保存传感器偏差。除非再次出现漂移，否则无需重新校准。

## 磁力计校准指南

为减少九轴追踪漂移，请按以下步骤校准磁力计：
1. **开始校准：**点击设置面板中的**[校准磁力计]**按钮。按钮会变成橙色并显示 `Stop Mag Calib`。
2. **画“8”字：**握住手柄，在空中持续画**“8”字**，并确保手柄绕三个轴转动，以覆盖完整的磁场范围。
3. **参考视频：**如果不确定动作，可点击界面中的[**“8”字动作演示链接**](https://youtu.be/J_cZnPcW-Yw?si=QWSizI49NQ_5OkA7)观看短视频。
4. **保存并完成：**持续动作约 5–10 秒后，点击 **[Stop Mag Calib]** 保存校准数据。软件会使用新的磁偏差数据稳定方向判断。

## 支持本项目

本项目以用户体验为出发点，目前功能已较为成熟和完整，并将永久免费使用。

如果这款应用改善了你的游戏体验，也欢迎通过小额赞助支持作者。任何形式的支持都十分感谢！

<p align="left">
  <a href="https://ko-fi.com/tagayama">
    <img width="200" src="https://storage.ko-fi.com/cdn/brandasset/v2/support_me_on_kofi_beige.png?_gl=1*1ndc5yc*_gcl_au*MTAzOTY3NTA1Ni4xNzgyODE2Nzkx*_ga*MTQ5NTE2MDk5MC4xNzgyODE2Nzky*_ga_M13FZ7VQ2C*czE3ODQzMDg3NDckbzQ0JGcxJHQxNzg0MzA5NTQxJGo1OSRsMCRoMA.." alt="ko-fi">
  </a>
</p>

祝你游戏愉快，感谢支持！

## 致谢
**本项目基于 [Nadeflore/switch2-controllers](https://github.com/Nadeflore/switch2-controllers) 开发，并在其基础上进行了大量修改。感谢原作者打下的基础。**
* **[Nadeflore/switch2-controllers](https://github.com/Nadeflore/switch2-controllers)：**本项目的核心基础。
* **[TheFrano/joycon2py](https://github.com/TheFrano/joycon2py)、[german77/JoyconDriver](https://github.com/german77/JoyconDriver)、[darthcloud/BlueRetro](https://github.com/darthcloud/BlueRetro/issues/1249)：**原始 switch2-controllers 项目所依据的脚本和逆向研究资料。
* **[nefarius/ViGEmBus](https://github.com/nefarius/ViGEmBus)、[lurebat/WinUHid](https://github.com/lurebat/WinUHid)、[vadimgrn/usbip-win2](https://github.com/vadimgrn/usbip-win2)：**用于模拟虚拟手柄的驱动。
* **[ndeadly/switch2_controller_research](https://github.com/ndeadly/switch2_controller_research)：**虚拟 Switch 2 Pro 手柄模拟和实体有线 Switch 2 Pro 手柄输入转换的逆向研究。
* **[dekuNukem/Nintendo_Switch_Reverse_Engineering](https://github.com/dekuNukem/Nintendo_Switch_Reverse_Engineering)：**Switch 1 Pro 手柄和 Joy-Con 模拟的逆向研究。
* **[mart1nro/joycontrol](https://github.com/mart1nro/joycontrol)：**Switch 1 Pro 手柄和 Joy-Con 模拟的参考实现。
* **[LeonChrome/XinHeLianSheng-Pro2-Bridge](https://github.com/LeonChrome/XinHeLianSheng-Pro2-Bridge)：**ESP32-S3 N16R8 实现的灵感来源，也是 DualSense 音频触觉和基于 USBIP 的 Switch 2 手柄模拟实现的参考资料。
* **[SundayMoments/DS5_Bridge](https://github.com/SundayMoments/DS5_Bridge)：**DualSense 音频端点 HID 描述符的主要参考资料。
* **[JibbSmart/JoyShockLibrary](https://github.com/JibbSmart/JoyShockLibrary)：**Switch 1 Joy-Con 陀螺仪方向的参考资料。
* **[RyanCopley/NSO-GameCube-Controller-Pairing-App](https://github.com/RyanCopley/NSO-GameCube-Controller-Pairing-App)：**NSO GameCube 手柄相关功能和 BLE 吞吐优化模式的参考资料。
* **[DarkEslariate/m12-pro-support](https://github.com/DarkEslariate/Switch2Connect/tree/m12-pro-support)：**贡献了 Mobapad M12 Pro 支持。
