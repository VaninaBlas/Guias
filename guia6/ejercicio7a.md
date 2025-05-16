Considerar el siguiente programa:

``` python
def buscar_v1(elem:int,ls:list[int])->bool:
    """
    Requiere:nada
    Devuelve:True sii elem aparece al menos una vez en ls.
    """
    r:bool=False
    i:int=0
    while i<len(ls):
        r=r or (ls[i]== elem)
        i=i+1
    return r

def buscar_v2(elem:int,ls:list[int])->bool:
    """
    Requiere:nada
    Devuelve:True sii elem aparece al menos una vez en ls.
    """
    r:bool=False
    i:int=0
    while i<len(ls) and not r:
        r=ls[i] == elem
        i=i+1
    return r
a:list[int] = [1,2,4,1,5]
print(buscar_v1(1,a), buscar_v2(1,a))
print(buscar_v1(3,a), buscar_v2(3,a))
print(buscar_v1(5,a), buscar_v2(5,a))
```
(a) Hacer un seguimiento a mano de la ejecución de los tres print, y observar cuándo
termina la ejecución del ciclo en cada caso
<br>
***Primer print:***
<br>
buscar(1,a) <br>
iteracion 0: i=0, r=False, i<len(ls) (0<5) es True <br>
iteracion 1: i=1, r=True, i<len(ls) (1<5) es True <br>
iteracion 2: i=2, r=True, i<len(ls) (2<5) es True<br>
iteracion 3: i=3, r=True, i<len(ls) (3<5) es True<br>
iteracion 4: i=4, r=True, i<len(ls) (4<5) es True<br>
iteracion 0: i=5, r=True, i<len(ls) (5<5) es False<br>

En ese momento el ciclo termina y la ultima linea retorna el valor actual de r (osea True) 
<br>

buscar_v2(1,a)<br>
iteracion 0: i=0, r=False, i<len(ls) (0<5) y not r (True and True) es True <br>
iteracion 1: i=1, r=True, i<len(ls) (1<5) y not r (True and False) es False <br>

En ese momento el ciclo termina y la ultima linea retorna el valor actual de r (osea True) <br>

***segundo print:***<br>
buscar_v1 (3, a) <br>
iteracion 0: i=0, r=False, i<len(ls) (0<5) es True<br>
iteracion 1: i=1, r=False, i<len(ls) (1<5) es True<br>
iteracion 2: i=2, r=False, i<len(ls) (2<5) es True<br>
iteracion 3: i=3, r=False, i<len(ls) (3<5) es True<br>
iteracion 4: i=4, r=False, i<len(ls) (4<5) es True<br>
iteracion 0: i=5, r=False, i<len(ls) (5<5) es False<br>

En ese momento el ciclo termina y la ultima linea retorna el valor actual de r (osea False) 
<br>
buscar_v2 (3, a) <br>
iteracion 0: i=0, r=False, i<len(ls) (0<5) y not r (True and True) es True<br>
iteracion 1: i=1, r=False, i<len(ls) (1<5) y not r(True and True) es True<br>
iteracion 2: i=2, r=False, i<len(ls) (2<5) y not r(True and True) es True<br>
iteracion 3: i=3, r=False, i<len(ls) (3<5) y not r(True and True) es True<br>
iteracion 4: i=4, r=False, i<len(ls) (4<5) y not r(True and True) es True<br>
iteracion 0: i=5, r=False, i<len(ls) (5<5) y not r(False and True) es False<br>

En ese momento el ciclo termina y la ultima linea retorna el valor actual de r (osea False) <br>

***tercer print:*** <br>
buscar_v1 (5, a) <br>
iteracion 0: i=0, r=False, i<len(ls) (0<5) es True<br>
iteracion 1: i=1, r=False, i<len(ls) (1<5) es True<br>
iteracion 2: i=2, r=False, i<len(ls) (2<5) es True<br>
iteracion 3: i=3, r=False, i<len(ls) (3<5) es True<br>
iteracion 4: i=4, r=False, i<len(ls) (4<5) es True<br>
iteracion 0: i=5, r=True, i<len(ls) (5<5) es False<br>

En ese momento el ciclo termina y la ultima linea retorna el valor actual de r (osea True) <br>

buscar_v2 (5, a) <br>
iteracion 0: i=0, r=False, i<len(ls) (0<5) y not r (True and True) es True<br>
iteracion 1: i=1, r=False, i<len(ls) (1<5) y not r(True and True) es True<br>
iteracion 2: i=2, r=False, i<len(ls) (2<5) y not r(True and True) es True<br>
iteracion 3: i=3, r=False, i<len(ls) (3<5) y not r(True and True) es True<br>
iteracion 4: i=4, r=False, i<len(ls) (4<5) y not r(True and True) es True<br>
iteracion 0: i=5, r=True, i<len(ls) (5<5) y not r(False and False) es False<br>

En ese momento el ciclo termina y la ultima linea retorna el valor actual de r (osea False) <br>