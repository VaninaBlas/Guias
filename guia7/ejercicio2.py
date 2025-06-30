# Se tienen N cofres cerrados con llave y M llaves,
#  con M > N. Se sabe que una y solo una llave abre 
# cada cofre, y las restantes llaves son inútiles 
# (no abren ningún cofre). Escribir un algoritmo para
#  abrir todos los cofres. Calcular su complejidad 
# algorítmica (en peor caso)
import random

def llaves_cofre(c:list[str],l:list[str]):
  llave_maestra:int= random.randint(0,len(l)-1) #o(1)
  i:int=0
  while(i<len(l)):
    if(i == llave_maestra):
      print("se abren todos los cofres", c)
      i=len(l)
    i=i+1
cofres:list[str]=["a","b","c","d"]
llaves:list[str]=["llave1","llave2","llave3","llave4","llave5","llave6","llave7"]
llaves_cofre(cofres,llaves)
# cofre 1, cofre 2, cofre 3
# llave 1, llave 2, llave3, llave4,llave5
# probar llave 1 con cofre1
# probar llave 2 con cofre1
# probar llave 3 con cofre1
# se abre el cofre
# encontraste la llave
"""
linea 10- o(len(L)-1) / o(n) / o(1)
linea 11- o(1)
linea 12-o(L)
if / o(max(1,1,1))
linea 13-o(1)
linea 14-o(1)
linea 15-o(1)
linea 16-o(1)
"""