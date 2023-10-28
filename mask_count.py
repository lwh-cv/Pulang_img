from PIL import Image

# 加载掩码图像
mask_image = Image.open('./predict_result/10_predict.png').convert('RGB')

# 获取图像尺寸
width, height = mask_image.size

# 创建颜色计数字典
color_counts = {}

# 遍历图像像素
for y in range(height):
    for x in range(width):
        # 获取像素的RGB颜色值
        r, g, b = mask_image.getpixel((x, y))

        # 组合RGB颜色值为元组
        color = (r, g, b)

        # 更新颜色计数
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

# 打印每种颜色像素点的个数
for color, count in color_counts.items():
    print(f"颜色 {color} 的像素点个数为: {count}")
