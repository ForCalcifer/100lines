#!/usr/bin/env python
#coding: utf-8
import pymysql
import randomKey

HOST =  '192.168.0.129'
USER = 'root'
PASSWORD = '1q@W3e4r'
PORT = 3306
DB = 'mysql'
#连接数据库
conn = pymysql.connect(
    host =HOST,
    user=USER,
    passwd=PASSWORD,
    db=DB,
    port=PORT)
cur = conn.cursor()

#生成200组激活码
codelist = randomKey.generate(2)
#将生成的激活码插入到表中
for i in xrange(2):
    sql = "INSERT INTO Code VALUE ('%d', '%s')"
    data = (i, codelist[i])
    cur.execute(sql % data)

conn.commit()
cur.close()
conn.close()