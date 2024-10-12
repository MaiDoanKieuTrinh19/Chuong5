# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 19:52:15 2024

@author: Hi
"""
N=int(input('Nhập số nguyên dương N= '))
while N<0:
    N=int(input('Vui lòng nhập số NGUYÊN DƯƠNG N= '))
print('N=',N)
tong_cac_so=0
while N>0:
    so_cuoi= N % 10
    N=N//10
    tong_cac_so +=so_cuoi
print('Tống các chữ số của N là',tong_cac_so)

