def buscar(elem:int,lista:list[int])->tuple[bool,int]:
    """
    Requiere:nada
    Devuelve: (True,p) si elem  aparece en la lista por primera vez
    en la posicion p; o bien (False, None) si no aparece nunca. 
    """
    vr:tuple[bool,int]
    for p in range(0,len(lista)):
        if lista[p]==elem:
            vr=(True,p)
            break
        else:
            vr=(False,None)
    return vr

xs:list[int]=[3,4,5,5]
buscar(5,xs) # Devuelve (True, 2)