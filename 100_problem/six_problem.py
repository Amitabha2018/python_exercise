#!/usr/bin/env python
# -*- coding:utf-8 -*-  
__author__ = 'IT小叮当'
__time__ = '2019-11-16 19:13'
#问题描述
'''
求一个自然数N，个位数是6,将6提到最前面所得数是N的4倍
'''

#解题思路：
'''
1.令末尾数e = 6 ,其余除末尾部分为n
2.e左移位数*10，加n得到新数
3.根据题目建立等量关系
e_n = 4 * N
例如 1236--->6123 == 1236*4 
'''

def seek_N(n):
    num = n
    e = 6
    while num > 0:
        e *= 10
        num //= 10

    m = 10*n + 6

    if e + n == m * 4:
        print(m)

for x in range(1,100000):
    seek_N(x)