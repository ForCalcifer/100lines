#!/usr/bin/env python
#coding: utf-8
'''

第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
'''

import os, re

FILE_PATH = '/Users/calcifer/'

def analyze_code(srcfile):
    total_line = 0
    comment_line = 0
    blank_line = 0
    with open(srcfile) as f:
        lines = f.readlines()
        total_line = len(lines)
        print "总共%d行" % total_line
        line_index = 0
        #line = lines[line_index]
        #判断是否为注释行
        while line_index < total_line:
            line = lines[line_index]
            if line.startswith('#'):
                comment_line += 1
            elif re.match("\s*'''", line) is not None:
                comment_line += 1
                while re.match("'''.*\$", line):
                    line = lines[line_index]
                    comment_line += 1
                    line_index += 1
            elif line == "\n":
                blank_line += 1
            line_index += 1
    print "在%s中：" % srcfile
    print "代码行数：", total_line
    print "注释行数：", comment_line, "占%0.2f%%" % (comment_line * 100.0 / total_line)
    print "空行数：  ", blank_line, "占%0.2f%%" % (blank_line * 100.0 / total_line)
    return [total_line, comment_line, blank_line]

def run(FILE_PATH):
    os.chdir(FILE_PATH)
    # 遍历该目录下的py文件
    total_lines = 0
    total_comment_lines = 0
    total_blank_lines = 0
    for i in os.listdir(os.getcwd()):
        if os.path.splitext(i)[1] == '.py':
            line = analyze_code(i)
            total_lines, total_comment_lines, total_blank_lines = total_lines + line[0], total_comment_lines + line[
                1], total_blank_lines + line[2]
    print "总代码行数：", total_lines
    print "总注释行数：", total_comment_lines, "占%0.2f%%" % (total_comment_lines * 100.0 / total_lines)
    print "总空行数：  ", total_blank_lines, "占%0.2f%%" % (total_blank_lines * 100.0 / total_lines)


if __name__ == '__main__':
    run(FILE_PATH)