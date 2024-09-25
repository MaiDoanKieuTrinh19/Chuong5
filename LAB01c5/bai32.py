# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:21:38 2024

@author: Hi
"""

km=-1
while km!=0:
    km= float(input('Nhập số km đã đi (nhập 0 để kết thúc chương trình): '))
    
    if km==0:
        print('Kết thúc chương trình')
    elif km < 0:
        print('Khoảng cách không hợp lệ. Vui lòng nhập lại ')
    else:
        if km <= 1:
            cuoc = 15000
        elif km <= 5:
            cuoc = 15000 + (km-1)*13500
        else:
            cuoc = 15000 + 4*13500 + (km-5)*11000
            
        if km > 120:
            cuoc *=0.9
        print(f'Tổng tiền cước taxi cho {km} km là : {cuoc}đ')
        break
            
       
        