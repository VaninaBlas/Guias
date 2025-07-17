#Ejercicio 10. Escribir una función que deletree palabras. Por ejemplo, dado 'aljibe' debe de-
#volver 'a, ele, jota, i, be, e.' Usar un diccionario para representar las reglas.

def deletrear(s:str)->str:
    """
    Requiere:nada
    Devuelve:la palabra deletradea
    """
    pron:dict[str,str]={"a":"a", "b":"be", "c":"ce", "d":"de","e":"e",
                        "f":"efe", "g":"ge", "h":"ache", "i":"i", "j":"jota", "k":"ka", 
                        "l":"ele","m":"eme", "n":"ene","ñ":"eñe", "o":"o", "p":"pe","q":"cu",
                        "r":"ere", "s":"ese", "t":"te", "u":"u", "v":"ve", "w":"doblev", "x":"equis",
                        "y":"igriega", "z":"zet"}
    print(len(pron))
    vr:str=""
    for i in s:
        vr+=pron[i]+", "
    return vr[:-2]+ "."
deletrear("aljibe")
        