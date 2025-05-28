#Dados dos strings, devolver la cantidad de veces que el primero está contenido en el segundo
def dentro(c1:str, c2:str)->int:
    """
        Requiere: nada
        Devuelve: la cantidad de veces que c1 está contenido en c2
    """
    vr:int=0
    i:int=0
    while(i<len(c2)):
      if(c1 == c2[i]):
        vr=vr+1
      i=i+1
    return vr
dentro("a","casa")

"""
linea 7- o(1)
linea 8- o(1)
linea 9- o(len(c2))
linea 10- o(len(c2)) /??????
linea 11-o(1)
linea 12- o(1)
linea 13- o(1)
"""