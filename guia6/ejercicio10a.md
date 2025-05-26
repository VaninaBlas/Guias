``` python
def iniciales(ls:list[str]) -> list[str]:
    """
    Requiere: Todos los strings de ls tienen longitud >0.
    Devuelve: Una lista de longitud len(ls) tal que la posición j, para todo j entre 0 y len(ls)-1, tiene el primer carácter del string ls[j]
    """
    r:list[str]=[]
    i:int=0
    while i<len(ls):
        primer_caracter:str=ls[i][0]
        r.append(primer_caracter)
        i=i+1
    return r
```
## Terminacion
- antes del ciclo, i empieza valiendo 0
- en cada vuelta, i incrementa en 1
- ls no es modificada dentro del cuerpo del ciclo, por lo que len(ls) es una constante
- Por lo tanto, i va a tomar valores 0,1,2.. y en algun momento alcanzara a len(ls)
- En ese momento, la condicion i<len(ls) sera falso y el ciclo terminara.

## Predicado invariante
Inv: Para todo j tal que 0 ≤ j < i, el elemento en la posición j de la lista r es igual al primer carácter del string que está en la posición j de la lista ls.
Ademas, la longitud de r es igual i

## Correctitud
- el ciclo termina cuando i==len(ls)
- Por lo tanto, podemos reemplazar i por len(ls) en el inv, quedando "Para todo j tal que 0 ≤ j < len(ls), el elemento en la posición j de la lista r es igual al primer carácter del string que está en la posición j de la lista ls.
Ademas, la longitud de r es igual len(ls)"
- Eso se puede trasncribir como "Para todos los elementos de ls, la lista r contiene en la misma posición el primer carácter del string correspondiente."
- Eso es exactamente lo que la especificacion nos pide