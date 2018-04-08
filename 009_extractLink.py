#!/usr/bin/env python
#coding: utf-8
'''
第 0009 题：一个HTML文件，找出里面的链接。

'''
from bs4 import BeautifulSoup
import urllib
import urllib2

# 要分析的网页
url = 'http://www.ruanyifeng.com/blog/2015/05/co.html'

def extractl_link(url):
    proto, rest = urllib.splittype(url)
    domain = urllib.splithost(rest)[0]

    print "startwith %s\t%s\t%s:" % (proto, rest, domain)
    html = urllib2.urlopen(url).read()

    a = BeautifulSoup(html).findAll('a')

    #for i in a:
    alist = [i.attrs['href'] for i in a if i.attrs['href'][0] != 'j']
        #if i.attrs['href'][0] != 'h':
    alist = map(lambda i: proto + '://' + domain + i if i[0] == '/' else url + i if i[0] == '#' else i, alist)

            #print i.attrs['href']
    return alist

if __name__ == '__main__':
    a = extractl_link(url)
    for i in a:
        print(i)
