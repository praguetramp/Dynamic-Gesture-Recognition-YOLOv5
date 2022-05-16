import cv2
import os
import copy

# 数据增强-- 镜像翻转
# 新数据量 = 原数据量的2倍
def DataAugment (dir_path):
    if not os.path.exists(dir_path):
        print('路径不存在')
    else:
        dirs = os.listdir(dir_path)

        for subdir in dirs:  # 获取图像
            sub_dir = dir_path + '/' + subdir
            img = cv2.imread(sub_dir)

            size = img.shape

            # 深度复制
            ilr = copy.deepcopy(img)
            h = size[0]
            w = size[1]
            # 几何运算，实现镜像翻转
            for i in range(h):
                for j in range(w):
                    ilr[i, w - 1 - j] = img[i, j]

            # 保存的文件路径
            new_name = "../augment/picture/"+subdir
            cv2.imwrite(new_name, ilr)
    print("success!")


DataAugment(r"C:\Users\XXXX\Desktop\train_png")
