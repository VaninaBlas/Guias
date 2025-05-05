def enumerar(n:int)-> str:
    """
        Requiere:n>0
        Devuelve: los numeros de 1 a n, separados por comas: "1,2,...,n".
    """
    res:str = str(n)
    i:int= n-1
    while i>0:
        res=str(i) + "," + res
        i=i-1
    return res
# (BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB)
# Demostrar que el ciclo termina para cualquier entrada valida
"""
- Antes del ciclo, i empieza valiendo n-1
- En cada ejecucion del cuerpo del ciclo, i se decrementa en 1
- Por lo tanto, i va a tomar valores n-1, n-2,n-3.. y en algun momento va a llegar
a ser igual a 0
- En ese momento, i>0 es falso y el ciclo termina
"""
# Hacer un seguimiento de la ejecucion de enumerador(6)
"""
Luego de 0 iteraciones: res vale _____"6"_______; i vale __5__; i>0 (5>0) es ___True______.
Luego de 1 iteraciones: res vale _____"5,6"_______; i vale __4__; i>0 (4>0) es ___True______.
Luego de 2 iteraciones: res vale _____"4,5,6"_______; i vale __3__; i>0 (3>0) es ___True______.
Luego de 3 iteraciones: res vale _____"3,4,5,6"_______; i vale __2__; i>0 (2>0) es ___True______.
Luego de 4 iteraciones: res vale _____"2,3,4,5,6"_______; i vale __1__; i>0 (1>0) es ___True______.
Luego de 5 iteraciones: res vale _____"1,2,3,4,5,6"_______; i vale __0__; i>0 (0>0) es ___False______.
En ese momento, el ciclo termina y la linea 11 devuelve el valor actual de res(o sea, "1,2,3,4,5,6"),
y la ejecucion termina
"""
# Escribir un predicado invariante que describa el trabajo realizado por
# el ciclo para cualquier valor de n
"""
Inv: res vale los numeros de i+1 a n, separados por comas 
(Cuando i = 5, res = "6" → del 6 al 6 (i+1 a n)
Cuando i = 4, res = "5,6" → del 5 al 6 (i+1 a n))
"""
# Usar el predicado invariante para mostrar que la funcion cumple con la especificacion
"""
El ciclo termina cuando i==0
Entonces reemplazamos i por 0 en inv y sabemos que al terminar el ciclo,
"res vale los numeros de 0+1=1 a n, separados por comas"
Entonces, al terminar el ciclo, res vale los numeros de 1 a n, separados por comas.
Eso es exactamente lo que se espera que devuelva la funcion segun su especificacion.
"""