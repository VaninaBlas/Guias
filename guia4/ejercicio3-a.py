def enumerar(n:int)-> str:
    """
        Requiere:n>0
        Devuelve: los numeros de 1 a n, separados por comas: "1,2,...,n".
    """
    res:str="1"
    i:int=2
    while(i<=n):
        res =res +","+str(i)
        i=i+1
    return res
#(AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA)
# Demostrar que el ciclo termina para cualquier entrada valida
"""
- Antes del ciclo, i empieza valiendo 2
- En cada ejecucion del cuerpo del ciclo, i se incrementa en 1
- Por la clausula requiere sabemos que la variable entera n es mayor a 0 y,
ademas, no se modifica en el cuerpo del ciclo
- Por lo tanto, i va a tomar valores 2,3,.. y en algun momento va a llegar 
a ser mayor a n
- en ese momento, i <= n es falso  y el ciclo termina
"""
# Hacer un seguimiento de la ejecucion de enumerador(6)
"""
Luego de 0 iteraciones: res vale _____"1"_______; i vale __2__; i<=n (2<=6) es ___True______.
Luego de 1 iteraciones: res vale _____"1,2"_______; i vale __3__; i<=n (3<=6) es ___True______.
Luego de 2 iteraciones: res vale _____"1,2,3"_______; i vale __4__; i<=n (4<=6) es ___True______.
Luego de 3 iteraciones: res vale _____"1,2,3,4"_______; i vale __5__; i<=n (5<=6) es ___True______.
Luego de 4 iteraciones: res vale _____"1,2,3,4,5"_______; i vale __6__; i<=n (6<=6) es ___True______.
Luego de 5 iteraciones: res vale _____"1,2,3,4,5,6"_______; i vale __7__; i<=n (7<=6) es ___False______.
En ese momento, el ciclo termina y la linea 11 devuelve el valor actual de res(o sea, "1,2,3,4,5,6"),
y el ciclo termina
"""
# Escribir un predicado invariante que describa el trabajo realizado por
# el ciclo para cualquier valor de n
"""
Inv: res vale los numeros de 1 a i-1, separados por comas
"""
# Usar el predicado invariante para mostrar que la funcion cumple con la especificacion
"""
El ciclo termina cuando i==n+1
Entonces reemplazamos i por n+1 en inv y sabemos que al terminar el ciclo,
"res vale los numeros de 1 a n+1-1=n, separados por comas"
Entonces, al terminar el ciclo, res vale los numeros de 1 a n, separados por comas.
Eso es exactamente lo que se espera que devuelva la funcion segun su especificacion.
"""