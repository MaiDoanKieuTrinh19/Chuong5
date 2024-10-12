# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 18:16:44 2024

@author: Hi
"""

nho_nhat=979
A=[]
for x in range(1,485):
    for y in range(1,140):
        for z in range(1,109):
            if 2*x+7*y+9*z==979:
                if x+y+z<nho_nhat:
                    nho_nhat = x + y + z
                    A=[(x, y, z)]
print(f'Bộ nghiệm {A} với tổng x+y+z nhỏ nhất là: {nho_nhat}')             
               
                    
                    