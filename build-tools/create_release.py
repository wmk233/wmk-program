import os
import zipfile

def create_zip():
    print("正在创建发布包...")
    print("当前目录:", os.getcwd())
    
    # 检查目录是否存在
    if not os.path.exists('watermark-tool-v1.0.0-release'):
        print("❌ 错误: 发布目录不存在")
        return
    
    # 显示目录内容
    print("发布目录内容:")
    for root, dirs, files in os.walk('watermark-tool-v1.0.0-release'):
        for file in files:
            print(f"  {os.path.join(root, file)}")
    
    # 创建zip文件
    with zipfile.ZipFile('watermark-tool-v1.0.0.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        # 遍历目录中的所有文件
        for root, dirs, files in os.walk('watermark-tool-v1.0.0-release'):
            for file in files:
                file_path = os.path.join(root, file)
                # 添加文件到zip，保持目录结构
                arc_name = os.path.relpath(file_path, 'watermark-tool-v1.0.0-release')
                zipf.write(file_path, arc_name)
                print(f"已添加: {arc_name}")
    
    print("✅ 发布包已创建: watermark-tool-v1.0.0.zip")

if __name__ == "__main__":
    create_zip()