# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:41:53 2024

@author: Hi
"""

n=int(input('Nhập số nguyên dương n= '))
while n<=0:
    n=int(input('Số bạn đã nhập không phải là số nguyên dương. Vui lòng nhập lại số nguyên dương n= '))
s=0
for i in range(1,n+1):
    s+=1/(i*(i+1))
print(f'Tổng của dãy 1/(1*2)+1/(2*3)+..+1/n*(n+1) là: {round(s,3)}')
