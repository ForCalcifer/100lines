#!/usr/bin/env python
#coding: utf-8
import re
from collections import Counter
FILESOURCE = '/Users/Calcifer/threadcp.py'

def getMostCommonWord(articlefilesource):
    '''输入一个英文的纯文本文件，统计其中的单词出现的个数'''
    #pattern = r'''[A-Za-z]+|\$?\d+%?$'''
    pattern = r'''[a-zA-Z]+|\$?\d+%?$'''
    with open(articlefilesource) as f:
        r = re.findall(pattern,f.read())
        #print(r)
        return Counter(r).most_common()

if __name__ == '__main__':
    print getMostCommonWord(FILESOURCE)