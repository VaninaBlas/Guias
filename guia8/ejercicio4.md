Para cada una de las siguientes expresiones, determinar cuál es su tipo y evaluarla a mano a mano,
realizando las conversiones de tipos que sean necesarias. Suponer que xs es una lista de
enteros con valor [1, 4, 2, 1, 5].

<br>
***xs=[1,4,2,1,5]***
<br>

| expresiones | tipo/output | 
|----------|----------|
| {}    | diccionario, devuelve {}   | 
| {'a','b','a'}   | set, devuelve  {'a','b'}  |
| set()    | set, devuelve  set()  | 
| set(xs)    | set, devuelve {1,4,2,5} sin un orden especifico  | 
| list(set(xs))    | list, devuelve [1,4,2,5] de nuevo sin un orden especifico   | 
| len(xs)-len(set(xs))    | int, devuelve 5-4=1   | 
| 5 in set(xs)    | bool, devuelve True  | 
| set(xs) & {1,10}    | set, {1}   | 
| set(xs) I {1,10}    | set, {1,4,2,5,10} sin un orden especifico  | 
| set(xs) - {1,10}    |  set, {4,2,5}  sin un orden especifico| 