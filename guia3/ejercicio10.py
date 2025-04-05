#(a) En la función controlar_m, demostrar que las líneas 8 y 9 podrían eliminarse y obtener el
#mismo resultado en todos los casos

def controlar_m(m1:int,m2:int)->bool:
    """
    Requiere : nada.
    Devuelve: True si los valores de m1 y m2 son seguros; False si no.
    """
    ok:bool=False
    if m1<70:
        ok=True
    if m1<70 and m2<990: #linea 8
        ok = True # linea 9
    return ok

def controlar_m2(m1:int,m2:int)->bool:
    """
    Requiere : nada.
    Devuelve: True si los valores de m1 y m2 son seguros; False si no.
    """
    ok:bool=False
    if m1<70 or (m2<990 and m1<70):
        ok=True
    return ok

#(b) Mostrar que las líneas 6 y 7 de la función controlar_x podrían reemplazarse por una única
#condición más simple:
def controlar_x(x1:int,x2:int)->bool:
    """
    Requiere : nada .
    Devuelve: True si los valores de x1 y x2 son seguros; False si no
    """
    ok:bool=False
    if x1>100 or x2<50:
        if not(x1<=100 or x2>=50): 
            ok=True
    return ok

def controlar_x2(x1:int,x2:int)->bool:
    """
    Requiere : nada .
    Devuelve: True si los valores de x1 y x2 son seguros; False si no
    """
    ok:bool=False
    if (x1 <= 100 and x2 >= 50): 
            ok=True
    return ok