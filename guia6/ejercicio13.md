Determinar qué imprime por pantalla el siguiente código
``` python
def suma_problematica(ls:list[int])->int:
    n:int=0
    i:int=0
    while i<len(ls):
        n=n+ls[i]
        i=i+1
    ls.clear() # clear() elimina todos los elementos de la lista, linea 7
    return n
a:list[int]=[1,2,3,4]
print(suma_problematica(a))
print(suma_problematica(a))
```
Yo creo que imprime en el primer print 10 y en el segundo 0. <br>
¿Qué cambia si reemplazamos la línea 7 por ls = []? Es importante entender la diferencia entre
esas dos instrucciones. <br>

Eso imprime en ambos print 10.
Cuando hacés ls = [] dentro de la función, sólo cambiás la variable local ls para que apunte a una nueva lista vacía.
La variable a en el programa principal sigue apuntando a la lista [1, 2, 3, 4].
