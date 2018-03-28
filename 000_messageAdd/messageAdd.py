#!/usr/bin/env python
# encoding: utf-8


'''from PIL import Image, ImageDraw, ImageFont, ImageColor
def add_num(img, txt):
    # 创建一个Draw对象
    draw = ImageDraw.Draw(img)
    # 创建一个 Font, mac下字体不支持会导致乱码，暂时不知道哪种支持中文
    myfont = ImageFont.truetype('Library/Fonts/Verdana.ttf', size=40)
    fillcolor = ImageColor.colormap.get('red')
    width, height = img.size
    draw.text((width-100, 0), txt, font=myfont, fill=fillcolor)
    img.save('images/result.jpg', 'jpeg')
    return 0
if __name__ == '__main__':
   # image = Image.open('images/TLG.jpeg')
    add_num(image, 'TLG')'''

from PIL import Image,ImageFont,ImageDraw

def add_num(in_file, txt, out_file):
    img = Image.open(in_file)
    font = ImageFont.truetype('Library/Fonts/Verdana.ttf', 50)
    #fill_color = '#ff0000'
    fill_color = 'red'
    draw = ImageDraw.ImageDraw(img)
    width, height = img.size
    draw.text((width-120, 0), txt, fill=fill_color, font=font)
    img.save(out_file)
    return 0;

if __name__ == '__main__':
    add_num('images/TLG.jpeg', 'TLG', 'images/TLM.jpeg')




