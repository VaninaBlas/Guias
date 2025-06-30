#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#productoria(xs): Dada una lista no vacía de enteros xs, calcular el resultado de multiplicar
#todos los números de xs.

def productoria(xs:list[int])->int:
    """
    Requiere: len(xs)>0
    Devuelve: el resultado de multiplicar todos los numeros de xs
    """
    if(len(xs)==1):
        return xs[0]
    else:
        return xs[0]* productoria(xs[1:])
    
productoria([10,2,1,0]) # Devuelve 0

#BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
#cantidad_ocurrencias(x, xs): Dada una lista de enteros xs y un entero x, devolver la
#cantidad de veces que aparece x en xs

def cantidad_ocurrencias(x:int, xs:list[int])->int:
    """
    Requiere:nada
    Devuelve:la cantidad de veces que aparece x en xs
    """
    n=0
    if(len(xs)==0):
        return 0
    else:
        if(xs[0]==x):
            n+=1
            return n+cantidad_ocurrencias(x, xs[1:])
        else:
            return cantidad_ocurrencias(x, xs[1:])   
            
cantidad_ocurrencias(4, [4,4,0,1,9,1])        
        
#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
#max_pos(xs): Dada una lista no vacía de enteros xs, devolver la posición del elemento más
#grande. En caso de empate, devolver la posición de la primera aparición.
        

#DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
#contar_coincidencias(xs): Dada una lista de enteros xs, contar cuántas veces es cierto
#que la i-ésima posición tiene el número i (es decir, cuántas veces xs[i]==i)

def contar_coincidencias(xs:list[int])->int:
    """
    Requiere: nada
    Devuelve: cuantas veces es cierto que la i-eisma posicion tiene el numero i
    """
    i=len(xs)-1
    n=0
    if(len(xs)==0):
        return 0
    else:
        if(xs[i]==i):
            n+=1
            return n+contar_coincidencias(xs[:i])
        else:
            return contar_coincidencias(xs[:i])
    
        
contar_coincidencias([0,1,2,3,7]) # Devuelve 4
        
#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
#sumar_posiciones_pares(xs): Dada una lista de enteros, sumar los elementos en sus posiciones 
#pares. Ejemplo: sumar_posiciones_pares([1,2,9,4,3]) devuelve 13 = 1 + 9 + 3.

def sumar_posiciones_pares(xs:list[int])->int:
    """
    Requiere: nada
    Devuelve: sumatoria de los elementos en posiciones pares
    """  
    i=len(xs)-1
    n=0  
    if(len(xs)==0):
        return 0
    else:
        if(i%2==0):
            n+=xs[i]
            return n+sumar_posiciones_pares(xs[:i])
        else:
            return sumar_posiciones_pares(xs[:i])
                
sumar_posiciones_pares([1,2,9,4,3])  #Devuelve 13

      
        
        
        
        
        
        
        
        
        
        
        