"""
Especificar, programar y verificar funciones para resolver los siguientes problemas. En
los ciclos usar while; no usar iteradores (for) todavía. Para la verificación, se pide hacer testing de
unidad, demostrar que los ciclos terminan, escribir predicados invariantes y usarlos para mostrar
que el código hace lo pedido.
"""
#AAAAAAAAAAAAAAAAAAAAAAAAAAAA
#Dada una lista no vacía de float, encontrar su máximo elemento. 
# Por ejemplo, para la lista [1.0, 12.7, 1.0, 8.8, 12.7, 3.0],
#  debería devolverse 12.7. No usar max
def maximo_elemento(l:list[float])-> float:
    """
    Requiere: len(l)>0
    Devuelve: el numero mayor en la lista l
    """
    i:int=0
    vr:float=0.0
    while(i<len(l)):
        if(l[i]>vr):
            vr= l[i]
        i=i+1
    return vr
maximo_elemento([1.0, 12.7, 1.0, 8.8, 12.7, 3.0]) # Devuelve 12.7

#Terminacion
"""
-i empieza valiendo 0
-i incrementa en 1 en cada vuelta del ciclo
-Por la clausula requiere len(l) es mayor a 0, y dentro del cuerpo
del ciclo l no cambia
-Por lo tanto, i va a tomar valores 0,1,2.. y en algun momento
va a llegar a len(l)
-En ese momento, i<len(l) sera falso y el ciclo terminara
"""
#Inv
"""
Inv: vr vale el numero mayor en los primeros i elementos de la lista l
"""

#BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
#Dada una lista de strings, construir un 
# string que sea la concatenación de todos sus elementos. Por ejemplo, 
# para la lista ['ab','c','','def'], se debe devolver 'abcdef'

def concatenar_strings_lista(l:list[str])->str:
    """
    Requiere: len(l)>0
    Devuelve:un string que sea la concatenacion de todos los elementos de l
    """
    i:int=0
    vr:str=""
    while(i<len(l)):
        vr=vr + l[i]
        i=i+1
    return vr
concatenar_strings_lista(['ab','c','','def']) # Devuelve 'abcdef'

#Inv
"""
Inv: vr vale un string que es la concatenacion de los primeros i elementos de l
"""

#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
#Dada una lista de enteros, determinar si está ordenada en forma 
# estrictamente creciente. Por ejemplo, [1,4,6] y [] están ordenadas,
# pero [6,4,1] y [4,6,6] no lo están. Notar que una lista vacía se considera ordenada

def verificar_lista_ordenada_creciente(l:list[int])->bool:
    """
    Requiere:nada
    Devuelve: True si l esta ordenada en forma estrictamente creciente, False si no
    """
    i:int=1
    vr:bool=True
    while(i<len(l) and len(l)!=0):
        if(l[i]<=l[i-1]):
            vr=False
        i=i+1
    return vr
verificar_lista_ordenada_creciente([1,2,13,24,5]) # Devuelve False
#Inv
"""
Inv: vr vale true si los primeros i-1 elementos de l esta ordenada
en forma estrictamente creciente, False si no
"""

#DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
#Dado un número natural n, construir una lista con los primeros n números 
# naturales impares, ordenados de menor a mayor. Por ejemplo, para 
# n=3, la lista esperada es [1,3,5].
def primero_n_naturales(n:int)->list[int]:
    """
    Requiere: n>0
    Devuelve: una lista formada con los primeros n números 
    naturales impares, ordenados de menor a mayor
    """
    i:int=0
    vr:list[int]=[]
    while(i<n*2):
        if(i%2!=0):
            vr.append(i)
        i=i+1
    return vr
primero_n_naturales(3) # Devuelve [1,3,5]

#Inv
"""
Inv: vr es una lista formada por los primeros i numeros naturales impares
"""

#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
#Dada una lista de enteros ls y un entero n, construir una nueva lista, 
# resultante de sumarle n a cada elemento de ls. Por ejemplo, para 
# ls=[1,9,7,7] y n=10, se debe devolver la lista [11,19,17,17]

def elementos_lista_n_sumado(ls:list[int], n:int) -> list[int]:
    """
    Requiere:len(ls)>0
    Devuelve: una lista resultante de sumarle n a cada elemento de ls
    """
    i:int=0
    vr:list[int]=[]
    while(i<len(ls)):
        vr.append(ls[i]+n)
        i=i+1
    return vr
elementos_lista_n_sumado([1,9,7,7],10) # Devuelve [11, 19, 17, 17]
#Inv
"""
Inv: vr es una lista resultante de sumarle n a los primeros i elementos de ls
"""

#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
#Dada una lista de strings, contar la cantidad total de caracteres. 
# Por ejemplo, para ['tor','c','ua','to'] el resultado esperado es 8
def contar_caracteres(ls:list[str])->int:
    """"
    Requiere: nada 
    Devuelve: la cantidad total de carecteres de ls
    """
    i:int=0
    vr:int=0
    while(i<len(ls)):
        vr=vr+len(ls[i])
        i=i+1
    return vr
#Inv
"""
Inv: vr vale la cantidad total de los primeros i caracteres de ls
"""

#GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
#Dada una lista de strings, contar la cantidad de veces que aparece la
#  letra 'a'. Por ejemplo, para ['abba','acdc','bee gees','a-ha'] 
# el resultado esperado es 5
def contar_a_en_texto(t:str)->int:
    """
    Requiere: nada
    Devuelve: la cantidad de a en t
    """
    i:int=0
    vr:int=0
    while(i<len(t)):
        if("a" in t[i]):
            vr=vr+1
        i=i+1
    return vr

#Inv
"""
Inv: vr vale la suma de coincidencias con a en los primeros i caracteres de t
"""

def contador_a_en_lista(ls:list[str])-> int:
    """
    Requiere: nada
    Devuelve: la cantidad de a en ls
    """
    i:int=0
    vr:int=0
    while(i<len(ls)):
        vr=vr+contar_a_en_texto(ls[i])
        i=i+1
    return vr
contador_a_en_lista(['absba','acdc','bee gees','a-ha']) # Devuelve 5

#Inv
"""
Inv: vr vale la suma de coincidencias con a en los primeros i caracteres de ls
"""

#HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
#Dado un string txt de longitud arbitraria y un string sep de longitud 1,
#  separar txt en cada aparición de sep, construyendo así una nueva lista.
#  Por ejemplo, para txt='a;bb;c;;ddd;' y sep=';', la lista resultante es
#  ['a','bb','c','','ddd','']. No usar split

def cortar_texto(t:str, sep:str)-> str:
    i:int=1
    vr:str=""
    texto:str=""
    while(i<len(t)):
        if(t[-i] == sep):
            vr=texto
            i=len(t)
        texto= t[-i] + texto 
        i=i+1
    return vr


def texto_separado_en_sep(txt:str, sep:str) -> list[str]:
    """
    Requiere:
    Devuelve:
    """
    i:int=0
    vr:list[str]=[]
    while(i<len(txt)):
        if(txt[i]==sep):
            vr.append(cortar_texto(txt[i], sep))

