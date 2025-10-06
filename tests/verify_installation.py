#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
水印工具核心功能验证脚本
验证程序的主要功能模块是否正常工作
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont

def test_pillow_installation():
    """测试Pillow库是否正确安装"""
    print("1. 测试Pillow库安装...")
    try:
        from PIL import Image, ImageDraw, ImageFont
        print("   ✅ Pillow库已正确安装")
        print(f"   📦 Pillow版本: {Image.__version__}")
        return True
    except ImportError as e:
        print(f"   ❌ Pillow库未正确安装: {e}")
        return False

def test_tkinter_installation():
    """测试Tkinter是否可用"""
    print("2. 测试Tkinter安装...")
    try:
        import tkinter as tk
        print("   ✅ Tkinter已正确安装")
        return True
    except ImportError as e:
        print(f"   ❌ Tkinter未正确安装: {e}")
        return False

def test_main_module():
    """测试主模块是否可以导入"""
    print("3. 测试主模块导入...")
    try:
        # 添加当前目录到Python路径
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        
        import main
        print("   ✅ 主模块导入成功")
        
        # 测试WatermarkApp类是否存在
        if hasattr(main, 'WatermarkApp'):
            print("   ✅ WatermarkApp类存在")
        else:
            print("   ❌ WatermarkApp类不存在")
            return False
            
        return True
    except Exception as e:
        print(f"   ❌ 主模块导入失败: {e}")
        return False

def test_image_processing():
    """测试图像处理功能"""
    print("4. 测试图像处理功能...")
    try:
        # 创建一个简单的测试图像
        image = Image.new('RGB', (200, 150), color='white')
        draw = ImageDraw.Draw(image)
        draw.rectangle([10, 10, 190, 140], outline='black', width=2)
        draw.text((50, 60), "Test", fill='black')
        
        # 测试保存和重新打开
        test_path = "test_image.jpg"
        image.save(test_path, quality=95)
        
        # 验证图像是否正确保存
        loaded_image = Image.open(test_path)
        if loaded_image.size == (200, 150):
            print("   ✅ 图像处理功能正常")
        else:
            print("   ❌ 图像处理结果不正确")
            return False
            
        # 清理测试文件
        if os.path.exists(test_path):
            os.remove(test_path)
            
        return True
    except Exception as e:
        print(f"   ❌ 图像处理功能测试失败: {e}")
        return False

def test_requirements_file():
    """测试requirements.txt文件"""
    print("5. 测试依赖文件...")
    try:
        req_file = os.path.join(os.path.dirname(__file__), "requirements.txt")
        if os.path.exists(req_file):
            with open(req_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'Pillow' in content:
                    print("   ✅ requirements.txt文件格式正确")
                    return True
                else:
                    print("   ❌ requirements.txt文件内容不正确")
                    return False
        else:
            print("   ❌ requirements.txt文件不存在")
            return False
    except Exception as e:
        print(f"   ❌ 依赖文件测试失败: {e}")
        return False

def main():
    """主函数"""
    print("水印工具核心功能验证")
    print("=" * 30)
    
    tests = [
        test_pillow_installation,
        test_tkinter_installation,
        test_main_module,
        test_image_processing,
        test_requirements_file
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()  # 添加空行分隔
    
    print("=" * 30)
    print(f"测试结果: {passed}/{total} 通过")
    
    if passed == total:
        print("🎉 所有测试通过！水印工具已准备就绪。")
        print("\n下一步:")
        print("1. 运行 'py main.py' 启动水印工具")
        print("2. 使用示例图片测试功能")
        print("3. 查看 README.md 获取详细使用说明")
    else:
        print("❌ 部分测试失败，请检查上述错误信息。")

if __name__ == "__main__":
    main()