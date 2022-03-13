# _*_ coding:utf-8 _*_
import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import cv2
import logging
from glob import glob
import time
'''
YOLO v5 
xml -> txt
'''

class2id = {"person": 0, "hat": 1, "head": 2}
def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    x = min(x, 1.0)
    y = min(y, 1.0)
    w = min(w, 1.0)
    h = min(h, 1.0)
    
    return (x,y,w,h)
 
def convert_annotation(image_path):
    in_file = open(image_path.replace('.xml', '.xml'),encoding="utf-8")
    out_file = open(image_path.replace('.xml', '.txt'), 'w')
    # print(in_file)
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    # img = cv2.imread("./datasets/VOCdevkit/VOC2007/JPEGImages/"+image_id+".jpg")
    # sp = img.shape

    for obj in root.iter('object'):
        name = obj.find('name').text
        cls_id = class2id[name]
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b,)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

files = glob('./helmet_data/*.xml')

if __name__ == '__main__':
    for file in files:
        print(file)
        convert_annotation(file)

