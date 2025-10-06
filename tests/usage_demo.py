#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
水印工具使用示例
演示如何使用水印工具的核心功能
"""

import os
import sys
import tempfile
from PIL import Image, ImageDraw

def create_sample_images():
    """创建示例图片用于演示"""
    print("正在创建示例图片...")
    
    # 创建示例图片目录
    sample_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample_images")
    if not os.path.exists(sample_dir):
        os.makedirs(sample_dir)
    
    # 创建示例图片
    sample_images = []
    sizes = [(800, 600), (1024, 768)]
    
    for i, size in enumerate(sizes):
        image = Image.new('RGB', size, color='lightblue')
        draw = ImageDraw.Draw(image)
        
        # 添加一些简单的图形用于演示
        draw.rectangle([50, 50, size[0]-50, size[1]-50], outline='darkblue', width=3)
        draw.ellipse([100, 100, 300, 300], outline='red', width=2)
        draw.text((size[0]//2-50, size[1]//2-10), f"Sample Image {i+1}", fill='black')
        
        filepath = os.path.join(sample_dir, f"sample_{i+1}.jpg")
        image.save(filepath, quality=95)
        sample_images.append(filepath)
        print(f"已创建示例图片: {os.path.basename(filepath)}")
        
    return sample_dir, sample_images

def demonstrate_usage():
    """演示水印工具的使用方法"""
    print("水印工具使用演示")
    print("=" * 30)
    
    # 1. 创建示例图片
    sample_dir, sample_images = create_sample_images()
    
    print(f"\n1. 已创建 {len(sample_images)} 张示例图片在目录: {sample_dir}")
    print("   您可以手动将这些图片导入到水印工具中进行测试")
    
    # 2. 文本水印设置示例
    print("\n2. 文本水印设置示例:")
    print("   - 水印文字: '示例水印'")
    print("   - 字体大小: 36")
    print("   - 颜色: 红色 (#FF0000)")
    print("   - 透明度: 70%")
    print("   - 位置: 右下角")
    
    # 3. 图片水印设置示例
    print("\n3. 图片水印设置示例:")
    print("   - 选择一张PNG格式的Logo图片作为水印")
    print("   - 缩放比例: 50%")
    print("   - 透明度: 80%")
    print("   - 位置: 中心")
    
    # 4. 导出设置示例
    print("\n4. 导出设置示例:")
    print("   - 导出文件夹: 选择一个新文件夹")
    print("   - 命名规则: 添加后缀 '_watermarked'")
    print("   - 格式: 保持原格式")
    
    # 5. 模板使用示例
    print("\n5. 模板使用示例:")
    print("   - 保存当前设置为模板 '我的水印设置'")
    print("   - 下次使用时直接加载该模板")
    
    print("\n" + "=" * 30)
    print("使用步骤:")
    print("1. 运行 'py main.py' 启动水印工具")
    print("2. 点击 '选择图片' 导入示例图片")
    print("3. 在左侧控制面板中设置水印参数")
    print("4. 在预览窗口中查看效果")
    print("5. 设置导出参数并点击 '导出图片'")
    
    print(f"\n示例图片目录: {sample_dir}")
    print("您可以现在运行 'py main.py' 来使用水印工具!")

if __name__ == "__main__":
    demonstrate_usage()