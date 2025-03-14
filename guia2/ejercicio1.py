'''
def f( x : int ) :
    x = x + 1
x:int = 10
f(x)
print(x)
f( x * x )
print(x)

'''
#La funcion recibe un numero y a ese mismo numero le suma uno y lo reasigna
# el numero que se pasa como parametro es 10, en el primer print deberia 
# imprimirse 11, en la linea 7 se pasa como parametro ese x siendo multiplicado
# por si mismo que daria como resultado 100, luego se muestra otro print para x
# que en la funcion se transforma en 101 

def f( x : int ) :
    x = x + 1
x:int = 10
f(x)
print(x)
f(x*x)
print(x)
print("----------------------------------------------------------------")
#output: 
#10
#10 
# Buenooo, varias cosas, primero la funcion no tiene un return que nos devuelva
# la x sobreescrita, asi que por defecto esa funcion devuelve un none,
# otra cosa es que en todo caso ni siquiera se esta guardando lo que la funcion
# nos deberia devolver en una nueva variable o la misma, y ademas de todo,
# cuando llamamos a esa funcion no nos modifica de ningun modo la varible original
# si no que es totalmente independiente, un ejemplo
 
def f( x : int ) -> int:
    x = x + 1
    return x
x:int = 10
x11:int= f(x)
print(x11)
x101:int=f(x*x)
print(x101)
x11_2da:int= f(x)
print(x11_2da)

# Como podemos ver el valor original de x no cambia no importa cuantas veces
# usemos la funcion, y en este caso la funcion si devuelve algo
print("---------------------------------------------------------------")
'''
def f( x:int ) -> int :
 x = x + 1
 return x
x:int = 10
x = f(x)
print(x)
print(x * x)
'''
# En este caso la funcion si nos esta devolviendo algo y ese resultado se 
# esta asignando a una variable que en este caso es el x original
# entonces, eso hace que cambie el valor de nuestra x original y se vuelva
# lo que la funcion devuelve que en este caso es 11
# imprimimos el valor de x que anteriormente fue modificada, en la siguiente
# linea (56) se imprime el resultado de la multiplicacion de x por si mismo
# que seria 11 * 11, como resultado 121

def f( x:int ) -> int :
 x = x + 1
 return x
x:int = 10
x = f(x)
print(x)
print(x * x)
# output:
# 11
# 121
# Ahora si me salio bien la prediccion
print("-----------------------------------------------------------------")
'''
def f ( x : int ) -> int :
 x = x + 1
 return x
def g ( y : int ) -> int :
 x :int = f(y)
 return f(x) # Python nos permite usar el return para guardar el resultado sin necesidad de ponerla en una variable
x : int = 10
x = g( x )
print( x )
x = g( x * x )
print( x )

'''
#Aca tenemos dos funciones una que es la que teniamos antes y otra nueva
# que es medio confusa, lo que esta haciendo se llama funcion anidada
# que es cuando llamamos a una funcion dentro de otra, en este caso, 
# llamamos a la funcion f y le pasamos el parametro de la funcion g y se lo asignamos
# a una nueva variable llamada x, esta variable es completamente diferente 
# de la que tenemos originalmente, las variables creadas dentro de una 
# funcion existen solo dentro de esa funcion, osea, no podemos llamarlas cuando
# salgamos de la funcion

# Entonces, para finalizar la funcion g, nos termina devolviendo f(x) que 
# esta llamando nuevamente a la funcion f

# Para empezar a probar, tenemos una variable x con valor 10, esta es reasignada
# con el resultado que nos da la funcion de g con parametro x
# un print para ver el resultado que yo digo que devuelve 12

# En la siguiente linea (88), se vuelve a reasignar el valor de x con lo que
# devuelva la funcion de g con el parametro de x*x , que seria 12*12, nos
# devolveria 146

def f ( x : int ) -> int :
 x = x + 1
 return x
def g ( y : int ) -> int :
 x :int = f(y)
 return f(x)
x : int = 10
x = g( x )
print( x )
x = g( x * x )
print( x )

# output:
#12
#146
# Todo ok
print("--------------------------------------------------------------")
'''
def f ( x :int , y : int ) -> int :
 x = 2 * x + y
 return x
x:int= 3
y:int= 7
y = f (y , x ) # ¡Cuidado!, el parametro x en f es y, el parametro x en f es y
x = f (y , x )
print (x , y )
print (x , x * x )
'''
#Esta vez la funcion f recibe dos parametros(x,y), reasigna a x el valor de
# la operacion 2 * x +y, y nos devuelve ese resultado
# Se declaran dos variables llamadas x e y , luego se les reasigna el valor
# a cada uno con el resultado que da al llamar a la funcion f con los parametros
# x e y (en x y ya no es 7 si no que el valor reasignado), en la linea 137 se imprime x e y separados y al final se imprime
# x y x multiplicado a si mismo
# yo digo que en el primer print se muestra  37 17 y en el segundo 37 1369
def f ( x :int , y : int ) -> int :
 x = 2 * x + y
 return x
x:int= 3
y:int= 7
y = f(y , x ) # ¡Cuidado!, el parametro x en f es y, el parametro x en f es y
x = f(y , x )
print (x , y )
print (x , x * x )
#output:
#37 17
#37 1369
# Todo ok