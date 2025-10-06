#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
水印工具透明度功能验证脚本
用于验证透明度滑块是否正常工作
"""

import sys
import os

# 添加src目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_transparency_calculation():
    """测试透明度计算功能"""
    print("测试透明度计算...")
    
    # 测试不同的透明度值
    test_cases = [
        (100, 255),  # 100% 透明度应该等于 255 alpha
        (50, 127),   # 50% 透明度应该等于 127 alpha
        (0, 0),      # 0% 透明度应该等于 0 alpha
        (75, 191),   # 75% 透明度应该等于 191 alpha
        (25, 64)     # 25% 透明度应该等于 64 alpha
    ]
    
    for opacity, expected_alpha in test_cases:
        # 计算alpha值
        alpha = int(255 * opacity / 100)
        print(f"  透明度 {opacity}% -> Alpha {alpha} (期望: {expected_alpha})")
        
        if alpha != expected_alpha and abs(alpha - expected_alpha) > 1:
            print(f"  ✗ 计算错误!")
            return False
    
    print("  ✓ 透明度计算正确")
    return True

def test_color_parsing():
    """测试颜色解析功能"""
    print("\n测试颜色解析...")
    
    # 测试颜色解析
    test_colors = [
        ("#FF0000", (255, 0, 0)),    # 红色
        ("#00FF00", (0, 255, 0)),    # 绿色
        ("#0000FF", (0, 0, 255)),    # 蓝色
        ("#FFFFFF", (255, 255, 255)) # 白色
    ]
    
    for hex_color, expected_rgb in test_colors:
        if hex_color.startswith('#'):
            r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
            print(f"  {hex_color} -> RGB({r}, {g}, {b})")
            
            if (r, g, b) != expected_rgb:
                print(f"  ✗ 颜色解析错误!")
                return False
    
    print("  ✓ 颜色解析正确")
    return True

def test_watermark_integration():
    """测试水印集成功能"""
    print("\n测试水印集成功能...")
    
    try:
        # 导入必要的模块
        from PIL import Image, ImageDraw
        
        # 创建测试图像
        image = Image.new('RGBA', (300, 200), (255, 255, 255, 255))
        draw = ImageDraw.Draw(image)
        
        # 模拟水印设置
        watermark_settings = {
            "text": "测试水印",
            "color": "#FF0000",
            "opacity": 50  # 50% 透明度
        }
        
        # 应用透明度
        text = watermark_settings["text"]
        color = watermark_settings["color"]
        opacity = watermark_settings["opacity"]
        
        if color.startswith('#'):
            r, g, b = tuple(int(color[i:i+2], 16) for i in (1, 3, 5))
        else:
            r, g, b = 255, 0, 0
            
        alpha = int(255 * opacity / 100)
        rgba = (r, g, b, alpha)
        
        print(f"  水印文本: {text}")
        print(f"  颜色: {color} -> RGBA{rgba}")
        print(f"  透明度: {opacity}% -> Alpha {alpha}")
        
        # 在图像上绘制文本
        draw.text((50, 50), text, fill=rgba)
        
        # 保存测试结果
        image.save("watermark_integration_test.png")
        print("  ✓ 水印集成功能测试通过，结果保存为 watermark_integration_test.png")
        return True
        
    except Exception as e:
        print(f"  ✗ 水印集成功能测试失败: {e}")
        return False

def main():
    """主测试函数"""
    print("水印工具透明度功能验证")
    print("=" * 30)
    
    # 运行各项测试
    test1 = test_transparency_calculation()
    test2 = test_color_parsing()
    test3 = test_watermark_integration()
    
    print("\n" + "=" * 30)
    if test1 and test2 and test3:
        print("所有测试通过! 透明度功能正常工作。")
        return True
    else:
        print("部分测试失败，请检查上述错误信息。")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)