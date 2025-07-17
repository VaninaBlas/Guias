Ejercicio 11. Determinar qué hace la siguiente función y ejecutarla a mano para algunas entradas.
Revisar luego los resultados en Python.

```python

def construir_tabla(n:int)->dict[int,int]:
    """
    Requiere:n>0
    Devuelve: un diccionario con las claves del 1 a n, donde sus valores son
    el numero al cruadrado
    """
    r:dict[int,int]=dict()
    i:int=1
    while i<=n:
        r[i]=i*i
        i=i+1
    return r
```
Ingreso 2: <br>
1<=2<br>
r={1:1}<br>
2<=2<br>
r={1:1, 2:4}<br>
i=3<br>
stop<br>
Ingreso 6:<br>
r={1:1, 2:4, 3:9, 4:16, 5:25, 6:36}<br>