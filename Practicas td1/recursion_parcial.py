# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 12:57:25 2025

@author: 46912870
"""

def pares_desc(xs:list[int])->int:
    """
    Requiere:nada
    Devuelve:la cantidad de elementos de xs tales que xs[i]>=xs[i+1] con 0<=i<len(xs)-1
    """
    if len(xs)<2:
        return 0
    else:
        if xs[0]>=xs[1]:
            return 1+pares_desc(xs[1:])
        else:
            return pares_desc(xs[1:])
    
pares_desc([5,4,3,6,7,1,9,10,5]) #devuelve 4

def multiplicar_pos_impares(xs:list[int])->int:
    """
    Requiere:nada
    Devuelve:el producto entre los elementos que se encuentran en las posiciones impares de xs
    """
    i=len(xs)-1 
    if len(xs)<2:
        return 1
    else:
        if(i%2!=0):
            return xs[i]*multiplicar_pos_impares(xs[:i])
        else:
            return multiplicar_pos_impares(xs[:i])
        
multiplicar_pos_impares([4,3,2,5])

def espejar(xs):
    if len(xs)==0:
        return []
    else:
        return [xs[-1]] + espejar(xs[:-1])


def max_pos(xs:list[int])->int:
    if(len(xs)==1):
        return 0
    else:
        pos=max_pos(xs[:-1])
        if xs[pos]>=xs[-1]:
            return pos
        else:
            return len(xs)- 1
        
max_pos([1,3,2,0,3])

def contar_coincidencias(xs:list[int])->int:
    """
    Requiere: nada
    Devuelve: cuantas veces es cierto que la i-eisma posicion tiene el numero i
    """
    i=len(xs)-1

    if(len(xs)==0):
        return 0
    else:
        if(xs[i]==i):

            return 1+contar_coincidencias(xs[:i])
        else:
            return contar_coincidencias(xs[:i])
        
contar_coincidencias([1,1,2,3,7]) # Devuelve 4