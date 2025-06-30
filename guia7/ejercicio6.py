"""
Considerar esta variante del algoritmo SELECTIONSORT visto en clase:
Para cada i entre len(A) y 1 (inclusive):
    Buscar el mayor elemento en A[:i].
    Intercambiarlo con A[i-1].
(a) Pensar un predicado invariante que describa el comportamiento del ciclo principal.
(b) Implementar el algoritmo en Python.
(c) Mostrar que tiene complejidad O(len(A)^2)
"""
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
"""
Inv: A[i:] esta ordenada (para 1≤i≤len(A))
"""
#BBBBBBBBBBBBBBBBBBBBBBBBBBBB
def pos_mayor(L:list[int])->int:
    """
    Devuelve: la posicion del numero mayor de L
    """
    pos:int=0
    for j in range(1,len(L)):
        if L[j] >L[pos]:
            pos=j
    return pos  

def sort_inverso(A:list[int]):
    """
    Devuelve: ordena(modifica) la lista de menor a mayor
    """
    for i in range(len(A),0,-1): #o(n)
        sublista:list[int]=A[:i] #o(n)
        pm:int=pos_mayor(sublista)
        (A[i-1], A[pm])=(A[pm], A[i-1])

"""
linea 19-o(1)

linea 20-o(len(l))
if / o(max(1,1))
linea 21-o(1) ??
linea 22-o(1)

linea 23-o(1)

------------------------------------------------------------------

??????????????????
linea 29-o(len(a))
linea 30-o(i)
linea 31-o(i)
linea 32-o(1)
"""