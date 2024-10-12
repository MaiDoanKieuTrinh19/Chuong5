# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 16:21:17 2024

@author: Hi
"""
lon_nhat=0
A=[]
for x in range(1,485):
    for y in range(1,140):
        for z in range(1,109):
            if 2*x+7*y+9*z==979:
                if x+y+z>lon_nhat:
                    lon_nhat = x + y + z
                    A=[(x, y, z)]
print(f'Bộ nghiệm {A} với tổng x+y+z lớn nhất là: {lon_nhat}')
                
               
                    
                    