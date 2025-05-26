``` python
a:list[int]=[1,2]
b:list[int]=a
a.append(3)
print(len(b))
```
(a) ¿Qué valor se imprime en la última instrucción? ¿Por qué no se imprime 2, si luego de
ejecutar la línea 2, b tenía 2 elementos y luego no la modificamos? <br>

Yo creo que imprime 3, porque al modificar la lista a en la siguiente linea, la lista b en consecuencia tambien es modificada<br>

(b) ¿Qué se imprime si reemplazamos la línea 2 por b:list[int] = list(a)? <br>

Se imprime 2, porque la funcion list() no solo es para crear lista vacias, tambien sirve para hacer copias de otras listas y asi los cambios que se hagan en la lista original no afectan a esta.
<br>
(c) Comparar con el siguiente código, visto en el Ejercicio 6 de la Guía 1:

```python
a:int=1
b:int=a
a=2
print(b)
```
Esto nos devuelve b, esto es porque algo que tienen las listas es que son mutables donde apuntan a la misma lista guardada en la memoria, y con enteros b apunta al valor 1 no a a, sino al mismo valor, cuando se cambia el valor de a, hace que a apunte para otro valor (2) pero b sigue apuntando al 1, porque los enteros no se pueden modificar, solo reasignar