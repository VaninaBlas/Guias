"""
Escribir un programa que elija al azar dos números enteros entre 10 y 20, permita al
usuario ingresar el resultado del producto entre ambos números, y muestre un mensaje indicando
si el resultado es correcto o incorrecto. 
"""
import random
numero1:int = random.randint(10,20)
numero2:int = random.randint(10,20)
entrada:int=0
entrada=int(input("Ingresar el resultado de "+str(numero1)+"*"+str(numero2)+": "))
resultado:int=numero1*numero2
if(entrada==(resultado)):
    print("Bien!")
else:
    print("Mal! Resultado correcto: "+ str(resultado))