from glob import glob
import random
files = glob('/project/train/src_repo/helmet_data/*.txt')

train = open('train.txt', 'w')
val = open('val.txt', 'w')
for i in files:
    num = random.randint(1, 10)
    name = i.replace('.txt', '.jpg')
    if num < 2:
        val.write(name + '\n')
    else:
        train.write(name + '\n')
train.close()
val.close()