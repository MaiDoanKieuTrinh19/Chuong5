# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:48:25 2024

@author: Hi
"""

N=int(input('Nhập số nguyên dương N= '))
while N<=0:
   N=int(input('Nhập lại số NGUYÊN DƯƠNG N= '))
print('Số nguyên dương N= ',N)
uoc=[i for i in range(1,N+1) if N%i == 0]
print('Tất cả các ước của N là:', '\n',uoc)
