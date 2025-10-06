# Python 安装指南

## Windows 系统安装 Python

1. 访问 Python 官方网站下载页面：
   https://www.python.org/downloads/windows/

2. 下载适用于 Windows 的最新 Python 版本（推荐 3.8 或更高版本）
   - 选择 "Windows installer (64-bit)" 或 "Windows installer (32-bit)"

3. 运行下载的安装程序：
   - **重要**：勾选 "Add Python to PATH" 选项
   - 选择 "Install Now" 进行标准安装

4. 验证安装：
   - 打开命令提示符（按 Win+R，输入 cmd，回车）
   - 输入以下命令并回车：
     ```
     python --version
     ```
   - 如果显示版本号，说明安装成功

## MacOS 系统安装 Python

### 方法一：使用官方安装包
1. 访问 Python 官方网站下载页面：
   https://www.python.org/downloads/macos/

2. 下载适用于 MacOS 的最新 Python 版本

3. 运行下载的 .pkg 文件并按照安装向导操作

4. 验证安装：
   - 打开终端（Terminal）
   - 输入以下命令并回车：
     ```
     python3 --version
     ```
   - 如果显示版本号，说明安装成功

### 方法二：使用 Homebrew（推荐）
1. 如果尚未安装 Homebrew，先安装：
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. 使用 Homebrew 安装 Python：
   ```
   brew install python3
   ```

## 安装完成后运行水印工具

1. 双击 `start.bat`（Windows）或运行 `start.sh`（MacOS）脚本
2. 或者手动运行：
   - Windows:
     ```
     pip install -r requirements.txt
     python main.py
     ```
   - MacOS:
     ```
     pip3 install -r requirements.txt
     python3 main.py
     ```

如果在安装过程中遇到任何问题，请参考官方文档或寻求技术支持。