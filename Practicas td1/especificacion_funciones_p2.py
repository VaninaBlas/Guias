def espar( x: int ) -> bool :
 '''
 Requiere: nada
 Devuelve: False si el numero es impar y true si es par
 Completar
 '''
 return x % 2 == 0

num:int=2
#print(espar(num))

def espar2( x: int ) -> bool :
    '''
    Requiere:nada
    Devuelve:  si es par o no
    '''
    a: int = x // 2
    b: float = x / 2
    return abs (a - b) < 0.01

num=3
#print(espar2(num))
def rotar(s: str , s2:str) -> str:
    '''
    Requiere: ambos textos del mismo tamaño
    Devuelve: true si al rotar s2 es igual que s y False si no
    '''
    sr= s[len(s)-1] in s2[0]
    kk= s[0] in s2[len(s)-1]
    papa= s[-1] 
    rt= sr * kk 
    return bool(rt)
print(rotar("abc", "cba"))

#a in (b+b)