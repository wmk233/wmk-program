@echo off
title 水印工具

echo 水印工具启动脚本
echo ==================

REM 检查Python是否已安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误：未检测到Python，请先安装Python 3.7或更高版本
    echo 下载地址：https://www.python.org/downloads/
    pause
    exit /b 1
)

REM 检查pip是否可用
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误：未检测到pip，请确保Python安装时包含了pip
    pause
    exit /b 1
)

REM 检查依赖包
echo 正在检查依赖包...
pip show Pillow >nul 2>&1
if %errorlevel% neq 0 (
    echo 正在安装依赖包...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo 错误：无法安装依赖包
        pause
        exit /b 1
    )
)

echo 正在启动水印工具...
python main.py

pause