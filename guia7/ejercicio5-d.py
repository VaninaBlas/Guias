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

"""
linea 11-o(1)
linea 12-o(1)
linea 13-o(len(ls))
linea 14-o(1)
linea 15-o(1)
linea 16-o(1)
"""