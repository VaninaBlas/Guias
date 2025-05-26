Sin ejecutarlo en Python, determinar qué imprime por pantalla el siguiente código.
¿En qué difiere la ejecución de las líneas 5 y 7?<br>
``` python
def despedir(ls:list[str]):
    ls.append("chau")
a:list[str]=["hola", "mundo"]
despedir(a) #linea 5
print(a)
despedir(list(a)) #linea 7
print(a)
```
Yo creo que imprime en la linea 6 ["hola", "mundo", "chau"] y en la linea 8 imprime lo mismo ✅

La diferencia entre la linea 5 y 7 esta en que, en la primera modifico la lista a y en la ultima modifico una copia de a que no modifica la lista original a. Por eso en el ultimo print me dio lo mismo 
