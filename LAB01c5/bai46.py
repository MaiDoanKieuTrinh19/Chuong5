# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:18:24 2024

@author: Hi
"""
danhsach=[]
for x in range(1,485):
    for y in range(1,140):
        for z in range(1,109):
            if 2*x+7*y+9*z==979:
                danhsach+=[(x,y,z)]
for i in danhsach:
               print('Bộ nghiệm của phương trình 2x+7y+9z=979 là: ',i)
    

