# 水印工具发布说明

## 版本信息
- 版本号: v1.0.0
- 发布日期: 2025-10-06
- 支持平台: Windows, MacOS

## 功能特性

### 核心功能
1. 图片导入支持
   - 单张图片导入（拖拽或文件选择器）
   - 批量导入（多选图片或导入整个文件夹）
   - 图片列表显示（缩略图和文件名）

2. 格式支持
   - 输入格式: JPEG, PNG, BMP, TIFF（PNG支持透明通道）
   - 输出格式: JPEG, PNG

3. 水印类型
   - 文本水印: 自定义文本、字体、颜色、透明度、阴影/描边效果
   - 图片水印: 本地图片选择、缩放、透明度调节

4. 水印布局控制
   - 预设位置: 九宫格布局（9个预设位置）
   - 手动拖拽: 鼠标拖拽精确定位
   - 实时预览: 所有调整实时显示效果

5. 导出功能
   - 自定义导出文件夹
   - 命名规则: 原文件名、前缀、后缀
   - 防覆盖机制: 禁止导出到原文件夹

6. 配置管理
   - 水印模板保存/加载
   - 模板管理（增删改查）
   - 自动加载上次设置

## 安装包内容

```
watermark-app/
├── main.py                 # 主程序文件
├── requirements.txt        # 依赖包列表
├── start.bat               # Windows启动脚本
├── start.sh                # MacOS启动脚本
├── README.md               # 使用说明
├── PYTHON_INSTALLATION.md  # Python安装指南
├── LICENSE                 # 开源许可证
├── .gitignore              # Git忽略文件
├── package.json            # 项目信息文件
└── test_watermark.py       # 测试脚本
```

## 安装和运行

### 系统要求
- Python 3.7 或更高版本
- Pillow 图像处理库

### 安装步骤

1. 确保系统已安装 Python 3.7+
2. 下载并解压发布包
3. Windows 用户双击 `start.bat` 运行
4. MacOS 用户在终端中运行 `./start.sh`

### 手动安装依赖
```bash
# Windows
pip install -r requirements.txt

# MacOS
pip3 install -r requirements.txt
```

### 运行程序
```bash
# Windows
python main.py

# MacOS
python3 main.py
```

## 开发者信息

### 项目结构说明
- 使用 Python 3 和 Tkinter 开发图形界面
- 使用 Pillow 库进行图像处理
- 配置文件以 JSON 格式存储
- 支持跨平台运行

### 打包为可执行文件
开发者可以使用 PyInstaller 将程序打包为独立的可执行文件：

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

## 更新日志

### v1.0.0 (2025-10-06)
- 初始版本发布
- 实现所有核心功能
- 支持 Windows 和 MacOS 平台
- 完善的用户界面和交互体验

## 技术支持

如在使用过程中遇到问题，请参考以下资源：
1. 查看 README.md 和 PYTHON_INSTALLATION.md 文件
2. 确保系统满足最低要求
3. 检查依赖包是否正确安装
4. 联系开发者获取技术支持