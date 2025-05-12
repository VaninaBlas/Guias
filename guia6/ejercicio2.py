"""
Escribir el encabezado y el docstring de cada una de las siguientes funciones, 
describiendo qué hace y especificando lo que requiere y lo que devuelve.

(a)
def ____________ (n:int) -> _______________ :
    '''
    COMPLETAR
    '''
    r:list[str]=[]
    while n>0:
        r.append(str(n))
        n=n-1
    r.append("¡Despegue!")
    return r
"""
#A
def cuenta_regresiva(n:int) -> list[str] :
    """
    Requiere: n>0
    Devuelve: una lista de n a 1 y al final un ¡Despegue!
    """
    r:list[str]=[]
    while n>0:
        r.append(str(n))
        n=n-1
    r.append("¡Despegue!")
    return r

"""
(b)
def _______________ (a:______) -> _____________:
    '''
    COMPLETAR
    '''
    r:int=0
    i:int=0
    while i< len(a):
        r= r+round(a[i])
        i=i+1
    return r
"""
#B
def suma_numeros_redondeados_lista (a:list[float]) -> int:
    """
    Requiere: len(a)>0
    Devuelve: la suma de todos los numeros redondeados de la lista a
    """
    r:int=0
    i:int=0
    while i<len(a):
        r= r+round(a[i])
        i=i+1
    return r

"""
(c)
def _______________ (a:_______)->__________:
    '''
    COMPLETAR
    '''
    r:list[int]=[]
    i:int=len(a)-1
    while i>=0:
        r.append(a[i])
        i=i-1
    return r
"""
#C
def lista_ordenada_descendente (a:list[int])->list[int]:
    """
    Requiere: len(a)>0
    Devuelve: una lista con la lista a ordenada de manera descendente
    """
    r:list[int]=[]
    i:int=len(a)-1
    while i>=0:
        r.append(a[i])
        i=i-1
    return r
