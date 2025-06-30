#Dado un número natural n, construir una lista con
#  los primeros n números naturales impares, 
# ordenados de menor a mayo
def primero_n_naturales(n:int)->list[int]:
    """
    Requiere: n>0
    Devuelve: una lista formada con los primeros n números 
    naturales impares, ordenados de menor a mayor
    """
    i:int=0
    vr:list[int]=[]
    while(i<n*2):
        if(i%2!=0):
            vr.append(i)
        i=i+1
    return vr
primero_n_naturales(3) # Devuelve [1,3,5]

"""
linea 10-o(1)
linea 11-o(1)

linea 12-o(n^2)
if / o(max(1,1))
linea 13-o(1)
linea 14-o(1)

linea 15-o(1)

linea 16-o(1)
"""