"""
Escribir una función que, dado un entero n>0 y un string filename, escriba un archivo
nuevo con nombre filename, que tenga los primeros n números primos, uno por línea.
"""
def archivo_n_numeros_primos(n:int, filename:str):
    """
    Requiere:n>0
    Devuelve: un archivo nuevo con nombre filename, que tenga los primeros n numeros primos, uno por linea.
    """
    i:int=2
    f=open(filename, "w")
    while(i<=n):
        if(esprimo(i)):
            f.write(str(i) + "\n")
        i=i+1
def esprimo(n:int)->bool:
    """
    Requiere:n>0
    Devuelve: si es primo o no
    """
    i:int=2
    raiz_n:int=int(n**(1/2))
    vr:bool=True
    while(i<=raiz_n):
        if(n % i ==0):
            vr=False
            i=raiz_n
        i=i+1
    return vr
archivo_n_numeros_primos(100, "michis.txt") 
