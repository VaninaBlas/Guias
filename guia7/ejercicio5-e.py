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
"""
linea 9-o(1)
linea 10-o(1)

linea 11-o(len(ls))
linea 12-o(1) / o(len(ls))
linea 13-o(1)

linea 14-o(1)
"""