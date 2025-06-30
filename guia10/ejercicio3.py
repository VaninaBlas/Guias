#Escribir una función recursiva fibonacci(n) que dado un entero n ≥0, devuelva el término
#Fnde la sucesión de Fibonacci.
def fibonacci(n:int)->int:
    """
    Requiere:n>=0
    Devuelve: el termino fn de la sucesion de Fibonacci
    """
 
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

#fibonacci(50) se queda colgado

"""
fibonacci(6)
-n=6
n=5 + n=4
n=4 + n=2
n=3 + n=0

"""