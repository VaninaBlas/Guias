def enumerar(n:int)->str:
    """
    Requiere:n>0
    Devuelve:los impares de 1 a n, separados por comas: "1,3,5,...,n".
    """
    res:str="1"
    i:int=3
    while i<=n:
        res=res+","+str(i)
        i=i+2
    return res
#(CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC)
# Demostrar que el ciclo termina para cualquier entrada valida
"""
-Antes del ciclo, i empieza valiendo 3.
- En cada ejecucion del cuerpo del ciclo, i se incrementa en 2.
- Por la clausula requiere sabemos que la variable entera n es mayor a 0 y, ademas,
no se modifica en el cuerpo del ciclo.
- Por lo tanto, i va a tomar valores 3,5,.. y en algun momento va a llegar a ser
mayor a n.
- En ese momento,i <=n es falso y el ciclo termina.
"""
# Hacer un seguimiento de la ejecucion de enumerador(6)
"""
Luego de 0 iteraciones: res vale _____"1"_______; i vale __3__; i<=n (3<=6) es ___True______.
Luego de 1 iteraciones: res vale _____"1,3"_______; i vale __5__; i<=n (5<=6) es ___True______.
Luego de 2 iteraciones: res vale _____"1,3,5"_______; i vale __7__; i<=n (7<=6) es ___False______.
En ese momento, el ciclo termina y la linea 11 devuelve el valor actual de res (o sea "1,3,5"),
y la ejecucion termina
"""
# Escribir un predicado invariante que describa el trabajo realizado por
# el ciclo para cualquier valor de n
"""
Inv: res vale los impares de 1 a i-2, separados por comas
(cuando i=3, res ="1" del 1 al 1 (n a i-2)
cuando i=5, res = "1,3" del 1 al 3 (n a i-2)
cuando i=7, res = "1,3,5" del 1 al 5 (n a i-2))
"""
# Usar el predicado invariante para mostrar que la funcion cumple con la especificacion
"""
- El ciclo termina cuando i>n
- Sabemos que la invariante es:
“res vale los impares de 1 hasta i - 2, separados por comas”.
- Como el ciclo termina cuando i > n, entonces justo antes de terminar valía i ≤ n.
Eso significa que el valor anterior, i - 2, es menor o igual a n (i - 2 ≤ n).
- Por lo tanto, al finalizar el ciclo, res contiene los impares desde 1 hasta i - 2, y ese i - 2 es el
último impar menor o igual a n.
- Como el ciclo avanza de a 2, y comienza en i = 3, solo recorre números impares, agregándolos
a res. Además, res comienza en "1", así que se incluyen todos los impares desde 1 hasta i - 2.
- Entonces, al finalizar, res contiene exactamente los impares desde 1 hasta n, separados por comas.
- Eso es exactamente lo que debe devolver la función, según su especificación.


En este caso no usamos algo tipo i ==n porque el ciclo no se rompe en un valor exacto de n
si no que varia de si esta (n) es par o impar.
"""