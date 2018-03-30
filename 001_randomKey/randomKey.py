# encoding=utf-8
import random, string
'''
生成n组随机激活码

str = "-";
seq = ("a", "b", "c"); 
print str.join( seq ); // a-b-c

x = [i for i in list]
将一个 list 映射为另一个 list，每个元素设为变量i

random.sample()可以从指定的序列中，随机的截取指定长度的片断，不作原地修改
'''

filed = string.letters + string.digits


def get_random():
    return "".join(random.sample(filed, 4))


def concatenate(group):
    return "-".join([get_random()
                     for i in range(group)])


def generate(n):
    return [concatenate(4)
            for i in range(n)]

def printout(generate):
    for i in range(len(generate)):
        print(generate[i])


if __name__ == '__main__':
   # print(generate(10))
    printout(generate(10))






