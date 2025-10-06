@echo off
title 水印工具打包脚本

echo 水印工具打包脚本
echo ==================

REM 检查Python是否已安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误：未检测到Python，请先安装Python 3.7或更高版本
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

REM 检查PyInstaller是否已安装
pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo 正在安装PyInstaller...
    pip install pyinstaller
    if %errorlevel% neq 0 (
        echo 错误：无法安装PyInstaller
        pause
        exit /b 1
    )
)

echo 正在打包Windows版本...
pyinstaller --onefile --windowed --name WatermarkTool main.py

if %errorlevel% neq 0 (
    echo 错误：打包失败
    pause
    exit /b 1
)

echo.
echo 打包完成！
echo 可执行文件位于 dist\WatermarkTool.exe

REM 创建发布目录
if not exist release mkdir release

REM 复制可执行文件到发布目录
copy "dist\WatermarkTool.exe" "release\WatermarkTool-Windows.exe"

echo.
echo Windows版本已复制到 release\WatermarkTool-Windows.exe

REM 清理临时文件
echo.
echo 正在清理临时文件...
rmdir /s /q build
rmdir /s /q dist
del WatermarkTool.spec

echo 清理完成！

echo.
echo ==================
echo 打包过程已完成！
echo Windows可执行文件: release\WatermarkTool-Windows.exe
echo.
pause