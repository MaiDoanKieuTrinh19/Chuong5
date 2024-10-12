# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:19:21 2024

@author: Hi
"""

n=int(input('Nhập số nguyên chẵn dương n= '))
while n<=0 or n%2!=0:
    n=int(input('Bạn đã nhập sai. Vui lòng nhập lại số nguyên chẵn dương n= '))
s=0
for i in range(2, n+1, 2):
    s+=i
print(f'Tổng của dãy số chẵn từ 2 đến {n} là: {s}')
    
    