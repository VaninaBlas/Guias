#Un pangrama es un texto que usa todas las letras posibles 
# del alfabeto de un idioma.Se pide escribir una función en 
# Python que determine si un texto en español es un pangrama. 
# Por simplicidad, suponer que el texto de entrada está 
# compuesto solamente por letras en minúscula, sin tildes ni 
# diéresis, pero sí puede tener eñes. Por ejemplo, 
# es_pangrama('extraño pan de col y kiwi se quemo bajo fugaz
#  vaho') debe devolver True.

def es_pangrama(s:str)->bool:
    abc:set[str]={"a","b","c","d","e","f","g","h","i","j","k","l",
                "m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"}
    vr:bool=False
    if(abc==(set(s)-{" "})):
        vr=True
    return vr
es_pangrama('extraño pan de col y kiwi se quemo bajo fugaz vaho') # Devuelve True