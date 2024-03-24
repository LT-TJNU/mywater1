import os
from PIL import Image
from tqdm import tqdm

# 定义输入和输出文件夹路径
# 定义输入和输出文件夹路径
input_folder = r'G:\watertest\train_set\Image'  # 修改为你的PNG图片所在文件夹路径
output_folder = r'E:\watertest\deeplabv3-plus-pytorch-main\deeplabv3-plus-pytorch-main\VOCdevkit\VOC2007\JPEGImages'  # 修改为你想要保存JPG图片的文件夹路径


# 确保输出文件夹存在，如果不存在则创建
os.makedirs(output_folder, exist_ok=True)

# 获取文件列表
file_list = [filename for filename in os.listdir(input_folder) if filename.endswith('.png')]

# 使用tqdm显示转换进度
for filename in tqdm(file_list, desc='Converting images'):
    # 构建输入和输出文件的完整路径
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, filename[:-4] + '.jpg')  # 将文件后缀修改为.jpg

    # 打开PNG图片并保存为JPG格式
    img = Image.open(input_path)
    img.convert('RGB').save(output_path, 'JPEG')

print('Conversion completed.')
