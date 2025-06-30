#Se tienen N cofres y dentro de cada cofre hay un mazo de M naipes. Se sabe que
#en uno y solo uno de los cofres el mazo que contiene está ordenado (de menor a mayor). Escribir
#un algoritmo que determine cuál es el cofre que tiene el mazo ordenado. Calcular su complejidad
#algorítmica (en peor caso).


# cofre 1, cofre 2, cofre 3
# mazo de 4 naipes, mazo de 9 naipes, mazo de 10 naipes
#cofre x tiene el mazo ordenado
# cual es ese cofre

# abro cofre 1
# reviso naipes
# abro cofre 2
# reviso naipes
# lo tiene ordenado
# decir cual cofre

def verificar_lista_ordenada_creciente(l:list[int])->bool:
    '''
    Requiere:nada
    Devuelve: True si l esta ordenada en forma
      estrictamente creciente, False si no
    '''
    vr:bool=True
    for i in range(1,len(l)):
        if(l[i]<=l[i-1]):
            vr=False
            break
    return vr

def cofre_ordenado(cofres:list[list[int]])-> int:
  vr:int=0
  for i in range(0,len(cofres)):
    if(verificar_lista_ordenada_creciente(cofres[i])): #o(l)
      vr=i
      break #o(1)
  return vr+1

cofres:list[list[int]]=[[4,2,2,4],[9,6,7,8,9],[10,11,12,13,14,15]]
print("el cofre con naipes ordenados es el numero", str(cofre_ordenado(cofres)))
"""
linea 25- o(1)

linea 26- o(len(L))
Que hacer con el if, o(max(1,1,1)) 
linea 27-o(len(L)) / o(1)
linea 28- o(1)
linea 29-o(1)

linea 30-o(1)




linea 33- o(1)

linea 34- o(len(cofres))
if / o(max(len(l), 1, 1))
linea 35- o(len(l))
linea 36- o(1)
linea 37-o(1)

linea 38-o(1)
"""