#coding: utf-8

from random import choice
import string

def get_code(dict, length, count):
    for i in range(0, int(count)+1):
        code = ""
        for l in range(0, int(length)):
            code = code + str(choice(dict))
        print (code)

if __name__ == "__main__":
    dict = string.letters+string.digits
    count = input("请输入激活码个数：")
    if count == "":
        count = "1"
    length = input("请输入激活码长度：")
    if length == "":
        length = "8"

    get_code(dict, length, count)
'''
2018-03-30T15:12:18.306363Z 4 [Note] [MY-010454] A temporary password
is generated for root@localhost: ijmd=f2Xexdk

mysql

mysql> use mysql;

UPDATE user SET authentication_string=PASSWORD('root') WHERE user = 'root';

mysql> exit;
'''