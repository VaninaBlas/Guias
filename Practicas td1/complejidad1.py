# -*- coding: utf-8 -*-
"""
Created on Mon May 19 12:18:35 2025

@author: 46912870
"""

def buscar_v1(elem:int, lista:list[int])->bool:
    vr:bool=False
    for i in lista:
        if(i==elem):
            vr=True
    return vr

def buscar_v2(elem:int, lista:list[int])->bool:
    vr:bool=False
    for i in lista:
        if(i==elem):
            vr=True
            break
    return vr
