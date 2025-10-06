from PIL import Image, ImageDraw
import os

# 创建一个32x32的图标
icon = Image.new('RGBA', (32, 32), (240, 240, 240, 255))  # 浅灰色背景
draw = ImageDraw.Draw(icon)

# 绘制一个蓝色矩形（代表水印）
draw.rectangle([4, 4, 28, 22], fill=(74, 144, 226, 255))  # 蓝色

# 绘制WM文字
draw.text((16, 14), "WM", fill=(255, 255, 255, 255), anchor="mm")

# 绘制底部条形
draw.rectangle([8, 24, 24, 28], fill=(226, 226, 226, 255))  # 浅灰色

# 保存为ICO文件
icon.save("icon.ico", format="ICO")
print("ICO文件已创建: icon.ico")