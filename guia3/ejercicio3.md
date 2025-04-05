## Ejercicio 3. 
Para cada una de las siguientes expresiones, determinar su tipo y evaluarla (primero a mano, luego en la consola ipython):

(a) True and (1 / 0 == 0) <br>
(b) True or (1 / 0 == 0)<br>
(c) False and (1 / 0 == 0)<br>
(d) False or (1 / 0 == 0)<br>
(e) (1 / 0 == 0) and True<br>
(f) (1 / 0 == 0) or True<br>
(g) (1 / 0 == 0) and False<br>
(h) (1 / 0 == 0) or False<br>

¿Todos dan error porque no se puede dividir por cero?

**NO**, solo dan error cuando en la condicion se empieza por la division y dependiendo de si es or o and, esto es algo que hace python con los or y and de que si ve que la primer condicion se cumple (or) o incumple (and), no "mira" la segunda y sigue corriendo. 

Esto pasa en los puntos b,c. Donde apesar de ser incorrecto dividir por cero, ignora la segunda condicion y se queda solo con lo que dio la primera.