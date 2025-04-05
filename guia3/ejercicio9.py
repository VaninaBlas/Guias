#Escribir una única expresión booleana en el lugar indicado en la siguiente función, de manera de
#cumplir con su especificación

def bisiesto(a:int)->bool:
    """
    Requiere : a >=0
    Devuelve : True si a es un año bisiesto ; False si no.
    """
    b:bool = True if (a%4==0 and a%100!=0) or a%400==0 else False
    return b

print(bisiesto(2020)) #True
print(bisiesto(2021)) #False
print(bisiesto(1900)) #False
print(bisiesto(2000)) #True

#Todo ok