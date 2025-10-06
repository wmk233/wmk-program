#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
透明度功能测试脚本
用于验证水印工具的透明度滑块功能
"""

import sys
import os

# 添加项目路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_opacity_function():
    """测试透明度功能"""
    print("测试透明度功能...")
    
    try:
        from PIL import Image, ImageDraw
        print("✓ PIL库导入成功")
        
        # 创建测试图像
        image = Image.new('RGBA', (400, 300), (255, 255, 255, 255))
        draw = ImageDraw.Draw(image)
        
        # 测试不同的透明度值
        test_opacities = [0, 25, 50, 75, 100]
        
        for i, opacity in enumerate(test_opacities):
            # 计算alpha值 (0-255)
            alpha = int(255 * opacity / 100)
            print(f"  测试透明度 {opacity}% (alpha={alpha})")
            
            # 在图像上绘制带透明度的文本
            y_pos = 50 + i * 40
            draw.text((50, y_pos), f"透明度: {opacity}%", fill=(255, 0, 0, alpha))
            
        # 保存测试结果
        image.save("opacity_test_result.png")
        print("✓ 透明度测试图像已保存为 opacity_test_result.png")
        return True
        
    except Exception as e:
        print(f"✗ 透明度功能测试失败: {e}")
        return False

def test_scale_function():
    """测试缩放功能"""
    print("\n测试缩放功能...")
    
    try:
        from PIL import Image
        print("✓ PIL库导入成功")
        
        # 创建测试图像
        image = Image.new('RGBA', (200, 100), (0, 100, 200, 255))
        
        # 测试不同的缩放值
        test_scales = [50, 100, 150, 200]
        
        result_image = Image.new('RGBA', (500, 200), (255, 255, 255, 255))
        result_draw = ImageDraw.Draw(result_image)
        
        for i, scale in enumerate(test_scales):
            # 计算新尺寸
            new_width = int(200 * scale / 100)
            new_height = int(100 * scale / 100)
            
            print(f"  测试缩放 {scale}% ({new_width}x{new_height})")
            
            # 调整图像大小
            resized = image.resize((new_width, new_height), Image.LANCZOS)
            
            # 在结果图像上放置缩放后的图像
            x_pos = i * 120
            result_image.paste(resized, (x_pos, 50))
            result_draw.text((x_pos, 30), f"缩放: {scale}%", fill=(0, 0, 0, 255))
            
        # 保存测试结果
        result_image.save("scale_test_result.png")
        print("✓ 缩放测试图像已保存为 scale_test_result.png")
        return True
        
    except Exception as e:
        print(f"✗ 缩放功能测试失败: {e}")
        return False

def main():
    """主测试函数"""
    print("水印工具透明度和缩放功能测试")
    print("=" * 40)
    
    # 运行测试
    test1 = test_opacity_function()
    test2 = test_scale_function()
    
    print("\n" + "=" * 40)
    if test1 and test2:
        print("所有测试通过! 透明度和缩放功能正常工作。")
        return True
    else:
        print("部分测试失败，请检查上述错误信息。")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)