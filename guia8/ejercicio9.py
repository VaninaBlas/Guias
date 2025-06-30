#Escribir una función que, dado un string s, 
# devuelva un diccionario con la cantidad
# de apariciones de cada carácter en s. Por ejemplo,
#  para 'agua' tiene que devolver el diccionario
#{'a': 2, 'g': 1, 'u': 1}.

def cantidad_apariciones_caracter(s:str)-> dict[str,int]:
    """
    Requiere:nada
    Devuelve: un diccionario con la cantidad de
    apariciones de cada caracter en s.
    """
    vr:dict[str,int]={}
    t_s:set[str]=set(s)
    abc:list[str]=["a","b","c","d","e","f","g"]  
    for i in (0,len(s)):
        
