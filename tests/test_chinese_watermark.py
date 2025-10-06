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


def test_chinese_watermark():
    """测试中文水印功能"""
    # 创建一个测试图像
    image = Image.new('RGBA', (800, 600), (255, 255, 255, 255))
    draw = ImageDraw.Draw(image)
    
    # 测试不同的中文文本
    test_texts = [
        "中文水印测试",
        "水印工具",
        "测试文本水印",
        "中文支持验证",
        "Watermark 水印"
    ]
    
    y_position = 50
    for i, text in enumerate(test_texts):
        # 尝试使用中文字体
        try:
            font_size = 24 + i * 4  # 逐渐增大字体
            font = get_chinese_font(font_size)
            print(f"成功加载字体: {font} 大小: {font_size}")
            
            # 计算文本大小
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            # 在图像上绘制中文文本
            x = (800 - text_width) // 2
            y = y_position
            draw.text((x, y), text, font=font, fill=(255, 0, 0, 255))
            
            y_position += text_height + 20
            
        except Exception as e:
            print(f"处理文本 '{text}' 时出错: {e}")
    
    # 保存测试图像
    image.save("chinese_watermark_test.png")
    print("中文水印测试图像已保存为 chinese_watermark_test.png")
    return True


def test_font_fallback():
    """测试字体回退机制"""
    print("测试字体回退机制...")
    
    # 尝试加载一个不存在的字体文件
    try:
        font = ImageFont.truetype("nonexistent_font.ttf", 24)
    except:
        print("无法加载不存在的字体，测试回退机制")
        font = get_chinese_font(24)
        print(f"回退到字体: {font}")


if __name__ == "__main__":
    print("测试中文字体支持...")
    success = test_chinese_watermark()
    
    print("\n" + "="*50)
    test_font_fallback()
    
    if success:
        print("\n中文字体测试完成!")
    else:
        print("\n中文字体测试失败!")