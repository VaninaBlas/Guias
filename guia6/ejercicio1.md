Hacer un seguimiento a mano a mano, instrucción a instrucción, de la variable lista en el
siguiente programa, y determinar qué valor tiene al terminar

``` python
lista:list[str] = [ 'w' , 'l' , 'g' , 'x' , 'r' , 't' , 't' , 'm' , 'u']
lista.pop()
lista.append('x')
if 'w' in lista:
 lista[0] = 'a'
elif 'g' in lista:
 lista[0] = 'b'
else:
 lista[0] = 'c'
i:int=0
while i <len(lista):
  if lista[i]== 'x':
    lista[i] = 'o'
  i = i + 1
lista[5] = 'i'
```
1- con el pop(), [ 'w' , 'l' , 'g' , 'x' , 'r' , 't' , 't' , 'm'] <br>
2- con el append() [ 'w' , 'l' , 'g' , 'x' , 'r' , 't' , 't' , 'm' , 'x'] <br>
3- con el if, [ 'a' , 'l' , 'g' , 'x' , 'r' , 't' , 't' , 'm' , 'x'] <br>
4- como el if se cumple, el elif y el else se ignora, se mantiene [ 'a' , 'l' , 'g' , 'x' , 'r' , 't' , 't' , 'm' , 'x'] <br>
5- con el ciclo while, [ 'a' , 'l' , 'g' , 'o' , 'r' , 't' , 't' , 'm' , 'o'] <br>
6- en la linea final,  [ 'a' , 'l' , 'g' , 'o' , 'r' , 'i' , 't' , 'm' , 'o'] <br>
Segun lo que puedo ver lista termina valiendo [ 'a' , 'l' , 'g' , 'o' , 'r' , 'i' , 't' , 'm' , 'o'] <br>

El code se copilo y dio lo mismo 