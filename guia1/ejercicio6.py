#Ejercicio 6. ¿Qué valor se imprime en la última instrucción del 
# siguiente programa?
a :int = 1
b :int = a
a = 2
print ( b )
# Devuelve 1
# ¿Por qué no se imprime 2, si en la segunda instrucción indicamos 
# que b valiera lo mismo que a?
# el programa funciona en orden de ariba a abajo, b se quedo con el valor
# que a tenia en ese momento y no se volvio a actualizar