#Se tiene un mazo de M naipes. Escribir un algoritmo que determine si el mazo está
#ordenado (de menor a mayor) o no. Calcular su complejidad algorítmica (en peor caso).
def mazo_esta_ordenado_ascendente(mazo:list[int])-> bool:
    """
    Requiere:nada
    Devuelve: True si el mazo está ordenado (de menor a mayor) o False si no
    """
    i:int=1
    vr:bool=True
    while(i<len(mazo) and len(mazo)!=0 and vr==True):
        if(mazo[i]<=mazo[i-1]):
            vr=False
        i=i+1
    return vr

"""
linea 8- o(1)
linea 9- o(1)
linea 10- o(n), o(1),o(1),o(1)
linea 11- o(1)
linea 12- o(1)
linea 13-o(1)
linea 14-o(1)

o(1)+o(1)+o(n)*(o(1)+o(1)+o(1)+o(1)+o(1)+o(1)) + o(1)
o(1)+o(1)+o(n)*(o(max(1,1,1,1,1,1))) + o(1)
o(1)+o(1)+o(n)*o(1)+o(1)
o(1)+o(1)+o(n)+o(1)
o(max(1,1,n,1))
o(n)
"""
