```python
def iniciales2(ls:list[str]):
    '''
    Requiere: Todos los strings de ls tienen longitud >0. Llamamos LS al valor inicial de ls.
    Devuelve: Nada.
    Modifica: En ls[j], para todo j entre 0 y len(ls) -1, queda el primer carácter del string LS[j].
    '''
    i:int=0
    while i<len(ls):
        primer_caracter:str=ls[i][0]
        ls[i]=primer_caracter
        i=i+1
```
## Terminacion
- Antes del ciclo, i empieza valiendo 0
- En cada vuelta de ciclo, i se incrementa en 1
- ls no es modificada dentro del cuerpo del ciclo, por lo tanto len(ls) es una constante
- Por lo tanto, i va a tomar valores 0,1,2.. y en algun momento alcanzara a len(ls)
- En ese momento, i<len(ls) sera falso y el ciclo terminara.

## Predicado invariante
Inv: las primeras i posiciones de ls tienen el primer caracter del valor original que habia en esa posicion
El resto de las posiciones(desde i en adelante) aun conserva su valor original

## Correctitud
- El ciclo termina cuando i==len(ls)
- Entonces podemos reemplazar i por len(ls) en la invariante, esto quedaria "las primeras len(ls) posiciones de ls tienen el primer caracter del valor original que habia en esa posicion
El resto de las posiciones(desde len(ls) en adelante) aun conserva su valor original"
- No existen posiciones despues de len(ls) en adelante (porque ls tiene longitud len(ls)), asi que toda la lista ls fue modificada. Y las "primeras len(ls) posiciones" es lo mismo que decir "todas las posiciones de ls"
- Por lo tanto, se cumple que "En ls[j], para todo j entre 0 y len(ls) - 1, queda el primer carácter del string original (LS[j])." y eso es lo que indica la especificacion.