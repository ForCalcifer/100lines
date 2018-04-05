#!/usr/bin/env python
# coding: utf-8
'''
第 0006 题：你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
'''
import re, os
from collections import Counter

#目标文件所在目录
dstPath = '/Users/calcifer/'

def getCounter(dialy):
    #输入一个纯英文文件，统计其中单词出现的次数
    pattern = r'''[a-zA-Z]+|\$?\d+%?$'''
    with open(dialy) as f:
        r = re.findall(pattern, f.read())
        return Counter(r)

#过滤词
stop_word = ['the', 's','in', 'of', 'and', 'to', 'has', 'that', 's', 'is', 'are', 'a', 'with', 'as', 'an']

def run(dstPath):
    #切换到目标所在目录
    os.chdir(dstPath)
    #遍历该文件下的txt文件
    total_counter = Counter()
    for i in os.listdir(os.getcwd()):
        if os.path.splitext(i)[1] == '.py':
            total_counter += getCounter(i)

    for i in stop_word:
        total_counter[i] = 0

    #Counter.most_common输出计数不为0的值,Counter[0]:('filePath', 72);Counter[0][0]:filePath
    print(total_counter.most_common()[0][0])


if __name__ == '__main__':
    run(dstPath)

