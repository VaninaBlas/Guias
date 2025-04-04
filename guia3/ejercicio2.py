# Sean los siguientes programas, donde p y q son variables de tipo bool:
#Programa 1
def programa1(p:bool, q:bool) -> str:
    letra:str=""
    if p:
        if q:
            letra="A"
        else:
            letra="B"
    return letra

#Programa 2
def programa2(p:bool, q:bool) -> str:
    letra:str=""
    if p:
        if q:
            letra="A"
    else:
        letra="B"
    return letra 
#¿Qué diferencia hay entre los programas I y II? Para las 4 combinaciones
# de valores que pueden tener p y q, ¿qué imprime cada programa por pantalla? 
#La diferencia esta en donde se ubica el else. 
print("EJERCICIO A")
print("Programa 1:")
print("p y q True: ", programa1(True, True))
print("p False y q True: ", programa1(False, True))
print("p True y q False: ", programa1(True, False))
print("p y q False: ", programa1(False, False))
# El primero y ultimo estan vacios porque como p es False nunca se entra en la condicion
print("Programa 2:")
print("p y q True: ", programa2(True, True))
print("p False y q True: ", programa2(False, True))
print("p True y q False: ", programa2(True, False))
print("p y q False: ", programa2(False, False))
# El tercero esta vacio porque como p es true se entra en la condicion pero como
# q es False no se entra a la parte de asignacion y queda vacio 
print("-----------------------------------------------------------------")
#Completar los espacios en blanco, de modo que los programas III y IV se 
#comporten igual a los programas I y II, respectivamente, para todos los 
#posibles valores de p y q.
#Programa 3
def programa1b(p:bool,q:bool)-> str:
    letra:str=""
    if (p==True and q==True):
        letra="A"
    elif (q == False and p!=False):
        letra="B"
    return letra
#Programa 4
def programa2b(p:bool,q:bool)-> str:
    letra:str=""
    if (q==True and p==True):
        letra="A"
    elif (q==True or q==False and p!=True):
        letra="B"
    return letra
print("EJERCICIO B")
print("Programa 3:")
print("p y q True: ", programa1b(True, True))
print("p False y q True: ", programa1b(False, True))
print("p True y q False: ", programa1b(True, False))
print("p y q False: ", programa1b(False, False))
print("Programa 4:")
print("p y q True: ", programa2b(True, True))
print("p False y q True: ", programa2b(False, True))
print("p True y q False: ", programa2b(True, False))
print("p y q False: ", programa2b(False, False))