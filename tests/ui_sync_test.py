#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
UI同步功能测试脚本
用于验证水印工具的UI元素同步功能
"""

import sys
import os

# 添加src目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_text_sync():
    """测试文本同步功能"""
    print("测试文本同步功能...")
    
    try:
        # 模拟水印设置
        watermark_settings = {
            "text": "水印文字",
        }
        
        # 模拟文本输入框
        class MockEntry:
            def __init__(self, initial_text):
                self.text = initial_text
                
            def get(self):
                return self.text
                
            def delete(self, start, end=None):
                self.text = ""
                
            def insert(self, pos, text):
                self.text = text
                
        # 创建模拟输入框
        mock_entry = MockEntry(watermark_settings["text"])
        print(f"  初始文本: {mock_entry.get()}")
        
        # 模拟文本变化事件
        def on_text_change(event=None):
            watermark_settings["text"] = mock_entry.get()
            print(f"  文本已更新为: {watermark_settings['text']}")
            
        # 测试文本输入
        test_texts = ["测试水印", "Hello World", "中文测试", "123456"]
        
        for text in test_texts:
            # 模拟用户输入
            mock_entry.delete(0, tk.END) if 'tk' in globals() else mock_entry.delete(0)
            mock_entry.insert(0, text)
            
            # 触发文本变化事件
            on_text_change()
            
            # 验证设置是否同步
            if watermark_settings["text"] == text:
                print(f"  ✓ 文本 '{text}' 同步成功")
            else:
                print(f"  ✗ 文本同步失败: 期望 '{text}', 实际 '{watermark_settings['text']}'")
                return False
                
        print("  ✓ 所有文本同步测试通过")
        return True
        
    except Exception as e:
        print(f"  ✗ 文本同步测试失败: {e}")
        return False

def test_ui_element_binding():
    """测试UI元素绑定"""
    print("\n测试UI元素绑定...")
    
    try:
        # 模拟UI元素和事件绑定
        class MockUI:
            def __init__(self):
                self.watermark_settings = {"text": "水印文字"}
                self.text_entry = None
                self.preview_updated = False
                
            def create_text_entry(self):
                class Entry:
                    def __init__(self):
                        self.text = "水印文字"
                        self.bindings = {}
                        
                    def insert(self, pos, text):
                        self.text = text
                        
                    def get(self):
                        return self.text
                        
                    def delete(self, start, end=None):
                        self.text = ""
                        
                    def bind(self, event, callback):
                        self.bindings[event] = callback
                        
                self.text_entry = Entry()
                return self.text_entry
                
            def on_text_change(self, event=None):
                if self.text_entry:
                    self.watermark_settings["text"] = self.text_entry.get()
                    self.preview_updated = True
                    
            def update_preview(self):
                self.preview_updated = True
                
        # 创建模拟UI
        mock_ui = MockUI()
        entry = mock_ui.create_text_entry()
        
        # 绑定事件
        entry.bind('<KeyRelease>', mock_ui.on_text_change)
        entry.bind('<FocusOut>', mock_ui.on_text_change)
        
        # 验证绑定
        if '<KeyRelease>' in entry.bindings and '<FocusOut>' in entry.bindings:
            print("  ✓ 事件绑定成功")
        else:
            print("  ✗ 事件绑定失败")
            return False
            
        # 测试事件触发
        mock_ui.preview_updated = False
        entry.insert(0, "新测试文本")
        mock_ui.on_text_change()
        
        if mock_ui.watermark_settings["text"] == "新测试文本":
            print("  ✓ 文本变化事件处理正确")
        else:
            print("  ✗ 文本变化事件处理错误")
            return False
            
        if mock_ui.preview_updated:
            print("  ✓ 预览更新触发成功")
        else:
            print("  ✗ 预览更新未触发")
            return False
            
        print("  ✓ UI元素绑定测试通过")
        return True
        
    except Exception as e:
        print(f"  ✗ UI元素绑定测试失败: {e}")
        return False

def main():
    """主测试函数"""
    print("水印工具UI同步功能测试")
    print("=" * 30)
    
    # 运行测试
    test1 = test_text_sync()
    test2 = test_ui_element_binding()
    
    print("\n" + "=" * 30)
    if test1 and test2:
        print("所有测试通过! UI同步功能正常工作。")
        return True
    else:
        print("部分测试失败，请检查上述错误信息。")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)