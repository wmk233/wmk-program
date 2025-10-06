#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
中文水印测试脚本
用于验证水印工具中的中文字体支持功能
"""

import sys
import os

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import get_chinese_font
from PIL import Image, ImageDraw, ImageFont

def test_chinese_watermark_functionality():
    """测试中文水印功能"""
    print("开始测试中文水印功能...")
    
    # 创建测试图像
    image = Image.new('RGB', (500, 300), color='white')
    draw = ImageDraw.Draw(image)
    
    # 测试中文文本
    chinese_text = "中文水印测试"
    
    try:
        # 获取中文字体
        font = get_chinese_font(36)
        print(f"成功加载中文字体: {font}")
        
        # 计算文本尺寸
        bbox = draw.textbbox((0, 0), chinese_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # 在图像上绘制中文水印
        x = (500 - text_width) // 2
        y = (300 - text_height) // 2
        draw.text((x, y), chinese_text, font=font, fill=(255, 0, 0))
        
        # 保存测试结果
        image.save("chinese_watermark_functionality_test.png")
        print("中文水印功能测试成功，结果已保存为 chinese_watermark_functionality_test.png")
        return True
        
    except Exception as e:
        print(f"中文水印功能测试失败: {e}")
        return False

def test_font_fallback():
    """测试字体回退机制"""
    print("\n测试字体回退机制...")
    
    try:
        # 尝试加载不存在的字体文件
        font = ImageFont.truetype("nonexistent_font.ttf", 24)
    except Exception as e:
        print(f"无法加载不存在的字体: {e}")
        print("测试回退到中文字体...")
        font = get_chinese_font(24)
        print(f"成功回退到字体: {font}")
        return True
    
    return False

if __name__ == "__main__":
    print("水印工具中文字体支持测试")
    print("=" * 40)
    
    success1 = test_chinese_watermark_functionality()
    success2 = test_font_fallback()
    
    if success1 and success2:
        print("\n所有测试通过!")
    else:
        print("\n部分测试失败!")