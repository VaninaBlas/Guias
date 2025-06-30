#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#pot2(n): Dado un entero n ≥0, calcular 2^n. Ejemplos: pot2(0) →1; pot2(7) →128.
def post2(n:int):
    """
    Requiere: n>=0
    Devuelve:calculo de 2^n
    """
    if n==0:
        return 1
    else:
        return 2*post2(n-1)
print(post2(7))

#BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
#pot_a(a, n): Dados dos enteros n ≥0 y a, calcular an. Ejemplos: pot_a(3, 0) →1; pot_a(−2,
#7) →−128. Además, en particular pot_a(0, 0) debe devolver 1

def pot_a(a:int, n:int)->int:
    """
    Requiere:n>=0
    Devuelve:calculo de a^n
    """
    if n==0:
        return 1
    else:
        return a*pot_a(a,n-1)
pot_a(-2, 7) # Devuelve -128

#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
#producto(n, m): Dados dos enteros n ≥ 0,m ≥ 0, calcular n ∗m. Sugerencia: hacer la recursión 
#sobre el parámetro n, dejando fijo el valor de m

def producto(n:int, m:int)->int:
    """
    Requiere: n>=0, m>=0
    Devuelve: calcular n*m
    """
    if(n==0):
        return 0
    else:
        return m+producto(n-1,m)
    
producto(9,7) # Devuelve 63


#DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
#es_par(n): Determinar si un entero n ≥ 0 es par (o sea, debe devolver True si es par y
#False en caso contrario). Sugerencia: pensar cómo podría ayudar restarle 2 a n

def es_par(n:int)->bool:
    """
    Requiere: n>=0
    Devuelve: True si n es par, False si no
    """
    if(n==0):
        return True
    elif(n==1):
        return False
    else:
        return es_par(n-2)
    
    
es_par(6199)


    