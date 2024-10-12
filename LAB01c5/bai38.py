# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:23:15 2024

@author: Hi
"""

n=int(input('Nhập số nguyên lẻ dương n= '))
while n<=0 or n%2==0:
    n=int(input('Bạn đã nhập sai. Vui lòng nhập lại số nguyên lẻ dương n= '))
s=1
for i in range(1, n+1):
    s=s*i
print(f'Tích của dãy số  từ 1 đến {n} là: {s}')