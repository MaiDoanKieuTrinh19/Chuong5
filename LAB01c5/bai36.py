# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:16:22 2024

@author: Hi
"""

n=int(input('Nhập số nguyên dương n= '))
while n<=0:
    n=int(input('Bạn đã nhập sai. Vui lòng nhập lại số nguyên dương n= '))
S=0
for i in range(1,n+1):
    S+= i**2
print(f'Tổng của bình phương dãy số từ 1 đến {n} là: {S} ')
