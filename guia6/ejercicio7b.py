"""
Reescribir las funciones buscar_v1 y buscar_v2 usando for en
lugar de while. En una de ellas, para terminar la ejecución
del ciclo en el mismo momento, será necesario usar break
o return en el cuerpo del ciclo

def buscar_v1(elem:int,ls:list[int])->bool:
    '''
    Requiere:nada
    Devuelve:True sii elem aparece al menos una vez en ls.
    '''
    r:bool=False
    i:int=0
    while i<len(ls):
        r=r or (ls[i]== elem)
        i=i+1
    return r

def buscar_v2(elem:int,ls:list[int])->bool:
    '''
    Requiere:nada
    Devuelve:True sii elem aparece al menos una vez en ls.
    '''
    r:bool=False
    i:int=0
    while i<len(ls) and not r:
        r=ls[i] == elem
        i=i+1
    return r
"""
def buscar_v1(elem:int,ls:list[int])->bool:
    """
    Requiere:nada
    Devuelve:True sii elem aparece al menos una vez en ls.
    """
    r:bool=False
    for num in ls:
      r=r or (num== elem)
    return r

def buscar_v2(elem:int,ls:list[int])->bool:
    """
    Requiere:nada
    Devuelve:True sii elem aparece al menos una vez en ls.
    """
    r:bool=False
    for num in ls:
        r=num == elem
        if(r):
          break
    return r