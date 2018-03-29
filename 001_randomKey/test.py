'''
[]作为list集合需要用在return上
'''
# encoding=utf-8
import string, random

filed = string.letters + string.digits

def get_random():
    return "".join(random.sample(filed, 4))

def get_key(n):
    return "-".join([get_random()
                    for i in range(n)])

def get_group(n):
    return [get_key(5)
            for i in range(n)]


if __name__=='__main__':
    print(get_group(10))
