#!/usr/bin/env python
# -*- coding:utf-8 -*-  
__author__ = 'IT小叮当'
__time__ = '2019-11-19 22:06'
'''
如果某个数的平方的末尾几位等于这个数，那么就称这个数为自守数
例如5和6 5*5=25 6*6=36 25*25=625 76*76=5776 25和75也是自守数
用python 求10000以内的自守数
'''
#1.计算n的长度l
#2.取n*n的后l位b
#3. n==b ?
# n=1234
# count = 0
# while n > 0:
#     count+=1
#     n //= 10

for i in range (1,10000):
    l = len(str(i))
    b = i*i % (10**l)
    if b == i:
       print(i)


x = [j for j in range(1,10000) if j*j %(10 ** len(str(j)))==j]
print(x)