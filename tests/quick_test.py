#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
简单功能验证脚本
用于快速验证水印工具的核心功能
"""

import sys
import os

# 添加src目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """测试必要的模块是否可以导入"""
    print("测试模块导入...")
    
    try:
        from PIL import Image, ImageDraw, ImageFont
        print("✓ PIL/Pillow 导入成功")
    except ImportError as e:
        print(f"✗ PIL/Pillow 导入失败: {e}")
        return False
        
    try:
        import tkinter as tk
        print("✓ tkinter 导入成功")
    except ImportError as e:
        print(f"✗ tkinter 导入失败: {e}")
        return False
        
    return True

def test_chinese_font_function():
    """测试中文字体函数"""
    print("\n测试中文字体函数...")
    
    try:
        # 从主程序导入中文字体函数
        sys.path.insert(0, 'src')
        from main import get_chinese_font
        
        # 测试获取中文字体
        font = get_chinese_font(24)
        print(f"✓ 成功获取中文字体: {font}")
        return True
    except Exception as e:
        print(f"✗ 获取中文字体失败: {e}")
        return False

def test_main_app():
    """测试主应用程序是否可以导入"""
    print("\n测试主应用程序...")
    
    try:
        sys.path.insert(0, 'src')
        import main
        print("✓ 主应用程序导入成功")
        
        # 检查必要的类和函数是否存在
        if hasattr(main, 'WatermarkApp'):
            print("✓ WatermarkApp 类存在")
        else:
            print("✗ WatermarkApp 类不存在")
            return False
            
        if hasattr(main, 'get_chinese_font'):
            print("✓ get_chinese_font 函数存在")
        else:
            print("✗ get_chinese_font 函数不存在")
            return False
            
        return True
    except Exception as e:
        print(f"✗ 主应用程序测试失败: {e}")
        return False

def main():
    """主测试函数"""
    print("水印工具功能验证")
    print("=" * 30)
    
    # 运行各项测试
    test1 = test_imports()
    test2 = test_chinese_font_function()
    test3 = test_main_app()
    
    print("\n" + "=" * 30)
    if test1 and test2 and test3:
        print("所有测试通过! 水印工具可以正常工作。")
        return True
    else:
        print("部分测试失败，请检查上述错误信息。")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)