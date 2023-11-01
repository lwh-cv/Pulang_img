import Augmentor
from PIL import Image
import os

# 确定原始图像存储路径以及掩码文件存储路径，需要把“\”改成“/”
p = Augmentor.Pipeline("./JPEGImages1")
p.ground_truth("./SegmentationClass1")
 
# 图像旋转： 按照概率0.8执行，范围在0-25之间
p.rotate(probability=0.8, max_left_rotation=25, max_right_rotation=25)

# 图像左右互换： 按照概率0.5执行
p.flip_left_right(probability=0.5)
p.flip_top_bottom(probability=0.5)
 
# 图像放大缩小： 按照概率0.8执行，面积为原始图0.85倍
#p.zoom_random(probability=0.3, percentage_area=0.85)
 
#scale_factor表示缩放比例，只能大于1，且为等比放大。
p.scale(probability=1, scale_factor=1.3)
 
#小块变形
p.random_distortion(probability=0.8,grid_width=10,grid_height=10, magnitude=20)
 
#随机亮度增强/减弱，min_factor, max_factor为变化因子，决定亮度变化的程度，可根据效果指定
p.random_brightness(probability=1, min_factor=0.7, max_factor=1.2)
 
#随机颜色/对比度增强/减弱
#p.random_color(probability=1, min_factor=0.0, max_factor=1)
#p.random_contrast(probability=1, min_factor=0.7, max_factor=1.2)
 
#随机剪切(shear)  max_shear_left，max_shear_right为剪切变换角度  范围0-25
#p.shear(probability=1, max_shear_left=10, max_shear_right=10)
 
#随机裁剪(random_crop)
#p.crop_random(probability=1, percentage_area=0.8, randomise_percentage_area=True)
 
#随机翻转(flip_random)
#p.flip_random(probability=1)
 
# 最终扩充的数据样本数可以更换为100。1000等
p.sample(200)  