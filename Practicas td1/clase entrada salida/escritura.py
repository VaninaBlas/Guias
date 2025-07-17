def sumar_digitos(s:int) -> int:
 '''
 Requiere: nada.
 Devuelve: la suma de los dígitos de s.
 '''
 res:int = 0
 j:int = 0
 while j < len(str(s)):
     res = res + int(str(s)[j])
     j = j + 1
 return res

def comprobar(s:int)->bool:
    return sumar_digitos(s)==15

f = open("suman15.txt", "w")
i=0
cantidad=0
while(i<1000):
    if(comprobar(i)):
        f.write(str(i) + "\n")
    i=i+1
    
f.close()