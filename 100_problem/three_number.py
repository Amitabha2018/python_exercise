#!/usr/bin/env python
# -*- coding:utf-8 -*-  
__author__ = 'IT小叮当'
__time__ = '2019-11-18 20:32'
'''
0-9这10个数字可以组成多少不重复的3位数
'''
#百位 h:1-9
#十位 j:0-9
#个位 k:0-9

h = range(1,10)
j = range(10)
count = 0
for a in h:
    for b in j:
        if a == b : continue
        for c in j:
            if c != a and c !=b :
                print(int(str(a)+str(b)+str(c)))
                count += 1
print('共有：'+str(count)+"个")