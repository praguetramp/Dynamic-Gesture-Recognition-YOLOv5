
from keras.preprocessing.image import ImageDataGenerator

# 数据增强-- 空间旋转--随机角度
#  每次生成的数据  数据量为 batch_size * range(n) 的乘积

path = r"C:\Users\XXXX\Desktop\picture"
des_path = r"C:\Users\XXXX\Desktop\augment\picture"
datagen = ImageDataGenerator(rotation_range=40,
                             # width_shift_range = 0.02,
                             # height_shift_range = 0.02,
                             # shear_range = 0.02,
                             # horizontal_flip = False,
                             vertical_flip=True
                             )

gen = datagen.flow_from_directory(path,
                                  target_size=(224, 224),
                                  # 数据量为批次的整数倍
                                  batch_size=30,
                                  # 生成后的图像保存路径
                                  save_to_dir=des_path,
                                  # 生成的文件的 文件名前缀(方便区分) 和 文件格式
                                  save_prefix='n',
                                  save_format='png')

for i in range(10):
    gen.next()

print('success!')


