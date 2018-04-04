#/usr/bin/env python
#coding: utf-8
from PIL import Image
import os

#源目录
myPath = '/Users/calcifer/Desktop/'
#输出目录
outPath = '/Users/calcifer/Desktop/Pictures/'

def processImg(srcimg, dstimg, name, imgtype):
    imgtype = 'png'
    #打开图片
    im = Image.open(srcimg + name)
    #缩放比例
    rate = max(im.size[0]/640.0 if im.size[0]/640 > 0 else 0,
               im.size[1]/1164.0 if im.size[1]/1164.0 > 0 else 0)
    if rate:
        im.thumbnail((im.size[0]/rate, im.size[1]/rate))
    im.save(dstimg+name, imgtype)

def run():
    os.chdir(myPath)
    for i in os.listdir(os.getcwd()):
        postfix = os.path.splitext(i)[1]
        if postfix == '.png':
            processImg(myPath, outPath, i, postfix)

if __name__=='__main__':
    run()


