# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:10:53 2024

@author: Hi
"""

n=int(input('Nhập số nguyên dương n= '))
chinh_phuong=False
for i in range(1,n+1):
    if i*i==n:
        chinh_phuong=True
        break
    elif i*i>n:
        break
if chinh_phuong:
    print(f'{n} là số chính phương')
else:
    print(f'{n} không phải là số chính phương')