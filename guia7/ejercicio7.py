"""
(a) El algoritmo BUBBLESORT consiste en recorrer la lista A de izquierda a derecha, dejando
ordenado en cada paso al par de elementos A[i] y A[i+1]. Esta pasada por toda la lista
debe repetirse len(A) veces. Implementar el algoritmo en Python. ¿Por qué funciona?
(b) Mostrar que BUBBLESORT tiene complejidad O(len(A)^2).
"""
def ordena_primer_numero(li:list[int])->list[int]:
  pos:int=0
  for i in range(1,len(li)):
    if(li[i]<li[pos]):
      (li[i],li[pos])=(li[pos],li[i])
    pos=pos+1
def bubblesort(A:list[int]):
    """
    Requiere: nada
    Devuelve: ordena(modifica) la lista de menor a mayor
    """
    for i in range(0,len(A)):
      ordena_primer_numero(A)
        
a=[11,23,7,2,10]
bubblesort(a)
print(a)
lista=[10,4,2,11,9]
#bubblesort(lista)
#print(lista)

"""
linea 8-o(1)

linea 9-o(len(li))
if / o(max())
linea 10-o(1)
linea 11-o(len(li))
-
linea 12-o(1)

----------------------------------------------------------------
linea 18- o(len(a))
linea 19- ??????
"""