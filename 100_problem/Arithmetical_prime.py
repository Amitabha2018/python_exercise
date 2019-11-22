#!/usr/bin/env python
# -*- coding:utf-8 -*-  
__author__ = 'IT小叮当'
__time__ = '2019-11-22 18:48'
'''
类似7、37、67、97、127、157、187，这样由素数组成的数列，叫做等差数列。
素数数列具有项数的限制，一般指素数数列的项数有多少个连续项，最多可以存在多少个连续项。
python编程找出100以内的等差素数数列。
'''
#1.筛选法找到100内的所有素数
#2.对于素数list内数两两组合，构造等差数列a0,a1项
#3.计算a2,查表判断a2是否是素数，是素数则能构成素数等差序列，计算a3...

def findPrime(n):
    pl = [True] * n
    pl_res = []

    for p in range(2,n):
        if not pl[p]:continue
        pl_res.append(p)
        for i in range(p*p,n,p):
            pl[i] = False

    return pl_res

p100 = findPrime(100)

for i in range(len(p100)):
    for j in range(i+1,len(p100)):
        a0,a1 = p100[i],p100[j]
        an = a1+a1-a0
        s=[]
        while (an in p100):
            s.append(an)
            an += a1-a0
        if s:
            print([a0,a1]+s)