
print("EjercicioA:")
def cant_a(s:str) -> int:
    contador:int=s.count("a")
    return contador

ejemplo1:int=cant_a("aaa")
print(ejemplo1)
print("-----------------------------------------------------")
print("EjercicioB:")
def mayus_n ( s :str ) -> str :
    cadena:str=s.replace('n', 'N')
    return cadena
ejemplo2:str="libron"
ejemplo2Mayus= mayus_n(ejemplo2)
print(ejemplo2Mayus) 
print(ejemplo2)    
print("----------------------------------------------------------")
print("EjercicioC")
import math
def raiz_entera ( n : int) -> int:
    raiz:int= int(math.sqrt(n))
    return raiz

print(raiz_entera(4))
print(raiz_entera(16))
print(raiz_entera(26))
print(raiz_entera(48))