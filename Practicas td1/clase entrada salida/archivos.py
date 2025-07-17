def contar(letra:str, linea:str) -> int:
    i:int=0
    cantidad=0
    while(i<len(linea)):
        if(linea[i] == letra):
            cantidad=cantidad+1
        i=i+1
    return cantidad
def cinco_vocales_unicas(s:str) -> bool:
    """
    Requiere:nada
    Devuelve: true sii s tien por lo menos una vez cada vocal
    """
    return contar("a",s)==1 and contar("e",s)==1 and contar("i",s)==1 and contar("o", s)==1 and contar("u",s)==1
def contar_vocales(f):
    """
    Requiere:nada
    Devuelve: imprime por pantalla unicamente las palabras que contengan las 5 vocales (aeiou), separadas por espacios en blanco
    """
    for linea in f:
        linea=linea.rstrip()
        #print(linea)
        if(cinco_vocales_unicas(linea)):
            print(linea)
    
f=open("palabras.txt")  
contar_vocales(f)
    