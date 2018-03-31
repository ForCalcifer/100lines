#coding: utf-8
#第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
#Auther: wjsaya
from random import choice
import string
import pymysql.cursors

def get_code(dict, length, count):
#根据给定字典，长度来得出激活码
    for i in range(1,int(count)+1):
        code = ""
    #通过count限制激活码个数，循环调用choice来计算激活码
        for l in range(0,int(length)):
            code = code+str(choice(dict))
        save_to_mysql(i, code)

def save_to_mysql(id, code):
#保存到mysql数据库
    host = ("192.168.0.126")
    user = ("root")
    pass_ = ("1q@W3e4r")
    db = ("mysql")
    #设置数据库连接相关信息
    connect = pymysql.connect(host, user, pass_, db)
    cursor = connect.cursor()
    #链接数据库并设置游标
    sql = "insert into Code value ('%d', '%s')"
    data = (id, code)
    cursor.execute(sql % data)
    connect.commit()
    '''尼玛要提交呀兄弟。。。'''
    r = cursor.fetchall()
    for a in r:
        codeid = a[0]
        codenumber = a[1]
        print ('%d\t%s'%(codeid, codenumber))
    #执行sql语句

if __name__ == "__main__":
    dict = string.letters+string.digits
    #设定字典为'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = input("请输入激活码个数：")
    if count == "":
        count = "1"
    length = input("请输入激活码长度：")
    if length == "":
        length = "8"
    get_code(dict, length, count)

