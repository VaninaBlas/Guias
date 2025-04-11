def cant_a(s:str) -> int:
    """
    Requiere:nada
    Devuelve: la cantidad de ocurrencias de "a" en s
    """
    cant:int =0
    i:int =0
    while(i<len(s)):
        if(s[i]=="a"):
            cant=cant+1
        i=i+1
    return cant 
# Demostrar que el ciclo termina para cualquier entrada válida
#Terminacion
"""
- La variable i empieza valiendo 0
- En cada ejecucion del cuerpo del ciclo, i e incrementa en 1
- El string s no cambia nunca en el programa, entonces len(s) nunca va a cambiar
- por lo tanto, i va a tomar valores 0,1,2... y en algun momento va a llegar a len(s)
- en ese momento, i<len(s) es falso y el ciclo termina
"""
#Seguimiento
"""
Hacer un seguimiento completo de la ejecución de cant_a('alaska'):
Luego de 0 iteraciones: cant vale __0__; i vale __0__; i<len(s) es ____True_____.
Luego de 1 iteración: cant vale _1__; i vale __1__; i<len(s) es ____True_____.
Luego de 2 iteraciones: cant vale __1__; i vale __2__; i<len(s) es __True_______.
Luego de 3 iteraciones: cant vale ___2_; i vale __3__; i<len(s) es ___True______.
Luego de 4 iteraciones: cant vale ___2_; i vale __4__; i<len(s) es ____True_____.
Luego de 5 iteraciones: cant vale ___2_; i vale __5__; i<len(s) es ____True_____.
Luego de 6 iteraciones: cant vale __3__; i vale __6__; i<len(s) es ____True_____.
"""
#(c) Completar el siguiente predicado invariante, de manera que describa el trabajo realizado
#por el ciclo para cualquier valor de s:

"""
Inv: cant vale la cantidad de ocurrencias de "a" en los primeros i caracteres de s
"""
#(d) Entonces, ¿qué valor tendrá cant luego de len(s) iteraciones? Comparar con la cláusula
#Devuelve de la especificación de la función. (Deberían expresar lo mismo.)
"""
El ciclo termina cuando i==len(s)
Entonces, reemplazamos i por len(s) en inv y sabemos que al terminar el ciclo, "cant vale la cantidad de
ocurrencias de "a" en los primeros i caracteres de s" , 
Decir "la cantidad de ocurrencias de "a" los primeros i caracteres de s" equivale a decir "cant vale la cantidad
"a" en s"
Entonces: al terminar el ciclo, cant vale la cantidad de "a" en s, que es lo que debe devolver la funcion segun
su especificacion
De esta manera , al nosotros devolver cant en la ultima linea, estamos realizando lo que se pedia en la especificacion
"""