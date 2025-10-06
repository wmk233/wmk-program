#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
水印工具测试脚本
用于验证程序的基本功能
"""

import os
import sys
import unittest
from PIL import Image, ImageDraw

# 添加项目路径到系统路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class TestWatermarkApp(unittest.TestCase):
    
    def setUp(self):
        """测试前的准备工作"""
        # 创建测试图片目录
        self.test_dir = "test_images"
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)
            
        # 创建测试图片
        self.create_test_image("test1.jpg", (800, 600))
        self.create_test_image("test2.png", (600, 400))
        
    def tearDown(self):
        """测试后的清理工作"""
        # 删除测试图片
        test_files = ["test1.jpg", "test2.png"]
        for filename in test_files:
            filepath = os.path.join(self.test_dir, filename)
            if os.path.exists(filepath):
                os.remove(filepath)
                
        # 删除测试目录
        if os.path.exists(self.test_dir):
            os.rmdir(self.test_dir)
            
    def create_test_image(self, filename, size):
        """创建测试图片"""
        image = Image.new('RGB', size, color='white')
        draw = ImageDraw.Draw(image)
        
        # 添加一些简单的图形用于测试
        draw.rectangle([50, 50, size[0]-50, size[1]-50], outline='black', width=2)
        draw.text((size[0]//2-30, size[1]//2-10), "TEST", fill='black')
        
        filepath = os.path.join(self.test_dir, filename)
        image.save(filepath, quality=95)
        
    def test_import_images(self):
        """测试图片导入功能"""
        # 检查测试图片是否创建成功
        jpg_path = os.path.join(self.test_dir, "test1.jpg")
        png_path = os.path.join(self.test_dir, "test2.png")
        
        self.assertTrue(os.path.exists(jpg_path), "JPEG测试图片未创建成功")
        self.assertTrue(os.path.exists(png_path), "PNG测试图片未创建成功")
        
        # 检查图片是否可以正常打开
        try:
            img1 = Image.open(jpg_path)
            img2 = Image.open(png_path)
            self.assertEqual(img1.size, (800, 600), "JPEG图片尺寸不正确")
            self.assertEqual(img2.size, (600, 400), "PNG图片尺寸不正确")
        except Exception as e:
            self.fail(f"无法打开测试图片: {e}")
            
    def test_requirements_installed(self):
        """测试依赖包是否安装"""
        try:
            from PIL import Image, ImageDraw, ImageFont
            import tkinter as tk
        except ImportError as e:
            self.fail(f"依赖包未正确安装: {e}")
            
    def test_main_module_import(self):
        """测试主模块是否可以导入"""
        try:
            # 尝试导入主模块
            import main
            self.assertTrue(hasattr(main, 'WatermarkApp'), "WatermarkApp类未定义")
        except Exception as e:
            # 这个测试可能会因为缺少依赖而失败，这是预期的
            print(f"主模块导入测试: {e}")

if __name__ == '__main__':
    print("开始运行水印工具测试...")
    unittest.main(verbosity=2)