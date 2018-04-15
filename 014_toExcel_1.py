#/!usr/bin/env python
#encoding: utf-8
'''
第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}
'''
import xlwt
import json
import os
from collections import OrderedDict

#存放文件的路径
file_path = '/Users/calcifer/'

def run():
    os.chdir(file_path)
    with open('student.txt') as f:
        content = f.read()
        #print (content)
    #转为json
    jsoncontent = json.loads(content, object_pairs_hook=OrderedDict)

    '''print(jsoncontent)
       无序output:{u'1': [u'\u5f20\u4e09', 150, 120, 100], u'3': [u'\u738b\u4e94', 60, 66, 68], u'2': [u'\u674e\u56db', 90, 99, 95]}
        加上OrderedDict后：
        OrderedDict([(u'1', [u'\u5f20\u4e09', 150, 120, 100]), (u'2', [u'\u674e\u56db', 90, 99, 95]), (u'3', [u'\u738b\u4e94', 60, 66, 68])])
    '''
    excelfile = xlwt.Workbook()
    # 添加sheet
    table = excelfile.add_sheet('student')
    #row是enumerate的index，从0开始；i指list中对应的value值
    for row, i in enumerate(list(jsoncontent)):
        print (row, i)
        #print ('\n')
        table.write(row, 0, i) #写在第0列: value=1
        for col, j in enumerate(list(jsoncontent[i])):
            table.write(row, col+1, j) #写在第0列第1行：value=张三
        excelfile.save('student.xls')

if __name__ == '__main__':
    run()