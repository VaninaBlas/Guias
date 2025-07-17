# -*- coding: utf-8 -*-
"""
Created on Wed May  7 12:13:24 2025

@author: 46912870
"""

cuadrados=[]
i=1
while(i<=100):
    cuadrados.append(i**2)
    i=i+1
print(cuadrados)

i=0
while(i<len(cuadrados)):
    if (cuadrados[i]%2==1):
        print(cuadrados[i])
    i=i+1
   
    