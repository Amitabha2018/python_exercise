#!/usr/bin/env python
# -*- coding:utf-8 -*-  
__author__ = 'IT小叮当'
__time__ = '2019-11-21 20:03'
'''
可逆素数：指一个素数的各位数值顺序颠倒后得到的数仍为素数，如113-->311
用python找出1-900之间所有的可逆素数
'''
#1.用筛选法找到900以内的素数
#2.迭代表内所有数，是素数则检测它的反序数是否是素数
#3. 2条件为真，打印这俩个素数

def getPrimeList(n):
    pl = [True]*n
    res_pl = []
    for p in range(2,n):
        if not pl[p]:continue
        res_pl.append(p)
        for i in range(p*p,n,p):
            pl[i] = False

    return res_pl

res_pl = getPrimeList(900)
reversible_prime = []
#反序数两位数以上才有意义
for p  in res_pl:
    #反序数
    q = int(str(p)[::-1])
    if (p != q) and (q in res_pl):
        reversible_prime.append((p,q))
        res_pl.remove(q)
print(reversible_prime)

