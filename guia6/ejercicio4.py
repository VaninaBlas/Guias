"""
En una lista no vacía de números enteros, llamamos mesetas a las sublistas
 de números iguales que aparecen en forma consecutiva. Por ejemplo, la lista 
 [1,1,2,6,6,6,3,3] contiene
las mesetas [1,1], [2], [6,6,6] y [3,3]. Especificar, programar y verificar 
funciones para resolver los siguientes problemas, dada una lista de enteros:

(a) Determinar el número de la meseta más larga. Para la lista del ejemplo, 
la función debe devolver 6. Si hay más de una meseta de longitud máxima, 
devolver el número de la primera.
"""
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# estos codigos son horribles
def mesetas(ls:list[int], s:int)-> list[str]:
  i:int=0
  vr:list[str]=[]
  while(i<len(ls)):
    if(ls[i]==s):
      vr.append(ls[i])
    else:
      i=len(ls)
    i=i+1
  return vr
#print(mesetas([1,1,2,6,1,6,6,3,3], 1))
def numero_meseta_mas_larga(ls:list[int])-> int:
  """
  Requiere: len(l)>0
  Devuelve: el número de la meseta más larga, si hay más de una meseta 
  de longitud máxima, devolver el número de la primera, llamamos mesetas 
  a las sublistas de números iguales que aparecen en forma consecutiva
  """
  i:int=0
  vr:int=0
  longitud:int=0
  meseta:list[int]=[]
  while(i<len(ls)): 
    meseta=mesetas(ls[i:], ls[i])
    if(len(meseta)>longitud):
      longitud=len(meseta)
      vr=ls[i]
    elif(len(meseta)==longitud):
      if(vr>ls[i]):
        vr=ls[i]
    i=i+1
  return vr
numero_meseta_mas_larga([2,2,2,2,1,1,4,3,3,3,3,5,5,5,5,2,2,2,5,3,3,9,3,1,1,9,1,4,3,3,3,3])
    
"""
Construir una lista de listas, conteniendo las mesetas de la 
lista original, en el mismo orden. Para la lista del ejemplo, 
la lista resultante es [[1,1],[2],[6,6,6],[3,3]]
""" 
#BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
def lista_de_listas(ls:list[int])-> list[list[int]]:
  i:int=0
  vr:list[list[int]]=[]
  variable:int=ls
  meseta:list[int]=[]
  while(i<len(ls)):
    meseta=mesetas(variable, ls[i])
    variable= variable[len(meseta):]
    i=i+1
    if(meseta!=[]): #ignorando el verdadero problema
      vr.append(meseta)
  return vr
mi_lista=[1,1,1,1,1,2,2,21,12,3,1,1,1,6,1,6,6,3,3]
print(lista_de_listas(mi_lista))

"""
Construir una lista de enteros, conteniendo la longitud de cada 
meseta de la lista original, en el mismo orden. Para la lista del
ejemplo, se debe devolver [2,1,3,2]
"""
#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
def longitud_sublistas(ls:list[list[int]])-> list[int]:
  i:int=0
  vr:list[int]=[]
  while(i<len(ls)):
    vr.append(len(ls[i]))
    i=i+1
  return vr
  
mi_lista2=[1,1,1,3,3,3,4,4,5,3,3,3,6,6]
print(longitud_sublistas(lista_de_listas(mi_lista2)))
