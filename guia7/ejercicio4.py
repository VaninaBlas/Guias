#Se tienen N cofres cerrados con llave y M llaves. Se sabe que una y solo una de las
#M llaves sirve para abrir todos los cofres; las llaves restantes son inútiles (no abren ningún cofre).
#Escribir un algoritmo para determinar cuál es la llave útil. Calcular su complejidad algorítmica (en
#peor caso).


# cofre 1, cofre 2, cofre 3
# llave 1, llave 2, llave 3
# 1 llave abre todos los cofres
# llave 1 prueba con cofre1
# llave 2 prueba con cofre 1
# se abre
import random

def llaves_cofre(c:list[str],l:list[str]):
  llave_maestra:int= random.randint(0,len(l)-1) #o(1)
  vr:str=""
  i:int=0
  while(i<len(l)):
    if(i == llave_maestra):
      vr=l[i]
      i=len(l)
    i=i+1
  return vr


cofres:list[str]=["a","b","c","d"]
llaves:list[str]=["llave1","llave2","llave3","llave4","llave5","llave6","llave7"]
print("Encontro la llave, es:",llaves_cofre(cofres,llaves))

"""
linea 16-o(len(l)) / ??
linea 17- o(1)
linea 18-o(1)

linea 19-o(len(l))
if/ o(max(1,1,1))
linea 20-o(1)
linea 21-o(1)
linea 22-o(1)

linea 23-o(1)

linea 24-o(1)
"""