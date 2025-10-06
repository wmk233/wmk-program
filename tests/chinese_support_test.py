#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
水印工具中文支持功能测试
用于验证水印工具的完整中文支持功能
"""

import sys
import os

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import WatermarkApp, get_chinese_font
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk

def test_chinese_font_function():
    """测试中文字体函数"""
    print("测试中文字体函数...")
    
    try:
        # 测试获取中文字体
        font = get_chinese_font(24)
        print(f"✓ 成功获取中文字体: {font}")
        return True
    except Exception as e:
        print(f"✗ 获取中文字体失败: {e}")
        return False

def test_chinese_watermark_text():
    """测试中文水印文本处理"""
    print("\n测试中文水印文本处理...")
    
    try:
        # 创建测试图像
        image = Image.new('RGB', (400, 200), color='white')
        
        # 模拟水印设置
        watermark_settings = {
            "text": "中文水印测试",
            "font": "Arial",
            "size": 24,
            "color": "#FF0000",
            "opacity": 100,
            "position": "center",
            "custom_x": 0,
            "custom_y": 0
        }
        
        # 测试文本水印添加
        draw = ImageDraw.Draw(image)
        
        try:
            # 尝试使用指定字体
            font = ImageFont.truetype(watermark_settings["font"], watermark_settings["size"])
        except:
            # 如果指定字体不可用，尝试使用中文字体
            try:
                font = get_chinese_font(watermark_settings["size"])
            except:
                # 如果中文字体也不可用，使用默认字体
                font = ImageFont.load_default()
        
        text = watermark_settings["text"]
        
        # 计算文本大小
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        print(f"✓ 成功处理中文文本: {text}")
        print(f"  文本尺寸: {text_width} x {text_height}")
        return True
        
    except Exception as e:
        print(f"✗ 处理中文水印文本失败: {e}")
        return False

def test_gui_chinese_support():
    """测试GUI中的中文支持"""
    print("\n测试GUI中的中文支持...")
    
    try:
        # 创建一个隐藏的Tk根窗口用于测试
        root = tk.Tk()
        root.withdraw()  # 隐藏窗口
        
        # 创建应用实例
        app = WatermarkApp(root)
        
        # 测试设置中文水印文本
        app.watermark_settings["text"] = "中文水印"
        app.text_entry.delete(0, tk.END)
        app.text_entry.insert(0, "中文水印")
        
        print("✓ GUI中文支持测试通过")
        root.destroy()
        return True
        
    except Exception as e:
        print(f"✗ GUI中文支持测试失败: {e}")
        return False

def main():
    """主测试函数"""
    print("水印工具中文支持功能测试")
    print("=" * 40)
    
    # 运行各项测试
    test1 = test_chinese_font_function()
    test2 = test_chinese_watermark_text()
    test3 = test_gui_chinese_support()
    
    print("\n" + "=" * 40)
    if test1 and test2 and test3:
        print("所有测试通过! 中文水印功能正常工作。")
        return True
    else:
        print("部分测试失败，请检查上述错误信息。")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)