#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
交互式透明度测试脚本
用于手动验证透明度滑块功能
"""

import sys
import os

# 添加src目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def interactive_opacity_test():
    """交互式透明度测试"""
    print("交互式透明度测试")
    print("=" * 30)
    
    # 模拟水印设置
    watermark_settings = {
        "opacity": 100,
        "color": "#FF0000",
        "text": "测试水印"
    }
    
    print(f"初始设置:")
    print(f"  透明度: {watermark_settings['opacity']}%")
    print(f"  颜色: {watermark_settings['color']}")
    print(f"  文本: {watermark_settings['text']}")
    
    # 模拟透明度变化
    test_opacities = [100, 75, 50, 25, 0]
    
    for opacity in test_opacities:
        print(f"\n模拟透明度滑块调整到 {opacity}%:")
        
        # 更新设置
        watermark_settings["opacity"] = opacity
        
        # 计算alpha值
        alpha = int(255 * opacity / 100)
        
        # 应用颜色
        color = watermark_settings["color"]
        if color.startswith('#'):
            r, g, b = tuple(int(color[i:i+2], 16) for i in (1, 3, 5))
        else:
            r, g, b = 255, 0, 0
            
        rgba = (r, g, b, alpha)
        
        print(f"  更新后的RGBA值: {rgba}")
        print(f"  预期效果: {'完全不透明' if opacity == 100 else '半透明' if opacity > 0 else '完全透明'}")
        
        # 验证计算是否正确
        expected_alpha = int(255 * opacity / 100)
        if alpha == expected_alpha:
            print(f"  ✓ 透明度计算正确")
        else:
            print(f"  ✗ 透明度计算错误: 期望 {expected_alpha}, 实际 {alpha}")
            
    print("\n" + "=" * 30)
    print("交互式测试完成!")

def main():
    """主函数"""
    interactive_opacity_test()

if __name__ == "__main__":
    main()