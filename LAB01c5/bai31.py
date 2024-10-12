# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:30:33 2024

@author: Hi
"""

while True:
 a=int(input('Nhập só nguyên dương thứ nhất a= '))
 b=int(input('Nhập só nguyên dương thứ hai b= '))
 c=int(input('Nhập só nguyên dương thứ ba c= '))
 if a<=0 or b<=0 or c<=0:
    print('Tất cả các số phải là số NGUYÊN DƯƠNG. Vui lòng nhập lại.') 
    continue
 elif a+b>c and a+c>b and b+c>a:
    if a==b and b==c:
         print(f'Ba cạnh {a}, {b}, {c} là ba canh của tam giác đều')
    elif a==b or a==c or b==c:
         print(f'Ba cạnh {a}, {b}, {c} là ba canh của tam giác cân')
    elif a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
         print(f'Ba cạnh {a}, {b}, {c} là ba canh của tam giác vuông')
    else:
         print(f'Ba cạnh {a}, {b}, {c} là ba canh của tam giác thường')
    break
 else:
     print(f'Ba cạnh {a}, {b}, {c} không phải là ba canh của tam giác')     
    