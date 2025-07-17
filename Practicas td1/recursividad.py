# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 12:04:35 2025

@author: 46912870
"""

def jeringoso(s:str)->str:
    if(len(s)==0):
        return ""
    else:
        if(s[0] in "aeiou"):
            return s[0]+"p"+ s[0]+ jeringoso(s[1:])
        else:
            return s[0]+jeringoso(s[1:])
jeringoso("loco")

def max_pos(xs:list[int])->int:
    if(len(xs)==1):
        return 0
    else:
        N=len(xs)-1
        if xs[N]>xs[:N][max_pos(xs[:N])]:
            return N
        else:
            return max_pos(xs[:N])
    

max_pos([1,9,3,40,40])

def dict_longitudes(xs:list[str])->dict[str,int]:
    if(len(xs)==0):
        return {}
    else:
        d=dict_longitudes(xs[1:])
        d[xs[0]]=len(xs[0])
        return d

dict_longitudes(["arbol", "casa", "auto"])