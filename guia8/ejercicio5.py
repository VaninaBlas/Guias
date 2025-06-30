#Dada una lista de strings (posiblemente con repetidos),
#  queremos averiguar cuántos strings únicos hay. Escribir 
# una función en Python que resuelva esto de manera sencilla 
# usando conjuntos. Por ejemplo, en 
# ['abc', 'd', 'ef', 'abc', 'ef', 'ef'] hay 3 strings únicos.

def cantidad_strings_unicos(li:list[str])->int:
    """
    Requiere:nada
    Devuelve:cuantos strings unicos hay
    """
    return len(set(li))

cantidad_strings_unicos(['abc', 'd', 'ef', 'abc', 'ef', 'ef']) # Devuelve 3