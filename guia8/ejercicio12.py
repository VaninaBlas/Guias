#Ejercicio 12. Escribir una función que encuentre el máximo valor entero de un diccionario de
##strings a enteros (es decir, dict[str,int]) y devuelva el conjunto de claves que tienen dicho va-
#lor. Por ejemplo, para el diccionario {'a':10, 'b':14, 'c':9, 'd':14, 'e':7} debe devolver
#{'b', 'd'} (porque tanto 'b' como 'd' tienen valor 14, que es el valor máximo del diccionario).

def maximo_valor_entero(dic:dict[str,int])->set[str]:
    """
    Requiere:
    Devuelve:el máximo valor entero de un diccionario de strings a enteros (es decir, dict[str,int]) 
    y devuelva el conjunto de claves que tienen dicho valor.
    """
    may=0
    vr:set[str]=set()
    for k,v in dic.items():
        if v>=may:
            may=v 
    for k in dic:
        if dic[k]==may:
            vr.add(k)
    return vr

maximo_valor_entero({'a':10, 'b':14, 'c':9, 'd':14, 'e':7})
            