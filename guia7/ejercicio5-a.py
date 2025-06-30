#Dado un string, devolver su inversa 
"""
(b) Dado un string s, imprimir por pantalla la inversa de s. 
"""
def inversa_texto(texto:str)->str:
    """
    Requiere: nada
    Devuelve:imprime por pantalla la inversa de s
    """
    i:int=1
    vr:str=""
    while(i<=len(texto)):
        vr=vr+ texto[-i]
        i=i+1
    return vr

texto:str=input("Ingrese un texto: ")
print(inversa_texto(texto))

"""
linea 10- o(1)
linea 11-o(1)

linea 12-o(len(texto))
linea 13- o(1) /????
linea 14- o(1)

linea 15- o(1)
"""