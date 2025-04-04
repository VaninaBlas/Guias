#Sea la función f definida de la siguiente manera:
def f(s : str) -> str :
    if len(s)>0 and s[0]=='A':
        return 'Eureka'
    else:
       return 'Me aburro'

#(a) ¿Qué devuelven estas invocaciones? (Pensar Pensar las respuestas.)
#Yo creo que la primera devuelve Eureka, el segundo me abburro, el tercero
#  me aburro
print(f("Algoritmos"))
print(f("zzz"))
print(f(""))
# Todo ok

#(b) Repetir el punto anterior, pero considerando esta definición de f:
def f(s:str) -> str:
    if s[0]=='A' and len(s)>0:
        return 'Eureka'
    else:
        return 'Me aburro'
# Yo creo que todo devuelve lo mismo
print(f("Algoritmos"))
print(f("zzz"))
print(f(""))
# Ok, en el ultimo me da error, al parecer, segun deepseek y tambien es medio intuitivo
# en la anterior funcion cuando hicimos f("") en el condicional se evaluo primero len>0
# y lo siguiente lo ignoro pero si no lo hubiese ignorado tambien me hubiese
#dado error, como en el segundo primero evaluo eso (s[0]) y no lo ignoro
# da error porque no existe el indice 0 ya que esta vacio
