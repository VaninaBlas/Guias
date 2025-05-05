def mayus_n(s:str)->str:
    """
    Requiere:nada 
    Devuelve: una copia de s pero con todas las "n" en mayuscula
    """
    res:str=""
    j:int=0
    while(j<len(s)):
        if(s[j]=="n"):
            res = res + s[j].upper()
        else:
            res=res+s[j]
        j=j+1
    return res
#Demostrar que el ciclo termina para cualquier entrada válida
"""
- Antes del ciclo, la variable j empieza valiendo 0
- en cada ejecucion del cuerpo del ciclo, j se incrementa en 1
- El string s no se modifica en el cuerpo del ciclo, entonces len(s) nunca va a cambiar
- por lo tanto, i va a tomar valores 0,1,2,... y en algun momento va a llegar a len(s)
- en ese momento, i<len(s) es falso y el ciclo termina
"""
#Hacer un seguimiento completo de la ejecución de mayus_n('antena'):
"""
Luego de 0 iteraciones: res vale _____""_______; j vale __0__; j<len(s) es ___True______.
Luego de 1 iteración: res vale _______"a"_____; j vale __1__; j<len(s) es ___True______.
Luego de 2 iteraciones: res vale _____"aN"_______; j vale __2__; j<len(s) es __True_______.
Luego de 3 iteraciones: res vale _____"aNt"_______; j vale __3__; j<len(s) es ____True_____.
Luego de 4 iteraciones: res vale _____"aNte"_______; j vale __4__; j<len(s) es ____True_____.
Luego de 5 iteraciones: res vale _____"aNteN"_______; j vale __5__; j<len(s) es ____True_____.
Luego de 6 iteraciones: res vale _____"aNteNa"_______; j vale __6__; j<len(s) es ____False_____.
En ese momento, el ciclo termina y la linea 14 devuelve el valor actual de res(o sea, "aNteNa"),
y la ejecucion termina
"""
#Completar el siguiente predicado invariante, de manera que describa el trabajo realizado
#por el ciclo para cualquier valor de s:
"""
Inv: res vale la concatenacion de los primeros j caracteres de s pero con todas las "n" en mayuscula
""" 
#(d) Entonces, ¿qué valor tendrá res luego de len(s) iteraciones? Comparar con la cláusula
#Devuelve de la especificación de la función. (Deberían expresar lo mismo.)
"""
El ciclo termina cuando j==len(s)
Entonces reemplazamos j por len(s) en inv y sabemos que al terminar el ciclo, "res vale una copia
de los primeros len(s) caracteres de s pero con todas las "n" en mayuscula",
Decir "los primeros j caracteres de s " equivale a decir "todos los caracteres de s"
Entonces, al terminar el ciclo, res vale s pero con todas las "n" en mayuscula.
Eso es exactamente lo que se espera que devuelva la funcion segun su especificacion.
"""
