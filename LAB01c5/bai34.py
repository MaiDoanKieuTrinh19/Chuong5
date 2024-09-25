# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 17:48:32 2024

@author: Hi
"""

n=int(input('Nhập số nguyên dương n= '))
if n<2:
    print(f'{n} không phải là số nguyên tố')
else:
    so_nguyen_to=True
    x=int(n**(1/2))
    for i in range(2,x+1):
        if n%i==0:
            so_nguyen_to=False
            break
if so_nguyen_to:
    print(f'{n} là số nguyên tố')
else:
    print(f'{n} không phải là số nguyên tố')
