#!/usr/bin/env python
#encoding: utf-8
'''

'''
from PIL import Image,ImageDraw,ImageFont,ImageFilter  
import random  
  
def rndColor():  #产生随机颜色  
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))  
  
def rndChar():  #产生随机字母  
    return chr(random.randint(65,90))  
def rndColor2():   
    return (random.randint(30,120),random.randint(30,120),random.randint(30,120))  
  
height=60  
width=240  
image=Image.new('RGB',(width,height),(255,255,255))  #白色画布  
font=ImageFont.truetype("Arial.ttf",36)        #画笔字体  
draw=ImageDraw.Draw(image)   #绘画对象  
for i in range(width):  
    for j in range(height):  
        draw.point((i,j),fill=rndColor())     #随机逐像素填充颜色  
  
for i in range(4):  
    draw.text((60*i+10,10),rndChar(),font=font,fill=rndColor2())  #文本绘画  
  
image=image.filter(ImageFilter.BLUR)  #产生模糊感  
image.save('code.jpg','jpeg')  
image.show()  
