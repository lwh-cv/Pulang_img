from PIL import Image
import os

# 自定义一个函数，用于将图像转换为RGB模式
def convert_to_rgb(image):
    if image.mode != 'RGB':
        image = image.convert('RGB')
    return image

# 指定原始图像文件夹路径和目标文件夹路径
original_folder = "./SegmentationClass"  # 原始图像文件夹路径
target_folder = "./SegmentationClass1"  # 目标文件夹路径

# 遍历原始图像文件夹中的所有图片
for filename in os.listdir(original_folder):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        # 拼接原始图像文件路径和目标文件路径
        original_path = os.path.join(original_folder, filename)
        target_path = os.path.join(target_folder, filename)
        
        # 加载原始图像
        image = Image.open(original_path)
        
        # 将图像转换为RGB模式
        image = convert_to_rgb(image)
        
        # 保存转换后的图像到目标文件夹
        image.save(target_path)
        print(f"Converted {filename} to RGB and saved to {target_path}")
