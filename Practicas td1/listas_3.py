# Descomentar la siguiente línea si tenés Python versión 3.8.x o inferior (borrando el #).
# from __future__ import annotations


    #################
    ## EJERCICIO 1 ##
    #################

def suma_en_posiciones_impares(xs:list[int], n:int)->list[int]:
    '''
    Requiere: nada
    Devuelve:  una nueva lista con los
    mismos elementos que xs pero sumandoles n a aquellos en las posiciones
    impares de xs
    '''
    #COMPLETAR!
    i:int=0
    vr:list[int]=[]
    while(i<len(xs)):
        if(i%2!=0):
            vr.append(xs[i]+n)
        else:
            vr.append(xs[i])
        i=i+1
    return vr
            
#print(suma_en_posiciones_impares([6, 4, 7, 5], 10))
"""
inv: la lista res contiene,
"""
def suma_en_posiciones_impares_v2(xs:list[int], n:int):
    '''
    Requiere: nada
    Devuelve: no devuelve nada
    Modifica: xs queda alterada permanentemente,de modo que 
    en sus posiciones impares, los valores estan incrementandos en n
    '''
    #COMPLETAR!
    i:int=0
    while(i<len(xs)):
        if(i%2!=0):
            xs[i]=xs[i]+n
        print(xs[i])
        i=i+1
    return xs
mi_lista:list[int]=[6, 4, 7, 5]
#inv: las primeras i posiciones de xs conservan sus valores originales en las posiciones pares,  
#y tienen el valor original incrementando en n en las posiciones impares


#print(suma_en_posiciones_impares_v2(mi_lista, 10))
#print(mi_lista)
#print(suma_en_posiciones_impares_v2(mi_lista, 10))
#print(mi_lista)
    #################
    ## EJERCICIO 2 ##
    #################


#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

#primer print
# [30 ,20 ,12 ,38]  [30 ,20 ,12 ,38] [30 ,20 ,12 ,38]

#segundo print
# 100

# tercer print
# [] [] [30 ,20 ,12 ,38]


#PUNTO B) MODIFICAR AMBAS FUNCIONES

#(1)

def totalapagar(gastos:list[int]) -> int:
    total:int = 0
    for i in gastos:
        total=total+i
    gastos.clear()
    return total
print(totalapagar([5,2,1]))
#(2)

def totalapagar_con_descuento(gastos:list[int]) -> float:
    total:float = 0.0
    contar:int=0
    i=0
    while(i<len(gastos)):
        if(gastos[i] !=0 and contar==0):
            total=total+gastos[i]/2
            contar=contar+1
        else:
            total=total+gastos[i]
        i=i+1
    gastos.clear()
    return total
print(totalapagar_con_descuento([5,2,1,5,1]))

