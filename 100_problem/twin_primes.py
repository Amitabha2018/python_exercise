#!/usr/bin/env python
# -*- coding:utf-8 -*-  
__author__ = 'IT小叮当'
__time__ = '2019-11-20 22:32'
'''
若两个素数之差为2，则这两个素数就是孪生素数,用python找出1~100之间的所有孪生素数
'''#筛选找素数
#1.建一张表，用true,false 标识一个数是否是素数
#2.找到一个素数p,然后把p的倍数都标记成非素数
#3.查表检测p+1,如果非素数检测下一个，是素数执行1的操作

#2的倍数 4,6,8,10
#3的倍数 9,12,15
#4的倍数 16,20
#初始化表
pl = [True] * 100
p_res = []

#找出1，100内的素数
for p in range(2,100):
    #如果不是素数，继续查找
    if not pl[p]:continue
    #是素数存到素数表
    p_res.append(p)
    #筛掉非素数
    for i in range(p*p,100,p):
        pl[i] = False


#存放孪生素数
twin_prime = []
for i in range(1,len(p_res)):
    if p_res[i]-p_res[i-1] == 2:
        twin_prime.append((p_res[i-1],p_res[i]))

print(twin_prime)