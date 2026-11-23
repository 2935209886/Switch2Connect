"""Simplified Chinese display strings. Internal config tokens stay in English."""
import re
import tkinter as tk
from tkinter import ttk

TRANSLATIONS = {"'figure 8'": '“8 字形”',
 '6-Axis': '六轴',
 '9-Axis': '九轴',
 '9-axis Assist:': '九轴辅助：',
 'A button to SELECT': '按 A 键选择',
 'Absolute': '按总连接时长',
 'Activation:': '激活方式：',
 'Adaptive Triggers:': '自适应扳机：',
 'Add': '添加',
 'Administrator approval is required for driver changes.': '更改驱动需要管理员授权。',
 'Analog Trigger 100%:': '模拟扳机满行程：',
 'Applying...': '正在应用…',
 'Assign Current Profile To Apps': '将当前配置档分配给应用',
 'Assigned Apps': '已分配的应用',
 'Audio Haptics Settings': '音频触觉设置',
 'Audio Haptics:': '音频触觉：',
 'Auto': '自动',
 'Auto Disconnect': '自动断开连接',
 'Auto Disconnect:': '自动断开：',
 'Auto mode reduces idle CPU power use by requesting precision timing only while it is needed.\n\nButtons, sticks, triggers and motion controls remain fully enabled.\n\nHD Rumble, Audio Haptics and Impulse Trigger feedback may be less consistent, delayed, interrupted or occasionally lost.': '自动模式只在需要时请求高精度计时，以降低空闲时的 '
                                                                                                                                                                                                                                                                                                    'CPU '
                                                                                                                                                                                                                                                                                                    '功耗。\n'
                                                                                                                                                                                                                                                                                                    '\n'
                                                                                                                                                                                                                                                                                                    '按键、摇杆、扳机和体感控制仍可正常使用。\n'
                                                                                                                                                                                                                                                                                                    '\n'
                                                                                                                                                                                                                                                                                                    'HD '
                                                                                                                                                                                                                                                                                                    '震动、音频触觉和扳机震动反馈可能不稳定、延迟、中断或偶尔丢失。',
 'Auto Scan: {…}': '自动扫描：{…}',
 'B button to CANCEL': '按 B 键取消',
 'Before Click': '按到卡点前',
 'Boot': '引导模式',
 'Both Dampening': '双扳机缓冲',
 'Calibrate Gyro': '校准陀螺仪',
 'Calibrate Mag (Mag Cal): Move controller in a': '校准磁力计（Mag Cal）：校准时按“8 字形”移动手柄',
 'Calibrating 1..': '校准中 1…',
 'Calibrating 2..': '校准中 2…',
 'Calibrating 3..': '校准中 3…',
 'Calibrating 4..': '校准中 4…',
 'Calibrating 5..': '校准中 5…',
 'Calibration': '校准',
 'Calibration Done': '校准完成',
 'Cancel': '取消',
 'Capture': '截图键',
 'CH343/COM not detected': '未检测到 CH343/COM',
 'Change Profile': '切换配置档',
 'Change Profile List': '配置档列表',
 'Change Profile To': '切换到此配置档',
 'Chat': '聊天键',
 'Choose a .yaml File': '选择 YAML 文件',
 'Choose App': '选择应用',
 'Choose Export Location': '选择导出位置',
 'Close': '关闭',
 'Connecting Via: System BLE  |  Status: Ready': '连接方式：系统蓝牙 LE ｜ 状态：就绪',
 'Connecting Via: {…}  |  Status: {…}': '连接方式：{…} ｜ 状态：{…}',
 'Controller:': '控制器：',
 'Copy From Controller Mapping': '从控制器映射复制',
 'Could not enter flashing mode.\n\nTo enter Boot mode manually:\n  1. Hold the BOOT button\n  2. Tap RESET once, then release BOOT\n  3. Click Repair to retry\n\nDetails logged to:\n{…}': '无法进入烧录模式。\n'
                                                                                                                                                                                             '\n'
                                                                                                                                                                                             '手动进入引导模式：\n'
                                                                                                                                                                                             '  '
                                                                                                                                                                                             '1. '
                                                                                                                                                                                             '按住 '
                                                                                                                                                                                             'BOOT '
                                                                                                                                                                                             '键\n'
                                                                                                                                                                                             '  '
                                                                                                                                                                                             '2. '
                                                                                                                                                                                             '按一下 '
                                                                                                                                                                                             'RESET '
                                                                                                                                                                                             '键，再松开 '
                                                                                                                                                                                             'BOOT '
                                                                                                                                                                                             '键\n'
                                                                                                                                                                                             '  '
                                                                                                                                                                                             '3. '
                                                                                                                                                                                             '点击“修复”重试\n'
                                                                                                                                                                                             '\n'
                                                                                                                                                                                             '详细日志位置：\n'
                                                                                                                                                                                             '{…}',
 'Could not find the ESP32-S3 N16R8 CH343/COM flashing port.\nConnect the flashing Type-C/CH343P port and try again.': '未找到 '
                                                                                                                       'ESP32-S3 '
                                                                                                                       'N16R8 '
                                                                                                                       '的 '
                                                                                                                       'CH343/COM '
                                                                                                                       '烧录端口。\n'
                                                                                                                       '连接烧录用 '
                                                                                                                       'Type-C/CH343P '
                                                                                                                       '端口后重试。',
 'Custom': '自定义',
 'Day': '天',
 'Deadzone:': '死区：',
 'Default': '默认',
 'Delay:': '延迟：',
 'Delete': '删除',
 'Deleting ESP32-S3 N16R8 Firmware': '正在删除 ESP32-S3 N16R8 固件',
 'Detected, waiting for status': '已检测到，等待状态更新',
 'Disable HidHide': '关闭 HidHide',
 'Disconnect': '断开连接',
 'Disconnect after:': '满足条件后断开：',
 'DJG': '双 Joy-Con 陀螺仪（DJG）',
 'DJG:': '双 Joy-Con 陀螺仪：',
 'Do not show again': '不再提示',
 'Do not show again.': '不再提示。',
 'Dominant Side:': '主导侧：',
 'Done': '完成',
 'DOWN': '下',
 'Downloading {…} driver...': '正在下载 {…} 驱动…',
 'Dpad Down': '十字键下',
 'Dpad Left': '十字键左',
 'Dpad Right': '十字键右',
 'Dpad Up': '十字键上',
 'Driver Installation': '正在安装驱动',
 'Driver Uninstallation': '正在卸载驱动',
 'Driver:': '驱动：',
 'Dual Joy-con Gyro (DJG)': '双 Joy-Con 陀螺仪（DJG）',
 'Dynamic Frequency:': '动态频率：',
 'Emu Mode:': '模拟模式：',
 'Enable HidHide': '启用 HidHide',
 'Erase ESP32-S3 N16R8 firmware?': '要清除 ESP32-S3 N16R8 固件吗？',
 'Error': '错误',
 'ESP32 is not in Boot mode — firmware cannot be installed.\n\nTo enter Boot mode:\n  1. Hold the BOOT button\n  2. Tap RESET once, then release BOOT\n  3. Wait for Status to show "Boot", then click Install': 'ESP32 '
                                                                                                                                                                                                                 '未进入引导模式，无法安装固件。\n'
                                                                                                                                                                                                                 '\n'
                                                                                                                                                                                                                 '进入引导模式：\n'
                                                                                                                                                                                                                 '  '
                                                                                                                                                                                                                 '1. '
                                                                                                                                                                                                                 '按住 '
                                                                                                                                                                                                                 'BOOT '
                                                                                                                                                                                                                 '键\n'
                                                                                                                                                                                                                 '  '
                                                                                                                                                                                                                 '2. '
                                                                                                                                                                                                                 '按一下 '
                                                                                                                                                                                                                 'RESET '
                                                                                                                                                                                                                 '键，再松开 '
                                                                                                                                                                                                                 'BOOT '
                                                                                                                                                                                                                 '键\n'
                                                                                                                                                                                                                 '  '
                                                                                                                                                                                                                 '3. '
                                                                                                                                                                                                                 '等待状态显示“Boot”，然后点击“安装”',
 'ESP32-S3 is connected via OTG / native USB.\n\nFirmware cannot be flashed automatically on this port.\n\nTo install firmware, please:\n  1. Hold the BOOT button on the ESP32-S3 board\n  2. Tap the RESET button once, then release BOOT\n  3. Connect the CH343P / UART Type-C port and retry.': 'ESP32-S3 '
                                                                                                                                                                                                                                                                                                     '已通过 '
                                                                                                                                                                                                                                                                                                     'OTG／原生 '
                                                                                                                                                                                                                                                                                                     'USB '
                                                                                                                                                                                                                                                                                                     '连接。\n'
                                                                                                                                                                                                                                                                                                     '\n'
                                                                                                                                                                                                                                                                                                     '此端口无法自动烧录固件。\n'
                                                                                                                                                                                                                                                                                                     '\n'
                                                                                                                                                                                                                                                                                                     '请按以下步骤安装固件：\n'
                                                                                                                                                                                                                                                                                                     '  '
                                                                                                                                                                                                                                                                                                     '1. '
                                                                                                                                                                                                                                                                                                     '按住 '
                                                                                                                                                                                                                                                                                                     'ESP32-S3 '
                                                                                                                                                                                                                                                                                                     '开发板的 '
                                                                                                                                                                                                                                                                                                     'BOOT '
                                                                                                                                                                                                                                                                                                     '键\n'
                                                                                                                                                                                                                                                                                                     '  '
                                                                                                                                                                                                                                                                                                     '2. '
                                                                                                                                                                                                                                                                                                     '按一下 '
                                                                                                                                                                                                                                                                                                     'RESET '
                                                                                                                                                                                                                                                                                                     '键，再松开 '
                                                                                                                                                                                                                                                                                                     'BOOT '
                                                                                                                                                                                                                                                                                                     '键\n'
                                                                                                                                                                                                                                                                                                     '  '
                                                                                                                                                                                                                                                                                                     '3. '
                                                                                                                                                                                                                                                                                                     '连接 '
                                                                                                                                                                                                                                                                                                     'CH343P／UART '
                                                                                                                                                                                                                                                                                                     'Type-C '
                                                                                                                                                                                                                                                                                                     '端口后重试。',
 'ESP32-S3 N16R8 Driver': 'ESP32-S3 N16R8 驱动',
 'ESP32-S3 N16R8 Firmware': 'ESP32-S3 N16R8 固件',
 'ESP32-S3 N16R8 firmware installed successfully.\n\nPlease replug the ESP32-S3 USB cable (unplug then reinsert) to complete initialization and avoid port conflicts.': 'ESP32-S3 '
                                                                                                                                                                        'N16R8 '
                                                                                                                                                                        '固件安装成功。\n'
                                                                                                                                                                        '\n'
                                                                                                                                                                        '请拔下并重新插入 '
                                                                                                                                                                        'ESP32-S3 '
                                                                                                                                                                        'USB '
                                                                                                                                                                        '线，以完成初始化并避免端口冲突。',
 'ESP32-S3 N16R8 firmware operation failed:\n{…}': 'ESP32-S3 N16R8 固件操作失败：\n{…}',
 'ESP32-S3 N16R8 firmware uninstalled successfully.': 'ESP32-S3 N16R8 固件卸载成功。',
 'ESP32-S3: Update Available': 'ESP32-S3：有可用更新',
 'Exit': '退出',
 'Export': '导出',
 'Export Recorded File': '导出录制文件',
 'Exported: {…}\nTemporary recording removed.': '已导出：{…}\n临时录制文件已移除。',
 'Finalizing USBIP-win2 Driver installation...': '正在完成 USBIP-win2 驱动安装…',
 'Finish': '完成',
 'Firmware auto-updated. Please replug the ESP32-S3 USB cable.': '固件已自动更新。请拔下并重新插入 ESP32-S3 USB 线。',
 'Flashing Port:': '烧录端口：',
 'Frequency:': '频率：',
 'Full': '完全节能',
 'Fully Clicked': '已按到底',
 'Fully press the LEFT trigger all the way down past the click.\nWhile holding it down, click Next.': '将左扳机完全按到底，越过卡点。\n'
                                                                                                      '保持按住，然后点击“下一步”。',
 'Fully press the RIGHT trigger all the way down past the click.\nWhile holding it down, click Finish.': '将右扳机完全按到底，越过卡点。\n'
                                                                                                         '保持按住，然后点击“完成”。',
 'Game Bar': '游戏栏',
 'GameCube Controller:': 'GameCube 控制器：',
 'GameCube Trigger Calibration': 'GameCube 扳机校准',
 'GameCube Trigger Calibration saved successfully!': 'GameCube 扳机校准已保存！',
 'General': '常规',
 'Gyro Control:': '陀螺仪控制：',
 'Gyro Lock': '锁定陀螺仪',
 'Gyro Pass-Through': '陀螺仪直通',
 'Hair Trigger': '轻触扳机',
 'HDR Toggle': '切换 HDR',
 'Hide to System Tray': '最小化到系统托盘',
 'HidHide (hides the physical controller from games)\nStatus: Installed\nFiltering: {…}': 'HidHide（对游戏隐藏实体手柄）\n'
                                                                                          '状态：已安装\n'
                                                                                          '过滤：{…}',
 'Hold': '按住',
 'Home': 'Home 键',
 'Horizon Lock:': '水平锁定：',
 'Hour': '小时',
 'Import': '导入',
 'Impulse Trigger Settings': '扳机震动设置',
 'Impulse Trigger:': '扳机震动：',
 'In-app Gyro': '应用内陀螺仪',
 'In-app Gyro Mode': '应用内陀螺仪模式',
 'Inactive': '无操作时',
 'Initializing': '正在初始化',
 'install': '安装',
 'Install ESP32-S3 Driver': '安装 ESP32-S3 驱动',
 'Install HidHide': '安装 HidHide',
 'Install USBIP Driver': '安装 USBIP 驱动',
 'Install ViGEmBus Driver': '安装 ViGEmBus 驱动',
 'Install WinUHid Driver': '安装 WinUHid 驱动',
 'Installed ({…})': '已安装（{…}）',
 'Installed ({…}, waiting for USB transport)': '已安装（{…}，等待 USB 传输）',
 'Installing': '正在安装',
 'Installing ESP32-S3 N16R8 Firmware': '正在安装 ESP32-S3 N16R8 固件',
 'Installing USBIP-win2 Driver...\nPlease authorize the UAC prompt if asked.': '正在安装 USBIP-win2 驱动…\n'
                                                                               '如出现 UAC 提示，请批准管理员授权。',
 'Installing ViGEmBus driver...\nPlease authorize the UAC prompt if asked.': '正在安装 ViGEmBus 驱动…\n'
                                                                             '如出现 UAC 提示，请批准管理员授权。',
 'Installing WinUHid Driver...\nPlease authorize the UAC prompt if asked.': '正在安装 WinUHid 驱动…\n'
                                                                            '如出现 UAC 提示，请批准管理员授权。',
 'IR Mouse': '红外鼠标',
 'Joy-con IR Sensor:': 'Joy-Con 红外传感器：',
 'Joy-con Rail Buttons:': 'Joy-Con 导轨按键：',
 'Joystick Deadzone Settings': '摇杆死区设置',
 'Joysticks Cal': '摇杆校准',
 'Joysticks Calibration': '摇杆校准',
 'Joysticks calibration done.': '摇杆校准完成。',
 'KB Arrow Keys': '键盘方向键',
 'Keep controller stationary\nbefore calibrating.': '校准前请将控制器静置。',
 'Keyboard: {…}': '键盘：{…}',
 'L Gyro': '左侧陀螺仪',
 'L Joystick': '左摇杆',
 'L Joystick Click': '左摇杆按下',
 'L Joystick:': '左摇杆：',
 'L: 0 | R: 0': '左：0 ｜ 右：0',
 'L: {…} | R: {…}': '左：{…} ｜ 右：{…}',
 'Layout:': '布局：',
 'Left': '左',
 'LEFT': '左',
 'Legacy': '旧版',
 'Loading Ko-fi…': '正在加载 Ko-fi…',
 'm1 Left Click': '鼠标左键',
 'm2 Middle Click': '鼠标中键',
 'm3 Right Click': '鼠标右键',
 'm4 Backward': '鼠标后退键',
 'm5 Forward': '鼠标前进键',
 'Mag Cal': '校准磁力计',
 'Mag Tester': '磁力计测试',
 'Manual Scan': '手动扫描',
 'Media Keys': '媒体键',
 'Media Mute': '媒体静音',
 'Merge': '合并',
 'Minus': '减号键',
 'MINUS': '减号键',
 'Minute': '分钟',
 'Mode Shift': '模式切换',
 'Mode Shift:': '模式切换：',
 'Mode:': '模式：',
 'Mouse': '鼠标',
 'Mouse Click': '鼠标按键',
 'Mouse: {…}': '鼠标：{…}',
 'Mute': '静音',
 'Next': '下一步',
 'Next Track': '下一曲',
 'No NSO GameCube Controller is currently connected.': '当前未连接 NSO GameCube 控制器。',
 'No recording in this session.': '本次会话没有录制内容。',
 'None': '无',
 'Not Found': '未找到',
 'Not installed': '未安装',
 'OFF': '关',
 'Off': '关',
 'OK': '确定',
 'ON': '开',
 'On': '开',
 'On-Screen Keyboard': '屏幕键盘',
 'or': '或',
 'OTG Boot mode detected — ready to install firmware.': '已检测到 OTG 引导模式，可以安装固件。',
 'OTG port detected (firmware running). Please enter Boot mode first:\nHold BOOT, tap RESET once, release BOOT — then click Install.': '检测到 '
                                                                                                                                       'OTG '
                                                                                                                                       '端口（固件正在运行）。请先进入引导模式：\n'
                                                                                                                                       '按住 '
                                                                                                                                       'BOOT，按一下 '
                                                                                                                                       'RESET，再松开 '
                                                                                                                                       'BOOT，然后点击“安装”。',
 'pattern during calibration.': '校准期间保持该动作。',
 'Pending USB Connection': '等待 USB 连接',
 'Ping': '定位震动',
 'Play/Pause': '播放／暂停',
 'Please fully rotate both joysticks for 10 seconds each.': '请分别完整旋转两个摇杆，各持续 10 秒。',
 "Please release and don't touch the joysticks for 3 seconds.": '请松开摇杆，保持 3 秒不触碰。',
 'Plus': '加号键',
 'PLUS': '加号键',
 'Power Saving: {…}': '省电模式：{…}',
 'Press button of a paired controller, or hold sync button to pair': '按下已配对控制器的任意按键；如需配对，请按住同步键',
 'Press the LEFT trigger down just until you feel the click (bump).\nHold it there and click Next.': '将左扳机按至刚感觉到卡点。\n'
                                                                                                     '保持按住，然后点击“下一步”。',
 'Press the RIGHT trigger down just until you feel the click (bump).\nHold it there and click Next.': '将右扳机按至刚感觉到卡点。\n'
                                                                                                      '保持按住，然后点击“下一步”。',
 'Press {…} Layout': '切换为 {…} 布局',
 'Previous Track': '上一曲',
 'Print Screen': '打印屏幕',
 'Pro Controller Back Buttons:': 'Pro 控制器背键：',
 'Profile Name': '配置档名称',
 'Profile Switching Combo': '配置档切换组合键',
 'Profile Switching Combo Trigger:': '配置档切换组合键触发方式：',
 'Profile:': '配置档：',
 'PrtSc': '截图键（PrtSc）',
 'PS Input': 'PS 输入',
 'PS Mute': 'PS 静音',
 'R Gyro': '右侧陀螺仪',
 'R Joystick': '右摇杆',
 'R Joystick Click': '右摇杆按下',
 'R Joystick:': '右摇杆：',
 'Raw Input': '原始输入',
 'Ready': '就绪',
 'Real-time Indicators': '实时指示',
 'Recorded: {…}': '已录制：{…}',
 'Recording did not create a file.': '录制未生成文件。',
 'Recording error: {…}': '录制出错：{…}',
 'Recording...': '正在录制…',
 'Recording: {…}': '正在录制：{…}',
 'Refresh': '刷新',
 'Release both triggers completely and wait a moment.\nThen click Next.': '完全松开两个扳机，稍等片刻。\n然后点击“下一步”。',
 'Rename': '重命名',
 'Repair USBIP Driver': '修复 USBIP 驱动',
 'Repair ViGEmBus Driver': '修复 ViGEmBus 驱动',
 'Repair WinUHid Driver': '修复 WinUHid 驱动',
 'Repairing ESP32-S3 N16R8 Firmware': '正在修复 ESP32-S3 N16R8 固件',
 'Reset': '重置',
 'Restart Required': '需要重启',
 'RIGHT': '右',
 'Right': '右',
 'Rumble Mode:': '震动模式：',
 'Run At Startup: {…}': '开机启动：{…}',
 'Running USBIP-win2 Uninstaller...\nPlease authorize the UAC prompt if asked.': '正在运行 USBIP-win2 卸载程序…\n'
                                                                                 '如出现 UAC 提示，请批准管理员授权。',
 'Scroll Wheel': '滚轮',
 'Scroll Wheel Mode:': '滚轮模式：',
 'Select & Change Profile:': '选择并切换配置档：',
 'Sensitivity:': '灵敏度：',
 'Shadow': 'Shadow（影子）',
 'Shared Buttons & Joysticks': '共用按键和摇杆',
 'Show': '显示窗口',
 'Single Side Toggle': '单侧切换',
 'Split': '拆分',
 'Start Minimized: {…}': '启动时最小化：{…}',
 'Start Recording': '开始录制',
 'Starting in 1..': '1 秒后开始…',
 'Starting in 2..': '2 秒后开始…',
 'Starting in 3..': '3 秒后开始…',
 'Steering': '方向盘',
 'Step 1: Base State': '步骤 1：初始状态',
 'Step 2: Left Trigger (Bump)': '步骤 2：左扳机卡点',
 'Step 3: Left Trigger (Max)': '步骤 3：左扳机最大行程',
 'Step 4: Right Trigger (Bump)': '步骤 4：右扳机卡点',
 'Step 5: Right Trigger (Max)': '步骤 5：右扳机最大行程',
 'Stick Assist:': '摇杆辅助：',
 'Stop': '停止',
 'Stop Cal': '停止校准',
 'Stop Recording': '停止录制',
 'Strength:': '强度：',
 'Success': '成功',
 'successfully.': '成功。',
 'Switch Dominant Side': '切换主导侧',
 'Switch Gyro Side': '切换陀螺仪侧',
 'Switch Input': 'Switch 输入',
 'Switch1': 'Switch 1',
 'Switch2': 'Switch 2',
 'Sys Manager': '任务管理器',
 'System BLE': '系统蓝牙 LE',
 'Tap': '轻按',
 'Task Manager': '任务管理器',
 'to': '至',
 'Toggle': '切换',
 'Trackpad Center Click': '触控板中键点击',
 'Trackpad L Touch': '触控板左侧触摸',
 'Trackpad R Touch': '触控板右侧触摸',
 'Trigger Calibration': '扳机校准',
 'UI Scaling:': '界面缩放：',
 'uninstall': '卸载',
 'Uninstall HidHide': '卸载 HidHide',
 'Uninstall USBIP Driver': '卸载 USBIP 驱动',
 'Uninstall ViGEmBus Driver': '卸载 ViGEmBus 驱动',
 'Uninstall WinUHid and remove its trusted driver certificate?\n\nAdministrator approval is required.': '卸载 '
                                                                                                        'WinUHid '
                                                                                                        '驱动并移除其受信任驱动证书？\n'
                                                                                                        '\n'
                                                                                                        '此操作需要管理员授权。',
 'Uninstall WinUHid Driver': '卸载 WinUHid 驱动',
 'Uninstalling': '正在卸载',
 'Uninstalling ViGEmBus Driver...\nPlease authorize the UAC prompt if asked.': '正在卸载 ViGEmBus 驱动…\n'
                                                                               '如出现 UAC 提示，请批准管理员授权。',
 'Uninstalling WinUHid Driver...\nPlease authorize the UAC prompt if asked.': '正在卸载 WinUHid 驱动…\n'
                                                                              '如出现 UAC 提示，请批准管理员授权。',
 'Update required ({…} -> {…})': '需要更新（{…} → {…}）',
 'USB Connected': '已连接 USB',
 'USBIP Driver Installation': '正在安装 USBIP 驱动',
 'USBIP Driver Uninstallation': '正在卸载 USBIP 驱动',
 'ViGEmBus Uninstallation': '正在卸载 ViGEmBus',
 'Volume Down': '降低音量',
 'Volume Up': '提高音量',
 'Waiting for controller data': '等待控制器数据',
 'WinUHid driver is not installed.\n\nDo you want to install it now?\n(Requires administrator privileges.)': '未安装 '
                                                                                                             'WinUHid '
                                                                                                             '驱动。\n'
                                                                                                             '\n'
                                                                                                             '现在安装吗？\n'
                                                                                                             '（需要管理员权限。）',
 'WinUHid Driver Manager': 'WinUHid 驱动管理器',
 'WinUHid Driver...\nPlease authorize the UAC prompt if asked.': 'WinUHid 驱动…\n如出现 UAC 提示，请批准管理员授权。',
 'WinUHid Driver: Installed and Ready': 'WinUHid 驱动：已安装，可以使用',
 'WinUHid Driver: Not Installed': 'WinUHid 驱动：未安装',
 'WinUHid Driver: Repair Required': 'WinUHid 驱动：需要修复',
 'WinUHid is only partially installed and cannot be used reliably.\n\n{…}\n\nDo you want to clean up and reinstall it now?\n(Requires administrator privileges.)': 'WinUHid '
                                                                                                                                                                   '仅安装了一部分，无法可靠使用。\n'
                                                                                                                                                                   '\n'
                                                                                                                                                                   '{…}\n'
                                                                                                                                                                   '\n'
                                                                                                                                                                   '现在清理并重新安装吗？\n'
                                                                                                                                                                   '（需要管理员权限。）',
 'WinUHid operation failed.': 'WinUHid 操作失败。',
 'WinUHid will install a virtual HID driver and add its driver certificate to the Windows trusted stores.\n\nAdministrator approval is required.\n\nContinue?': 'WinUHid '
                                                                                                                                                                '将安装虚拟 '
                                                                                                                                                                'HID '
                                                                                                                                                                '驱动，并将其驱动证书加入 '
                                                                                                                                                                'Windows '
                                                                                                                                                                '受信任证书存储。\n'
                                                                                                                                                                '\n'
                                                                                                                                                                '此操作需要管理员授权。\n'
                                                                                                                                                                '\n'
                                                                                                                                                                '是否继续？',
 'World': '世界坐标',
 'Yaw': '偏航',
 'ZL Dampening': 'ZL 扳机缓冲',
 'ZR Dampening': 'ZR 扳机缓冲',
 '{…}\nFirmware: {…}': '{…}\n固件：{…}',
 '{…} / bias age {…} s / transient {…} deg': '{…} / 偏置已存在 {…} 秒 / 瞬态 {…} 度',
 '{…} / {…} / {…} dps ({…} samples)': '{…} / {…} / {…} 度/秒（{…} 个样本）',
 '{…} / {…} | {…} / {…} deg': '{…} / {…} ｜ {…} / {…} 度',
 '{…} / {…} | {…} / {…} deg (Transient)': '{…} / {…} ｜ {…} / {…} 度（瞬态）',
 '{…} deg / {…}': '{…} 度 / {…}',
 "{…} detected.\n\nHidHide hides the controller's physical HID so games only see the virtual controller (no double input).\n\nInstall it now?\n(Requires administrator privileges.)": '检测到 '
                                                                                                                                                                                      '{…}。\n'
                                                                                                                                                                                      '\n'
                                                                                                                                                                                      'HidHide '
                                                                                                                                                                                      '会向游戏隐藏实体控制器的 '
                                                                                                                                                                                      'HID '
                                                                                                                                                                                      '设备，使游戏只识别虚拟控制器（避免重复输入）。\n'
                                                                                                                                                                                      '\n'
                                                                                                                                                                                      '现在安装吗？\n'
                                                                                                                                                                                      '（需要管理员权限。）',
 '{…} dps / {…}': '{…} 度/秒 / {…}',
 '{…} Driver': '{…} 驱动',
 '{…} Joy-con: {…}': '{…} Joy-Con：{…}',
 '{…} {…} Driver': '{…} {…} 驱动',
 '{…}: {…} firmware on {…}...': '{…}：正在 {…} {…} 上的固件…'}
TRANSLATIONS.update({
    "Always Active:": "始终启用：",
    "SDL3 Native": "SDL3 原生",
    "Bluetooth not responding": "蓝牙无响应",
    (
        "The controller was removed, but Windows Bluetooth stopped responding.\n\n"
        "Automatic Bluetooth reconnection is paused so the adapter is not stressed further.\n\n"
        "If Bluetooth settings are missing or Device Manager shows unknown USB devices:\n"
        "1. Shut down the PC.\n"
        "2. Switch off the power supply (or unplug it) for about a minute.\n"
        "3. Start the PC again.\n\n"
        "Installing the latest Bluetooth driver from the chip vendor may also help."
    ): (
        "手柄已移除，但 Windows 蓝牙停止响应。\n\n"
        "已暂停自动重新连接蓝牙设备，以免加重适配器负担。\n\n"
        "如果蓝牙设置消失，或设备管理器显示未知 USB 设备，请尝试以下步骤：\n"
        "1. 关闭电脑。\n"
        "2. 关闭电源开关或拔下电源线，等待约一分钟。\n"
        "3. 重新启动电脑。\n\n"
        "安装蓝牙芯片厂商提供的最新驱动也可能解决问题。"
    ),
    (
        "The USBIP uninstaller and bundled recovery script are missing. "
        "Please restore the application files, then retry Repair USBIP Driver."
    ): "找不到 USBIP 卸载程序和附带的恢复脚本。请恢复应用文件，再重试修复 USBIP 驱动。",
    "Recovering incomplete USBIP installation...\nPlease authorize the UAC prompt if asked.":
        "正在恢复未完成的 USBIP 安装…\n如果出现 UAC 提示，请授权。",
    "USBIP uninstallation failed.\n\nExit code: {…}\nRecovery log: {…}":
        "USBIP 卸载失败。\n\n退出代码：{…}\n恢复日志：{…}",
    "USBIP uninstallation failed.\n\nExit code: {…}": "USBIP 卸载失败。\n\n退出代码：{…}",
    "USBIP removal started. A restart is required to complete the uninstall.":
        "已开始移除 USBIP。请重启电脑以完成卸载。",
    "A restart is required to finish removing USBIP.\n\nRestart now?":
        "需要重启电脑才能完成 USBIP 卸载。\n\n现在重启吗？",
    "Failed to start the USBIP installer: {…}": "无法启动 USBIP 安装程序：{…}",
    "Failed to start the USBIP uninstaller: {…}": "无法启动 USBIP 卸载程序：{…}",
    "USBIP driver installation was cancelled or failed to start (UAC prompt declined).":
        "USBIP 驱动安装已取消，或因未授权 UAC 而无法启动。",
    "USBIP driver uninstallation was cancelled or failed to start (UAC prompt declined).":
        "USBIP 驱动卸载已取消，或因未授权 UAC 而无法启动。",
    "Are you sure you want to uninstall the USBIP driver?\n(Requires administrator privileges.)":
        "确定要卸载 USBIP 驱动吗？\n（需要管理员权限。）",
    "USBIP-win2 driver installed successfully.": "USBIP-win2 驱动安装成功。",
    "ViGEmBus Connection Error": "ViGEmBus 连接错误",
    "ViGEmBus files and device are present, but the runtime bus connection failed.\n\n{…}\n\nUse Repair ViGEmBus Driver to cleanly reinstall it.":
        "已找到 ViGEmBus 文件和设备，但连接总线失败。\n\n{…}\n\n请使用“修复 ViGEmBus 驱动”清理并重新安装。",
    "Could not find the bundled ViGEmBus installer. Please verify the application files.":
        "找不到附带的 ViGEmBus 安装程序。请检查应用文件。",
    "ViGEmBus install was cancelled or failed to start (UAC prompt declined).":
        "ViGEmBus 安装已取消，或因未授权 UAC 而无法启动。",
    "ViGEmBus installation was not completed. A system restart may be required; please try again if the issue persists.":
        "ViGEmBus 安装未完成，可能需要重启电脑。如果问题仍然存在，请重试。",
    "ViGEmBus driver installed successfully.": "ViGEmBus 驱动安装成功。",
    "Are you sure you want to uninstall the ViGEmBus driver?\n(Requires administrator privileges.)":
        "确定要卸载 ViGEmBus 驱动吗？\n（需要管理员权限。）",
    "ViGEmBus uninstallation was cancelled or failed to start (UAC prompt declined).":
        "ViGEmBus 卸载已取消，或因未授权 UAC 而无法启动。",
    "ViGEmBus driver uninstalled successfully. A system reboot is highly recommended.":
        "ViGEmBus 驱动卸载成功。建议重启电脑。",
    "Unavailable": "不可用",
    "WinUHid Driver Mode is not available in the Microsoft Store version.":
        "Microsoft Store 版本无法使用 WinUHid 驱动模式。",
    "WinUHid driver installed successfully.": "WinUHid 驱动安装成功。",
    "WinUHid driver uninstalled successfully.": "WinUHid 驱动卸载成功。",
    "Uninstall WinUHid and use Win32 API output until it is reinstalled?\n(Requires administrator privileges.)":
        "卸载 WinUHid，并在重新安装前使用 Win32 API 输出吗？\n（需要管理员权限。）",
    "Driver installation was cancelled or failed to start (UAC prompt declined).":
        "驱动安装已取消，或因未授权 UAC 而无法启动。",
    "Driver uninstallation was cancelled or failed to start (UAC prompt declined).":
        "驱动卸载已取消，或因未授权 UAC 而无法启动。",
    "Could not find {…}. Please verify the integrity of the application files.":
        "找不到 {…}。请检查应用文件是否完整。",
    "Unknown driver: {…}": "未知驱动：{…}",
    "Download Error": "下载失败",
    "Keyboard Raw Input Error": "键盘原始输入错误",
    "The WinUHid driver is present, but the virtual keyboard could not be created. Keyboard output remains Standard.":
        "已找到 WinUHid 驱动，但无法创建虚拟键盘。键盘输出将保持为标准模式。",
    "HidHide installed successfully.": "HidHide 安装成功。",
    "HidHide removal started. A restart is required to complete the uninstall.":
        "已开始移除 HidHide。请重启电脑以完成卸载。",
    "A restart is required to finish removing HidHide.\n\nRestart now?":
        "需要重启电脑才能完成 HidHide 卸载。\n\n现在重启吗？",
    "A restart is required to finish HidHide setup and hide the physical controller.\n\nRestart now?":
        "需要重启电脑才能完成 HidHide 设置并隐藏实体手柄。\n\n现在重启吗？",
    "HidHide operation was cancelled (UAC prompt declined).": "HidHide 操作已取消（未授权 UAC）。",
    "Uninstall the HidHide driver?\n(Requires administrator privileges.)":
        "卸载 HidHide 驱动吗？\n（需要管理员权限。）",
    "HidHide hides the controller's physical HID so games only see the virtual controller (no double input). Install it now?\n(Optional. Requires administrator privileges.)":
        "HidHide 会隐藏实体手柄的 HID 设备，使游戏只识别虚拟手柄，避免重复输入。现在安装吗？\n（可选，需要管理员权限。）",
    "{…} detected.\n\nHidHide hides the physical controller's HID so games only see the virtual controller. Install it now?\n(Requires administrator privileges.)":
        "检测到 {…}。\n\nHidHide 会隐藏实体手柄的 HID 设备，使游戏只识别虚拟手柄。现在安装吗？\n（需要管理员权限。）",
    "Failed to apply HidHide setting.\n\nPlease make sure 'HidHide Configuration Client' is CLOSED.":
        "无法应用 HidHide 设置。\n\n请确认已关闭 HidHide 配置客户端。",
    "Could not restart automatically: {…}\nPlease restart manually.": "无法自动重启：{…}\n请手动重启。",
    "Unable to start recording. Check the console log for details.": "无法开始录制。请查看控制台日志。",
    "No completed recording is available.": "没有已完成的录制。",
    "Reset Profile": "重置配置档",
    "Delete Profile": "删除配置档",
    "Cannot delete the last profile.": "无法删除最后一个配置档。",
    "Are you sure you want to reset profile '{…}'?": "确定要重置配置档“{…}”吗？",
    "Are you sure you want to delete profile '{…}'?": "确定要删除配置档“{…}”吗？",
    "Profile '{…}' already exists.": "配置档“{…}”已存在。",
    "This file is not a valid config file.": "这不是有效的配置文件。",
    "This file contains nothing to import.": "此文件中没有可导入的内容。",
    "Failed to read the file:\n{…}": "无法读取文件：\n{…}",
    "Failed to write the config file:\n{…}": "无法写入配置文件：\n{…}",
    "Failed to export:\n{…}": "导出失败：\n{…}",
    "Export failed: {…}": "导出失败：{…}",
})

_EXACT = {k: v for k, v in TRANSLATIONS.items() if "{…}" not in k}
_TEMPLATES = []
for source, target in sorted(TRANSLATIONS.items(), key=lambda pair: len(pair[0]), reverse=True):
    if "{…}" in source:
        regex = re.compile("(.+?)".join(re.escape(part) for part in source.split("{…}")), re.DOTALL)
        _TEMPLATES.append((regex, target))

def tr(value):
    if not isinstance(value, str):
        return value
    if value in _EXACT:
        return _EXACT[value]
    stripped = value.strip()
    if stripped != value:
        localized = tr(stripped)
        if localized == stripped:
            return value
        start = len(value) - len(value.lstrip())
        end = len(value.rstrip())
        return value[:start] + localized + value[end:]
    for regex, target in _TEMPLATES:
        match = regex.fullmatch(value)
        if match:
            translated = target
            for part in match.groups():
                translated = translated.replace("{…}", tr(part), 1)
            return translated
    return value

class LocalizedStringVar(tk.StringVar):
    """Keep a raw value for callers while a Tk variable displays its translation."""
    def __init__(self, *args, choices=(), value=None, **kw):
        self._display_to_raw = {tr(raw): raw for raw in choices}
        super().__init__(*args, value=tr(value), **kw)

    def get(self):
        visible = super().get()
        return self._display_to_raw.get(visible, visible)

    def set(self, value):
        super().set(tr(value))

class LocalizedCombobox(ttk.Combobox):
    """Translate visible options while get()/set() retain existing config tokens."""
    def __init__(self, master=None, **kw):
        self._raw_values = ()
        raw = kw.pop("values", ())
        kw["values"] = self._translated_values(raw)
        super().__init__(master, **kw)

    def _translated_values(self, raw):
        self._raw_values = tuple(raw)
        return tuple(tr(value) for value in self._raw_values)

    def configure(self, cnf=None, **kw):
        if isinstance(cnf, dict) and "values" in cnf:
            cnf = {**cnf, "values": self._translated_values(cnf["values"])}
        if "values" in kw:
            kw["values"] = self._translated_values(kw["values"])
        return super().configure(cnf, **kw)

    config = configure

    def get(self):
        visible = super().get()
        for raw in self._raw_values:
            if visible == tr(raw):
                return raw
        return visible

    def set(self, value):
        super().set(tr(value))
