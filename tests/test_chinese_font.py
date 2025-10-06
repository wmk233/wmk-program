import tkinter as tk
from tkinter import ttk, filedialog, messagebox, colorchooser
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os
import json
import platform


def get_chinese_font(font_size):
    """获取支持中文的字体"""
    system = platform.system()
    font_paths = []
    
    if system == "Windows":
        # Windows系统字体路径
        font_paths = [
            "C:/Windows/Fonts/simsun.ttc",
            "C:/Windows/Fonts/SimSun.ttf",
            "C:/Windows/Fonts/msyh.ttc",
            "C:/Windows/Fonts/msyh.ttf"
        ]
    elif system == "Darwin":  # macOS
        # macOS系统字体路径
        font_paths = [
            "/System/Library/Fonts/PingFang.ttc",
            "/System/Library/Fonts/Helvetica.ttc",
            "/Library/Fonts/Songti.ttc"
        ]
    
    # 尝试加载中文字体
    for font_path in font_paths:
        if os.path.exists(font_path):
            try:
                return ImageFont.truetype(font_path, font_size)
            except Exception as e:
                print(f"无法加载字体 {font_path}: {e}")
                continue
    
    # 如果找不到中文字体，回退到默认字体
    print("未找到可用的中文字体，使用默认字体")
    return ImageFont.load_default()


def test_chinese_font():
    """测试中文字体功能"""
    # 创建一个测试图像
    image = Image.new('RGBA', (400, 200), (255, 255, 255, 255))
    draw = ImageDraw.Draw(image)
    
    # 测试中文文本
    chinese_text = "中文水印测试"
    
    # 尝试使用中文字体
    try:
        font = get_chinese_font(24)
        print(f"成功加载字体: {font}")
        
        # 计算文本大小
        bbox = draw.textbbox((0, 0), chinese_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # 在图像上绘制中文文本
        x = (400 - text_width) // 2
        y = (200 - text_height) // 2
        draw.text((x, y), chinese_text, font=font, fill=(255, 0, 0, 255))
        
        # 保存测试图像
        image.save("chinese_font_test.png")
        print("中文水印测试图像已保存为 chinese_font_test.png")
        return True
    except Exception as e:
        print(f"测试中文字体时出错: {e}")
        return False


if __name__ == "__main__":
    print("测试中文字体支持...")
    success = test_chinese_font()
    if success:
        print("中文字体测试成功!")
    else:
        print("中文字体测试失败!")