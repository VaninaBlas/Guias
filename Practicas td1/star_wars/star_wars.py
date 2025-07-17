 # Descomentar la siguiente línea si tenés Python versión 3.8.x o inferior (borrando el #).
# from __future__ import annotations

def nave_estelar_cercana(sensado: list[int], p: int) -> bool:
    """
    Requiere: p>=0
    Devuelve:  si existe alguna nave estelar a una proximidad menor o igual al
punto crıtico
    """
    # EJ 1: COMPLETAR
    i:int=0
    vr:bool=False
    while (i<len(sensado)):
        if(sensado[i]<=p):
            vr=True
            i=len(sensado)
        i=i+1
    return vr

print(nave_estelar_cercana([32638, 205, 258, 71115], 250)) # True
def naves_cercanas(sensado: list[int], p: int) -> list[int]:
    '''
    Requiere: p>=0
    Devuelve: una lista con los elementos de sensado que estan a una
    proximidad menor o igual al punto crıtico
    '''
    # EJ 2: COMPLETAR
    i:int=0
    vr:list[int]=[]
    while (i<len(sensado)):
        if(sensado[i]<=p):
            vr.append(sensado[i])
        i=i+1
    return vr
# Inv : vr es una lista que contiene los elementos de sensado de la posicion 0 hasta
# i -1 menor o iguales a p

#Inv: vr contiene los primeros i elementos de sensado que son menores o iguales que p
print(naves_cercanas([32638, 205, 258, 71115, 198, 205], 250)) # [205,198,205]
    