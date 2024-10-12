# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:16:24 2024

@author: Hi
"""
N=0
T=0
while T<1 or T>12:
    T=int(input('Nhập tháng: '))
    if T<1 or T>12:
        print('Tháng không hợp lệ. Vui lòng nhập lại.')
N=int(input('Nhập năm: '))
if T in [1, 3, 5, 7, 8, 10, 12]:
    day=31
elif T in [4, 6, 9, 11]:
    day=30
else:
    if (N%4==0 and N%100!=0) or N%400==0:
        day=29
    else:
        day=28
print(f'Tháng {T} năm {N} có {day} ngày')
 