#Reescribir la función del Ejercicio 3(c), de 
# modo que la ejecución del ciclo corte en cuanto
#  se sepa que la lista no está ordenada. Escribir
#  dos versiones: una con while y otra con for
"""
def verificar_lista_ordenada_creciente(l:list[int])->bool:
    '''
    Requiere:nada
    Devuelve: True si l esta ordenada en forma
      estrictamente creciente, False si no
    '''
    i:int=1
    vr:bool=True
    while(i<len(l) and len(l)!=0):
        if(l[i]<=l[i-1]):
            vr=False
        i=i+1
    return vr
verificar_lista_ordenada_creciente([1,2,13,24,5]) # Devuelve False
"""
#con while
def verificar_lista_ordenada_creciente(l:list[int])->bool:
    '''
    Requiere:nada
    Devuelve: True si l esta ordenada en forma
      estrictamente creciente, False si no
    '''
    i:int=1
    vr:bool=True
    # se agrega el vr==True para que corte cuando no se cumple la condicion dentro del ciclo
    while(i<len(l) and len(l)!=0 and vr==True):
        if(l[i]<=l[i-1]):
            vr=False
        i=i+1
    return vr

#con for 
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