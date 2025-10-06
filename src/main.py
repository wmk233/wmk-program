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
            except Exception:
                continue
    
    # 如果找不到中文字体，回退到默认字体
    return ImageFont.load_default()


class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("水印工具")
        self.root.geometry("1000x700")
        
        # 数据存储
        self.image_list = []  # 存储导入的图片路径
        self.current_image_index = -1  # 当前显示的图片索引
        self.watermark_settings = {
            "type": "text",  # text 或 image
            "text": "水印文字",
            "font": "Arial",
            "size": 24,
            "color": "#FF0000",
            "opacity": 100,
            "position": "bottom-right",  # top-left, top-center, top-right, center-left, center, center-right, bottom-left, bottom-center, bottom-right
            "custom_x": 0,
            "custom_y": 0,
            "rotation": 0,
            "shadow": False,
            "stroke": False,
            "watermark_image_path": "",
            "watermark_scale": 100
        }
        
        self.templates = []
        self.load_templates()
        
        self.setup_ui()
        
    def setup_ui(self):
        # 创建菜单栏
        self.create_menu()
        
        # 主框架
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 左侧控制面板
        control_frame = ttk.Frame(main_frame, width=300)
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        control_frame.pack_propagate(False)
        
        # 右侧预览区域
        preview_frame = ttk.Frame(main_frame)
        preview_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # 创建控制面板内容
        self.create_control_panel(control_frame)
        
        # 创建预览区域
        self.create_preview_area(preview_frame)
        
    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # 文件菜单
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="文件", menu=file_menu)
        file_menu.add_command(label="导入图片", command=self.import_images)
        file_menu.add_command(label="导入文件夹", command=self.import_folder)
        file_menu.add_separator()
        file_menu.add_command(label="退出", command=self.root.quit)
        
        # 模板菜单
        template_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="模板", menu=template_menu)
        template_menu.add_command(label="保存当前设置为模板", command=self.save_template)
        template_menu.add_command(label="管理模板", command=self.manage_templates)
        
    def create_control_panel(self, parent):
        # 导入区域
        import_frame = ttk.LabelFrame(parent, text="导入图片")
        import_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(import_frame, text="选择图片", command=self.import_images).pack(fill=tk.X, pady=5)
        ttk.Button(import_frame, text="选择文件夹", command=self.import_folder).pack(fill=tk.X, pady=5)
        
        # 图片列表
        list_frame = ttk.LabelFrame(parent, text="图片列表")
        list_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # 创建列表框和滚动条
        listbox_frame = ttk.Frame(list_frame)
        listbox_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.image_listbox = tk.Listbox(listbox_frame)
        scrollbar = ttk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=self.image_listbox.yview)
        self.image_listbox.configure(yscrollcommand=scrollbar.set)
        
        self.image_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.image_listbox.bind('<<ListboxSelect>>', self.on_image_select)
        
        # 水印类型选择
        type_frame = ttk.LabelFrame(parent, text="水印类型")
        type_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.watermark_type_var = tk.StringVar(value="text")
        ttk.Radiobutton(type_frame, text="文本水印", variable=self.watermark_type_var, value="text", command=self.update_watermark_type).pack(anchor=tk.W)
        ttk.Radiobutton(type_frame, text="图片水印", variable=self.watermark_type_var, value="image", command=self.update_watermark_type).pack(anchor=tk.W)
        
        # 文本水印设置
        self.text_settings_frame = ttk.LabelFrame(parent, text="文本水印设置")
        self.text_settings_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(self.text_settings_frame, text="水印文字:").pack(anchor=tk.W)
        self.text_entry = ttk.Entry(self.text_settings_frame)
        self.text_entry.pack(fill=tk.X, padx=5, pady=5)
        self.text_entry.insert(0, self.watermark_settings["text"])
        
        # 字体大小
        ttk.Label(self.text_settings_frame, text="字体大小:").pack(anchor=tk.W)
        self.size_var = tk.IntVar(value=self.watermark_settings["size"])
        size_spinbox = ttk.Spinbox(self.text_settings_frame, from_=8, to=100, textvariable=self.size_var, command=self.update_preview)
        size_spinbox.pack(fill=tk.X, padx=5, pady=5)
        
        # 颜色选择
        color_frame = ttk.Frame(self.text_settings_frame)
        color_frame.pack(fill=tk.X, padx=5, pady=5)
        ttk.Label(color_frame, text="颜色:").pack(side=tk.LEFT)
        self.color_button = tk.Button(color_frame, bg=self.watermark_settings["color"], width=3, command=self.choose_color)
        self.color_button.pack(side=tk.LEFT, padx=(5, 0))
        self.color_label = ttk.Label(color_frame, text=self.watermark_settings["color"])
        self.color_label.pack(side=tk.LEFT, padx=(5, 0))
        
        # 透明度
        ttk.Label(self.text_settings_frame, text="透明度:").pack(anchor=tk.W)
        self.opacity_var = tk.IntVar(value=self.watermark_settings["opacity"])
        opacity_scale = ttk.Scale(self.text_settings_frame, from_=0, to=100, variable=self.opacity_var, command=self.on_opacity_change)
        opacity_scale.pack(fill=tk.X, padx=5, pady=5)
        self.opacity_label = ttk.Label(self.text_settings_frame, text=f"{self.watermark_settings['opacity']}%")
        self.opacity_label.pack()
        
        # 图片水印设置（初始隐藏）
        self.image_settings_frame = ttk.LabelFrame(parent, text="图片水印设置")
        self.image_settings_frame.pack(fill=tk.X, pady=(0, 10))
        self.image_settings_frame.pack_forget()  # 初始隐藏
        
        ttk.Button(self.image_settings_frame, text="选择水印图片", command=self.select_watermark_image).pack(fill=tk.X, pady=5)
        self.watermark_image_label = ttk.Label(self.image_settings_frame, text="未选择图片")
        self.watermark_image_label.pack(pady=5)
        
        # 缩放设置
        ttk.Label(self.image_settings_frame, text="图片缩放:").pack(anchor=tk.W)
        self.scale_var = tk.IntVar(value=self.watermark_settings["watermark_scale"])
        scale_scale = ttk.Scale(self.image_settings_frame, from_=10, to=200, variable=self.scale_var, command=self.on_scale_change)
        scale_scale.pack(fill=tk.X, padx=5, pady=5)
        self.scale_label = ttk.Label(self.image_settings_frame, text=f"{self.watermark_settings['watermark_scale']}%")
        self.scale_label.pack()
        
        # 位置设置
        position_frame = ttk.LabelFrame(parent, text="水印位置")
        position_frame.pack(fill=tk.X, pady=(0, 10))
        
        # 预设位置按钮网格
        grid_frame = ttk.Frame(position_frame)
        grid_frame.pack()
        
        positions = [
            ("↖", "top-left"), ("↑", "top-center"), ("↗", "top-right"),
            ("←", "center-left"), ("●", "center"), ("→", "center-right"),
            ("↙", "bottom-left"), ("↓", "bottom-center"), ("↘", "bottom-right")
        ]
        
        for i, (text, pos) in enumerate(positions):
            row, col = divmod(i, 3)
            btn = ttk.Button(grid_frame, text=text, width=3, command=lambda p=pos: self.set_position(p))
            btn.grid(row=row, column=col, padx=2, pady=2)
            
        # 手动拖拽提示
        ttk.Label(position_frame, text="在预览区可手动拖拽调整位置").pack(pady=5)
        
        # 导出设置
        export_frame = ttk.LabelFrame(parent, text="导出设置")
        export_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(export_frame, text="选择导出文件夹", command=self.select_export_folder).pack(fill=tk.X, pady=5)
        self.export_path_label = ttk.Label(export_frame, text="未选择导出文件夹")
        self.export_path_label.pack(pady=5)
        
        # 命名规则
        ttk.Label(export_frame, text="文件名规则:").pack(anchor=tk.W)
        self.naming_var = tk.StringVar(value="suffix")
        naming_frame = ttk.Frame(export_frame)
        naming_frame.pack(fill=tk.X, padx=5)
        ttk.Radiobutton(naming_frame, text="保留原名", variable=self.naming_var, value="original").pack(anchor=tk.W)
        ttk.Radiobutton(naming_frame, text="添加前缀", variable=self.naming_var, value="prefix").pack(anchor=tk.W)
        ttk.Radiobutton(naming_frame, text="添加后缀", variable=self.naming_var, value="suffix").pack(anchor=tk.W)
        
        self.prefix_entry = ttk.Entry(export_frame)
        self.prefix_entry.pack(fill=tk.X, padx=5, pady=5)
        self.prefix_entry.insert(0, "wm_")
        
        self.suffix_entry = ttk.Entry(export_frame)
        self.suffix_entry.pack(fill=tk.X, padx=5, pady=5)
        self.suffix_entry.insert(0, "_watermarked")
        
        # 导出按钮
        ttk.Button(export_frame, text="导出图片", command=self.export_images).pack(fill=tk.X, pady=10)
        
    def create_preview_area(self, parent):
        # 预览标题
        ttk.Label(parent, text="预览").pack(anchor=tk.W)
        
        # 创建画布用于显示图片
        self.canvas_frame = ttk.Frame(parent)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.canvas = tk.Canvas(self.canvas_frame, bg="lightgray")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # 绑定鼠标事件用于拖拽水印
        self.canvas.bind("<Button-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.drag_watermark)
        
        # 显示提示信息
        self.canvas.create_text(250, 200, text="请选择图片进行预览", fill="gray", font=("Arial", 16))
        
    def update_watermark_type(self):
        self.watermark_settings["type"] = self.watermark_type_var.get()
        if self.watermark_settings["type"] == "text":
            self.text_settings_frame.pack(fill=tk.X, pady=(0, 10))
            self.image_settings_frame.pack_forget()
        else:
            self.text_settings_frame.pack_forget()
            self.image_settings_frame.pack(fill=tk.X, pady=(0, 10))
        self.update_preview()
        
    def choose_color(self):
        color = colorchooser.askcolor(initialcolor=self.watermark_settings["color"])[1]
        if color:
            self.watermark_settings["color"] = color
            self.color_button.config(bg=color)
            self.color_label.config(text=color)
            self.update_preview()
            
    def on_opacity_change(self, value):
        opacity = int(float(value))
        self.watermark_settings["opacity"] = opacity
        self.opacity_label.config(text=f"{opacity}%")
        self.update_preview()
        
    def on_scale_change(self, value):
        scale = int(float(value))
        self.watermark_settings["watermark_scale"] = scale
        self.scale_label.config(text=f"{scale}%")
        self.update_preview()
        
    def set_position(self, position):
        self.watermark_settings["position"] = position
        self.update_preview()
        
    def start_drag(self, event):
        # 开始拖拽水印
        self.drag_start_x = event.x
        self.drag_start_y = event.y
        
    def drag_watermark(self, event):
        # 拖拽水印
        if self.current_image_index >= 0:
            dx = event.x - self.drag_start_x
            dy = event.y - self.drag_start_y
            
            # 更新自定义位置
            self.watermark_settings["custom_x"] += dx
            self.watermark_settings["custom_y"] += dy
            self.watermark_settings["position"] = "custom"
            
            self.drag_start_x = event.x
            self.drag_start_y = event.y
            self.update_preview()
            
    def import_images(self):
        file_paths = filedialog.askopenfilenames(
            title="选择图片文件",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
        )
        
        if file_paths:
            for path in file_paths:
                if path not in self.image_list:
                    self.image_list.append(path)
                    filename = os.path.basename(path)
                    self.image_listbox.insert(tk.END, filename)
                    
            # 如果是第一次导入图片，则显示第一张
            if self.current_image_index == -1 and len(self.image_list) > 0:
                self.current_image_index = 0
                self.image_listbox.selection_set(0)
                self.show_image(0)
                
    def import_folder(self):
        folder_path = filedialog.askdirectory(title="选择包含图片的文件夹")
        
        if folder_path:
            image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
            for filename in os.listdir(folder_path):
                if filename.lower().endswith(image_extensions):
                    full_path = os.path.join(folder_path, filename)
                    if full_path not in self.image_list:
                        self.image_list.append(full_path)
                        self.image_listbox.insert(tk.END, filename)
                        
            # 如果是第一次导入图片，则显示第一张
            if self.current_image_index == -1 and len(self.image_list) > 0:
                self.current_image_index = 0
                self.image_listbox.selection_set(0)
                self.show_image(0)
                
    def on_image_select(self, event):
        selection = self.image_listbox.curselection()
        if selection:
            index = selection[0]
            self.current_image_index = index
            self.show_image(index)
            
    def show_image(self, index):
        if 0 <= index < len(self.image_list):
            image_path = self.image_list[index]
            self.update_preview()
            
    def update_preview(self):
        if self.current_image_index >= 0 and self.current_image_index < len(self.image_list):
            # 清空画布
            self.canvas.delete("all")
            
            # 加载原始图片
            image_path = self.image_list[self.current_image_index]
            try:
                original_image = Image.open(image_path)
                
                # 调整图片大小以适应画布
                canvas_width = self.canvas.winfo_width() or 500
                canvas_height = self.canvas.winfo_height() or 400
                
                img_width, img_height = original_image.size
                scale = min(canvas_width/img_width, canvas_height/img_height) * 0.9
                new_width = int(img_width * scale)
                new_height = int(img_height * scale)
                
                resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)
                
                # 添加水印
                watermarked_image = self.add_watermark(resized_image.copy())
                
                # 转换为tkinter可以显示的格式
                self.preview_photo = ImageTk.PhotoImage(watermarked_image)
                
                # 在画布中央显示图片
                x = (canvas_width - new_width) // 2
                y = (canvas_height - new_height) // 2
                self.canvas.create_image(x, y, anchor=tk.NW, image=self.preview_photo)
                
            except Exception as e:
                self.canvas.create_text(250, 200, text=f"无法加载图片: {str(e)}", fill="red")
                
    def add_watermark(self, image):
        if self.watermark_settings["type"] == "text":
            return self.add_text_watermark(image)
        else:
            return self.add_image_watermark(image)
            
    def add_text_watermark(self, image):
        # 添加文本水印
        draw = ImageDraw.Draw(image)
        
        try:
            # 尝试使用指定字体
            font = ImageFont.truetype(self.watermark_settings["font"], self.watermark_settings["size"])
        except:
            # 如果指定字体不可用，尝试使用中文字体
            try:
                font = get_chinese_font(self.watermark_settings["size"])
            except:
                # 如果中文字体也不可用，使用默认字体
                font = ImageFont.load_default()
            
        text = self.watermark_settings["text"]
        color = self.watermark_settings["color"]
        opacity = self.watermark_settings["opacity"]
        
        # 计算文本大小
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # 计算水印位置
        img_width, img_height = image.size
        position = self.watermark_settings["position"]
        
        if position == "top-left":
            x, y = 10, 10
        elif position == "top-center":
            x, y = (img_width - text_width) // 2, 10
        elif position == "top-right":
            x, y = img_width - text_width - 10, 10
        elif position == "center-left":
            x, y = 10, (img_height - text_height) // 2
        elif position == "center":
            x, y = (img_width - text_width) // 2, (img_height - text_height) // 2
        elif position == "center-right":
            x, y = img_width - text_width - 10, (img_height - text_height) // 2
        elif position == "bottom-left":
            x, y = 10, img_height - text_height - 10
        elif position == "bottom-center":
            x, y = (img_width - text_width) // 2, img_height - text_height - 10
        elif position == "bottom-right":
            x, y = img_width - text_width - 10, img_height - text_height - 10
        else:  # custom
            x, y = self.watermark_settings["custom_x"], self.watermark_settings["custom_y"]
            
        # 应用透明度
        if color.startswith('#'):
            r, g, b = tuple(int(color[i:i+2], 16) for i in (1, 3, 5))
        else:
            r, g, b = 255, 0, 0
            
        alpha = int(255 * opacity / 100)
        rgba = (r, g, b, alpha)
        
        # 添加阴影效果
        if self.watermark_settings.get("shadow", False):
            shadow_offset = 2
            draw.text((x + shadow_offset, y + shadow_offset), text, font=font, fill=(0, 0, 0, alpha//2))
            
        # 添加描边效果
        if self.watermark_settings.get("stroke", False):
            # 简化的描边效果
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx != 0 or dy != 0:
                        draw.text((x + dx, y + dy), text, font=font, fill=(0, 0, 0, alpha//3))
                        
        # 绘制主要文本
        draw.text((x, y), text, font=font, fill=rgba)
        
        return image
        
    def add_image_watermark(self, image):
        # 添加图片水印
        if not self.watermark_settings["watermark_image_path"]:
            return image
            
        try:
            watermark = Image.open(self.watermark_settings["watermark_image_path"]).convert("RGBA")
            
            # 调整水印大小
            scale = self.watermark_settings["watermark_scale"] / 100
            w_width, w_height = watermark.size
            new_width = int(w_width * scale)
            new_height = int(w_height * scale)
            watermark = watermark.resize((new_width, new_height), Image.LANCZOS)
            
            # 应用透明度
            opacity = self.watermark_settings["opacity"]
            if opacity < 100:
                alpha = watermark.split()[3]  # 获取alpha通道
                alpha = alpha.point(lambda p: int(p * opacity / 100))
                watermark.putalpha(alpha)
                
            # 计算水印位置
            img_width, img_height = image.size
            w_width, w_height = watermark.size
            position = self.watermark_settings["position"]
            
            if position == "top-left":
                x, y = 10, 10
            elif position == "top-center":
                x, y = (img_width - w_width) // 2, 10
            elif position == "top-right":
                x, y = img_width - w_width - 10, 10
            elif position == "center-left":
                x, y = 10, (img_height - w_height) // 2
            elif position == "center":
                x, y = (img_width - w_width) // 2, (img_height - w_height) // 2
            elif position == "center-right":
                x, y = img_width - w_width - 10, (img_height - w_height) // 2
            elif position == "bottom-left":
                x, y = 10, img_height - w_height - 10
            elif position == "bottom-center":
                x, y = (img_width - w_width) // 2, img_height - w_height - 10
            elif position == "bottom-right":
                x, y = img_width - w_width - 10, img_height - w_height - 10
            else:  # custom
                x, y = self.watermark_settings["custom_x"], self.watermark_settings["custom_y"]
                
            # 粘贴水印
            image.paste(watermark, (x, y), watermark)
            
        except Exception as e:
            print(f"添加图片水印时出错: {e}")
            
        return image
        
    def select_watermark_image(self):
        file_path = filedialog.askopenfilename(
            title="选择水印图片",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff")]
        )
        
        if file_path:
            self.watermark_settings["watermark_image_path"] = file_path
            filename = os.path.basename(file_path)
            self.watermark_image_label.config(text=filename)
            self.update_preview()
            
    def select_export_folder(self):
        folder_path = filedialog.askdirectory(title="选择导出文件夹")
        if folder_path:
            self.export_folder = folder_path
            self.export_path_label.config(text=folder_path)
            
    def export_images(self):
        if not hasattr(self, 'export_folder'):
            messagebox.showerror("错误", "请先选择导出文件夹")
            return
            
        if not self.image_list:
            messagebox.showerror("错误", "没有要导出的图片")
            return
            
        # 获取导出设置
        naming_rule = self.naming_var.get()
        prefix = self.prefix_entry.get()
        suffix = self.suffix_entry.get()
        
        success_count = 0
        for image_path in self.image_list:
            try:
                # 打开原始图片
                original_image = Image.open(image_path)
                
                # 添加水印
                watermarked_image = self.add_watermark(original_image.copy())
                
                # 确定导出文件名
                filename = os.path.basename(image_path)
                name, ext = os.path.splitext(filename)
                
                if naming_rule == "prefix":
                    new_filename = prefix + name + ext
                elif naming_rule == "suffix":
                    new_filename = name + suffix + ext
                else:  # original
                    new_filename = filename
                    
                # 保存图片
                export_path = os.path.join(self.export_folder, new_filename)
                watermarked_image.save(export_path)
                success_count += 1
                
            except Exception as e:
                print(f"导出 {image_path} 时出错: {e}")
                
        messagebox.showinfo("完成", f"成功导出 {success_count} 张图片")
        
    def save_template(self):
        template_name = tk.simpledialog.askstring("保存模板", "请输入模板名称:")
        if template_name:
            template = {
                "name": template_name,
                "settings": self.watermark_settings.copy()
            }
            self.templates.append(template)
            self.save_templates()
            messagebox.showinfo("成功", f"模板 '{template_name}' 已保存")
            
    def manage_templates(self):
        # 这里应该打开一个新窗口来管理模板
        # 为了简化，我们只显示一个简单的对话框
        if not self.templates:
            messagebox.showinfo("模板管理", "暂无保存的模板")
            return
            
        template_names = [t["name"] for t in self.templates]
        selected_name = tk.simpledialog.askstring(
            "选择模板", 
            "可用模板:\n" + "\n".join(template_names) + "\n\n请输入要加载的模板名称:"
        )
        
        if selected_name:
            for template in self.templates:
                if template["name"] == selected_name:
                    self.load_template(template)
                    messagebox.showinfo("成功", f"已加载模板 '{selected_name}'")
                    return
            messagebox.showerror("错误", "未找到指定的模板")
            
    def load_template(self, template):
        self.watermark_settings.update(template["settings"])
        
        # 更新UI元素
        self.text_entry.delete(0, tk.END)
        self.text_entry.insert(0, self.watermark_settings["text"])
        
        self.size_var.set(self.watermark_settings["size"])
        self.opacity_var.set(self.watermark_settings["opacity"])
        self.scale_var.set(self.watermark_settings["watermark_scale"])
        
        self.color_button.config(bg=self.watermark_settings["color"])
        self.color_label.config(text=self.watermark_settings["color"])
        
        self.watermark_type_var.set(self.watermark_settings["type"])
        self.update_watermark_type()
        
        if self.watermark_settings["watermark_image_path"]:
            filename = os.path.basename(self.watermark_settings["watermark_image_path"])
            self.watermark_image_label.config(text=filename)
            
        self.update_preview()
        
    def save_templates(self):
        try:
            with open("templates.json", "w", encoding="utf-8") as f:
                json.dump(self.templates, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存模板时出错: {e}")
            
    def load_templates(self):
        try:
            if os.path.exists("templates.json"):
                with open("templates.json", "r", encoding="utf-8") as f:
                    self.templates = json.load(f)
        except Exception as e:
            print(f"加载模板时出错: {e}")
            self.templates = []

def main():
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()