# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:54:46 2024

@author: Hi
"""
x=float(input('Nhập số x= '))
n=int(input('Nhập số nguyên dương n= '))
while n<=0:
    n=int(input('Số bạn đã nhập không phải là số nguyên dương. Vui lòng nhập lại số nguyên dương n= '))
S=0
M=0
for i in range(1,n+1):
    M+=i
    S+=(x**i)/M
print(f'Tổng của dãy là: {S}')
  