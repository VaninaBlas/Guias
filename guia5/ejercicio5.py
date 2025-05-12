"""
Escribir un único programa que realice las dos operaciones del Ejercicio 4. Primero
debe preguntar el nombre de la operación a realizar ('cuadrado' o 'inversa') y después, los
argumentos que correspondan para la operación correspondiente.
"""
from ejercicio4 import cuadrado_n_astericos, inversa_texto
print("¿Qué operacion quiere realizar?")
operacion:int=int((input("1-Cuadrado \n2-Inversa\nIngrese número:")))
n:int=0
texto:str=""

if(operacion==1):
    n=int(input("Ingrese n: "))
    print(cuadrado_n_astericos(n))
else:
    texto=input("Ingrese un texto: ")
    print(inversa_texto(texto))