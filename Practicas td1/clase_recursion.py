#   Dado n un entero mayor o igual a cero, definir una funci´on recursiva
#que devuelva la potencia de 3 a la n (3n) sin utilizar el operador **

def potencia_n(n:int)->int:
    """
    Requiere:n<=0
    Devuelve:la potencia de 3 a la n
    """
    if(n==0):
        return 1
    else:
        return 3*(potencia_n(n-1))
potencia_n(2)


#Dado n un entero mayor o igual a cero, definir una funci´on recursiva
#que devuelva el resto obtenido en la divisi´on de n por 3, sin usar la
#operaci´on de m´odulo ( %) .

def resto(n:int)->int:
    '''
    Requiere: n>=0.
    Devuelve: el resto de dividir a n por 3.
    '''
    if(n==0):
        return 0
    else:
        if(n==1):
            return 1
        elif(n==2):
            return 2
        else:
            return resto(n-3)
print(resto(23))


def es_capicua(arr: list[int]) -> bool:
    '''
    Requiere: nada.
    Devuelve: True si arr es capicúa (se lee igual de atrás para adelante que de adelante para atrás), False en caso contrario.
    '''

    if(len(arr)<=1):
        return True
    else:
        return arr[0]==arr[-1] and es_capicua(arr[1:-1])

es_capicua([8 ,4 ,8]) 
print(es_capicua([31 ,21 ,11 ,11 ,21 ,31])) 
es_capicua([]) 
print(es_capicua([9 ,8 ,7 ,6 ,8 ,9]) )

def contar_letras(arr: list[str], l: str) -> int:
    '''
    Requiere: nada.
    Devuelve: la cantidad de elementos de arr que contienen a l.
    '''
    if(len(arr)==0):
        return 0
    else:
        if(l in arr[0] ):           
            return 1+ contar_letras(arr[1:], l)
        else:
            return contar_letras(arr[1:], l)

print(contar_letras ([ 'casa '],'a')) #1
print(contar_letras ([ 'casa '],'b'))  #0
print(contar_letras ([ 'mo ','rit ','go ','al '], 'o')) #2
print(contar_letras ([ 'mo ','rit ','go ','al '], 'i') )#1

"""
elif len(arr)==1:
    if l in arr[0]:
        return 1
    else:
        return 0
else:
    if l in arr[-1]:
        return 1+contar_letras(arr[:-1])
    else:
        return contar_letras(arr[:-1])
    
"""

    
# 7-3-3 , 1
# 9-3-3-3, 0
# 10-3-3-3, 1