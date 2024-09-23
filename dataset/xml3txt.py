import os, shutil, random
random.seed(0)
import numpy as np
from sklearn.model_selection import train_test_split

val_size = 0.1           #验证集
test_size = 0.2         #测试集
postfix = 'jpg'         #图片后缀
imgpath = 'D:\\workspace\\dataset\\PCB_DATASET\\Jpg\\allinall'
txtpath = 'D:\\workspace\\dataset\\PCB_DATASET\\txt'

os.makedirs('D:\\workspace\\dataset\\PCB_DATASET\\images\\train', exist_ok=True)
os.makedirs('D:\\workspace\\dataset\\PCB_DATASET\\images\\val', exist_ok=True)
os.makedirs('D:\\workspace\\dataset\\PCB_DATASET\\images\\test', exist_ok=True)
os.makedirs('D:\\workspace\\dataset\\PCB_DATASET\\labels\\train', exist_ok=True)
os.makedirs('D:\\workspace\\dataset\\PCB_DATASET\\labels\\val', exist_ok=True)
os.makedirs('D:\\workspace\\dataset\\PCB_DATASET\\labels\\test', exist_ok=True)

listdir = np.array([i for i in os.listdir(txtpath) if 'txt' in i])
random.shuffle(listdir)
train, val, test = listdir[:int(len(listdir) * (1 - val_size - test_size))], listdir[int(len(listdir) * (1 - val_size - test_size)):int(len(listdir) * (1 - test_size))], listdir[int(len(listdir) * (1 - test_size)):]
print(f'train set size:{len(train)} val set size:{len(val)} test set size:{len(test)}')


# print(os.listdir(imgpath))

for i in train:
    shutil.copy('{}/{}.{}'.format(imgpath, i[:-4], postfix), 'D:\\workspace\\dataset\\PCB_DATASET\\images/train/{}.{}'.format(i[:-4], postfix))
    shutil.copy('{}/{}'.format(txtpath, i), 'D:\\workspace\\dataset\\PCB_DATASET\\labels/train/{}'.format(i))
   
    

for i in val:
    shutil.copy('{}/{}.{}'.format(imgpath, i[:-4], postfix), 'D:\\workspace\\dataset\\PCB_DATASET\\images/val/{}.{}'.format(i[:-4], postfix))
    shutil.copy('{}/{}'.format(txtpath, i), 'D:\\workspace\\dataset\\PCB_DATASET\\labels/val/{}'.format(i))

for i in test:
    shutil.copy('{}/{}.{}'.format(imgpath, i[:-4], postfix), 'D:\\workspace\\dataset\\PCB_DATASET\\images/test/{}.{}'.format(i[:-4], postfix))
    shutil.copy('{}/{}'.format(txtpath, i), 'D:\\workspace\\dataset\\PCB_DATASET\\labels/test/{}'.format(i))

