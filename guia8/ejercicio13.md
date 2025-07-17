(a) Determinar a mano qué se imprime por pantalla en cada print al ejecutar el siguiente programa. Suponer definida la función construir_tabla del Ejercicio 11. Revisar luego los
resultados en Python


```python
def filtrar(tabla:dict[int,int], digito:int):
    """
    Requiere: digito>=0
    Devuelve:nada
    Modifica: la lista pasada como parametro es modificada
    permanentemente, quedando solo las claves donde su ultimo digito (de los valores) es igual a digito
    """
    claves_a_eliminar:list[int]=[]
    for k in tabla:
        valor:int=tabla[k]
        ultimo_digito:int=int(str(valor)[-1])
        if ultimo_digito != digito:
            claves_a_eliminar.append(k)
    for k in claves_a_eliminar:
        tabla.pop(k)

tabla:dict[int,int]= construir_tabla(10)
otra:dict[int,int]=tabla
print(otra)

filtrar(tabla, 9)
print(tabla)
print(otra)
```
primer print: ejecuta {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

segundo print: ejecuta {3: 9, 7: 49}, se eliminan las claves que no tienen en sus valores un 9 al final

tercer print: ejecuta {3: 9, 7: 49}, porque los dict son mutables