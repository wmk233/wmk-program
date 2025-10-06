#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
水印工具打包脚本
用于创建Windows和MacOS的可执行文件
"""

import os
import sys
import subprocess
import shutil

def install_pyinstaller():
    """安装PyInstaller"""
    print("正在安装PyInstaller...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✅ PyInstaller安装成功")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ PyInstaller安装失败: {e}")
        return False

def create_windows_release():
    """创建Windows版本"""
    print("正在创建Windows版本...")
    try:
        # 使用PyInstaller打包
        cmd = [
            sys.executable, "-m", "PyInstaller",
            "--onefile",           # 单文件
            "--windowed",          # 窗口模式（不显示控制台）
            "--name", "WatermarkTool",  # 应用名称
            "--icon", "icon.svg",       # 图标
            "main.py"              # 主程序
        ]
        
        subprocess.check_call(cmd)
        print("✅ Windows版本创建成功")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Windows版本创建失败: {e}")
        return False

def create_macos_release():
    """创建MacOS版本"""
    print("正在创建MacOS版本...")
    try:
        # 使用PyInstaller打包
        cmd = [
            sys.executable, "-m", "PyInstaller",
            "--onefile",           # 单文件
            "--windowed",          # 窗口模式（不显示控制台）
            "--name", "WatermarkTool",  # 应用名称
            "--icon", "icon.svg",       # 图标
            "main.py"              # 主程序
        ]
        
        subprocess.check_call(cmd)
        print("✅ MacOS版本创建成功")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ MacOS版本创建失败: {e}")
        return False

def package_release():
    """打包发布版本"""
    print("水印工具打包脚本")
    print("=" * 30)
    
    # 检查是否在正确目录
    if not os.path.exists("main.py"):
        print("❌ 请在项目根目录运行此脚本")
        return False
    
    # 安装PyInstaller
    if not install_pyinstaller():
        return False
    
    # 创建发布目录
    dist_dir = "release"
    if not os.path.exists(dist_dir):
        os.makedirs(dist_dir)
    
    # 创建Windows版本
    if create_windows_release():
        # 移动生成的可执行文件到发布目录
        if os.path.exists("dist/WatermarkTool.exe"):
            shutil.move("dist/WatermarkTool.exe", f"{dist_dir}/WatermarkTool-Windows.exe")
            print(f"✅ Windows可执行文件已移动到 {dist_dir} 目录")
    
    # 创建MacOS版本
    if sys.platform == "darwin":  # 仅在MacOS上创建
        if create_macos_release():
            # 移动生成的可执行文件到发布目录
            if os.path.exists("dist/WatermarkTool"):
                shutil.move("dist/WatermarkTool", f"{dist_dir}/WatermarkTool-MacOS")
                print(f"✅ MacOS可执行文件已移动到 {dist_dir} 目录")
    
    # 清理临时文件
    cleanup_files = ["build", "dist", "WatermarkTool.spec"]
    for file in cleanup_files:
        if os.path.exists(file):
            if os.path.isdir(file):
                shutil.rmtree(file)
            else:
                os.remove(file)
            print(f"🧹 已清理临时文件: {file}")
    
    print("\n🎉 打包完成！")
    print(f"📦 发布文件位于: {dist_dir}/")
    return True

if __name__ == "__main__":
    package_release()