#!/usr/bin/env python
#coding: utf-8
'''

第 0008 题：一个HTML文件，找出里面的正文。
'''
from goose import Goose
from goose.text import StopWordsChinese
#import sys
#reload(sys)
#sys.setdefaultcoding('utf-8')

#要分析的网页
url = 'http://www.ruanyifeng.com/blog/2015/05/thunk.html'
url1 = 'https://blog.csdn.net/huangxiongbiao/article/details/45557631'

def extarct_url(url):
    g = Goose({'stopwords_class': StopWordsChinese})
    article = g.extract(url=url)
    return article.cleaned_text


if __name__ == '__main__':
    print(extarct_url(url1))
   # print('\n')