# 水印工具 (Watermark Tool)

一个用于给图片添加水印的桌面应用程序，支持Windows和macOS系统。

## 项目结构

```
watermark-app/
├── src/                    # 源代码目录
│   ├── main.py            # 主程序文件
│   └── requirements.txt   # 依赖包列表
├── docs/                  # 文档目录
│   ├── README.md          # 项目说明文档
│   ├── LICENSE            # 许可证文件
│   └── 其他文档文件
├── tests/                 # 测试目录
│   ├── test_watermark.py  # 水印功能测试
│   └── 其他测试文件
├── build-tools/           # 构建工具目录
│   ├── build_windows.bat  # Windows构建脚本
│   ├── start.bat          # 启动脚本
│   └── 其他构建相关文件
├── release/               # 发布目录
│   └── watermark-tool-windows-v1.0.0-chinese-fix.zip  # Windows可执行文件
└── .gitignore             # Git忽略文件
```

## 功能特点

- 支持文本水印和图片水印
- 支持中文水印文本（已解决乱码问题）
- 可调节水印大小、透明度、颜色和位置
- 支持批量处理图片
- 跨平台支持（Windows/macOS）
- 图形用户界面，操作简单

## 安装和使用

### 方法1：使用预编译的可执行文件（推荐）

1. 从[release](release/)目录下载`watermark-tool-windows-v1.0.0-chinese-fix.zip`
2. 解压缩文件
3. 运行`WatermarkTool.exe`

### 方法2：从源代码运行

1. 确保已安装Python 3.6+
2. 安装依赖包：
   ```
   pip install -r src/requirements.txt
   ```
3. 运行程序：
   ```
   python src/main.py
   ```

## 开发

### 构建可执行文件

Windows系统：
```
cd build-tools
build_windows.bat
```

## 测试

运行测试：
```
python tests/test_watermark.py
```

## 许可证

本项目采用MIT许可证，详见[LICENSE](docs/LICENSE)文件。