#!/usr/bin/env python
#coding: utf-8
import redis
import randomKey

HOST = 'localhost'
PORT = 6379

#连接到数据库
r = redis.Redis(HOST,PORT)
#生成200组激活码
codelist = randomKey.generate(200)
#将生成的激活码存入数据库中
for i in xrange(200):
    r.sadd("code",codelist[i])
r.save()