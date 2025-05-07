"""
Escribir una función que, dado un entero n>0 y un string filename, escriba un archivo
nuevo con nombre filename, que tenga los primeros n números primos, uno por línea.
"""
def archivo_n_numeros_primos(n:int, filename:str):
    """
    Requiere:n>0
    Devuelve: un archivo nuevo con nombre filename, que tenga los primeros n números primos, uno por línea.
    """
    i:int=0
    while(i<n):
        if( i % (i+1)!=0):
            f=open(filename, "x")
            f.write(str(i) + "/n")
        i=i+1

archivo_n_numeros_primos(20, "michis.txt") 
