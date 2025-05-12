"""
(a) Dado un número entero n ≥ 0, imprimir por pantalla un cuadrado de asteriscos de lado n.
"""
def cuadrado_n_astericos(n:int)-> str:
    """
    Requiere:n >=0
    Devuelve: un cuadrado de asteriscos de lado n
    """
    i:int=0
    vr:str=""
    while(i<n):
        vr= vr + "*" * n + "\n"
        i=i+1
    return vr

n:int=int(input("Ingrese n: "))
print(cuadrado_n_astericos(n))

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
