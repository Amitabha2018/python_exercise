#!/usr/bin/env python
# -*- coding:utf-8 -*-  
__author__ = 'IT小叮当'
__time__ = '2019-11-17 19:31'
#水仙花数
'''
指一个n位数（n>=3),它的每个位上的数字的n次幂之和等于它本身
1^3+5^3+3^3=153
用python求100-999之间的所有水仙花数
水仙花数（Narcissistic number）也被称为超完全数字不变数（pluperfect digital invariant, PPDI）、
自恋数、自幂数、阿姆斯壮数或阿姆斯特朗数（Armstrong number）
'''
def isNarcissusNumber(n):
    p = []
    t = n
    while t > 0:
        p.append(t % 10)
        t //= 10
    l = len(p)
    # s = 0
    # for j in p:
    #     s += j ** l
    #
    # return s==n
    return sum([j**l for j in p]) == n

for i in range(100,999):
    if isNarcissusNumber(i):
        print(i)







