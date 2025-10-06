#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
水印工具功能测试脚本
用于验证程序的核心功能
"""

import os
import sys
import tempfile
from PIL import Image, ImageDraw

# 添加项目路径到系统路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_image_creation():
    """测试图片创建功能"""
    print("正在创建测试图片...")
    
    # 创建测试图片目录
    test_dir = tempfile.mkdtemp()
    print(f"测试目录: {test_dir}")
    
    # 创建测试图片
    test_images = []
    sizes = [(800, 600), (600, 400), (1024, 768)]
    
    for i, size in enumerate(sizes):
        image = Image.new('RGB', size, color='white')
        draw = ImageDraw.Draw(image)
        
        # 添加一些简单的图形用于测试
        draw.rectangle([50, 50, size[0]-50, size[1]-50], outline='black', width=2)
        draw.text((size[0]//2-30, size[1]//2-10), f"TEST {i+1}", fill='black')
        
        filepath = os.path.join(test_dir, f"test_{i+1}.jpg")
        image.save(filepath, quality=95)
        test_images.append(filepath)
        print(f"已创建测试图片: {os.path.basename(filepath)}")
        
    return test_dir, test_images

def test_watermark_functionality():
    """测试水印功能"""
    print("\n正在测试水印功能...")
    
    try:
        # 导入主模块
        import main
        
        # 创建应用实例
        print("正在初始化应用...")
        root = main.tk.Tk()
        root.withdraw()  # 隐藏主窗口
        
        app = main.WatermarkApp(root)
        print("应用初始化成功")
        
        # 测试图片导入
        test_dir, test_images = test_image_creation()
        
        # 添加图片到应用
        app.image_list = test_images.copy()
        for img_path in test_images:
            filename = os.path.basename(img_path)
            app.image_listbox.insert("end", filename)
            
        print(f"已导入 {len(test_images)} 张测试图片")
        
        # 测试文本水印
        print("正在测试文本水印...")
        app.watermark_settings["type"] = "text"
        app.watermark_settings["text"] = "测试水印"
        app.watermark_settings["color"] = "#FF0000"
        app.watermark_settings["opacity"] = 80
        
        # 测试图片水印设置
        print("正在测试图片水印设置...")
        app.watermark_settings["type"] = "image"
        # 由于我们没有实际的水印图片，这里只是测试设置
        
        # 切换回文本水印进行实际测试
        app.watermark_settings["type"] = "text"
        
        # 测试预览功能
        print("正在测试预览功能...")
        app.current_image_index = 0
        app.update_preview()
        print("预览功能测试完成")
        
        # 测试模板功能
        print("正在测试模板功能...")
        template = {
            "name": "测试模板",
            "settings": app.watermark_settings.copy()
        }
        app.templates.append(template)
        app.save_templates()
        print("模板保存功能测试完成")
        
        # 清理测试文件
        import shutil
        shutil.rmtree(test_dir)
        print("测试文件清理完成")
        
        print("\n所有功能测试通过！")
        return True
        
    except Exception as e:
        print(f"功能测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("水印工具功能测试")
    print("=" * 30)
    
    success = test_watermark_functionality()
    
    if success:
        print("\n✅ 所有测试通过，程序功能正常！")
    else:
        print("\n❌ 测试失败，请检查程序代码。")

if __name__ == "__main__":
    main()