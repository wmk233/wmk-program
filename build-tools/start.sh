#!/bin/bash

# 水印工具启动脚本 (MacOS)

echo "水印工具启动脚本"
echo "=================="

# 检查Python是否已安装
if ! command -v python3 &> /dev/null
then
    echo "错误：未检测到Python，请先安装Python 3.7或更高版本"
    echo "可以通过以下方式安装："
    echo "  1. 访问 https://www.python.org/downloads/"
    echo "  2. 或使用 Homebrew: brew install python3"
    exit 1
fi

# 检查pip是否可用
if ! command -v pip3 &> /dev/null
then
    echo "错误：未检测到pip，请确保Python安装时包含了pip"
    exit 1
fi

# 检查依赖包
echo "正在检查依赖包..."
if ! pip3 show Pillow &> /dev/null
then
    echo "正在安装依赖包..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "错误：无法安装依赖包"
        exit 1
    fi
fi

echo "正在启动水印工具..."
python3 main.py