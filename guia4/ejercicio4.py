def raiz_entera(n:int) -> int:
    """
    Requiere: n>=0
    Devuelve: La parte entera de la raiz cuadrada de n.
    """
    i:int=0
    while i*i <=n:
        i=i+1
    return i-1
#(a) Demostrar que el ciclo termina para cualquier entrada válida
"""
- Antes del ciclo, i empieza valiendo 0
- En cada ejecucion del cuerpo del ciclo, i se incrementa en 1
- Por la clausula requiere, n es mayor o igual a cero, y no se modifica dentro del cuerpo del ciclo
- Por lo tanto, i va a tomar valores 0,1,2.. y en algun momento va a llegar a ser
mayor a n
- En ese momento, i*i <= n es falso y el ciclo termina
"""
#b) Hacer un seguimiento completo de la ejecución de raiz_entera(10)
"""
Luego de 0 iteraciones:  i vale __0__; i*i<=n (0<=10) es ___True______.
Luego de 1 iteraciones:  i vale __1__; i*i<=n (1<=10) es ___True______.
Luego de 2 iteraciones:  i vale __2__; i*i<=n (4<=10) es ___True______.
Luego de 3 iteraciones:  i vale __3__; i*i<=n (9<=10) es ___True______.
Luego de 4 iteraciones:  i vale __4__; i*i<=n (16<=10) es ___False______.
En ese momento el ciclo termina y la linea 9 devuelve el valor actual de i-1 (o sea 3),
y la ejecucion termina
"""
#(c) Escribir un predicado invariante que describa el trabajo realizado por el ciclo
"""
Inv: (i-1) es la parte entera de la raiz cuadrada de n
"""
#(d) Usar el predicado invariante para mostrar que la función cumple con la especificación.
"""
Condición de salida: El ciclo se sigue ejecutando mientras i * i ≤ n.
El ciclo termina cuando i * i > n, es decir, cuando el cuadrado de i ya supera a n.

Antes de salir del ciclo:
Cuando i * i > n (condición de salida), sabemos que i - 1 es el último número cuyo
cuadrado es menor o igual a n. Es decir:

El número i - 1 cumple que su cuadrado (i - 1)² ≤ n.

Y el número i ya no cumple, porque i * i > n.

Así que, cuando salimos del ciclo:

(i - 1)² ≤ n < i²

Esto es clave porque nos dice que el número que está justo antes de i (es decir,
i- 1) es el último número cuya raíz cuadrada no supera a n.

Conclusión:
El valor que se devuelve es i - 1.
Como sabemos que (i - 1)² ≤ n < i², el número i - 1 es el mayor número cuya 
raíz cuadrada no excede n, lo cual es exactamente lo que queremos en la 
especificación de la función: la parte entera de la raíz cuadrada de n.
"""