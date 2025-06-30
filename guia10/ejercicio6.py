"""
lista[2,4,3]- [3,4,2]
1- lista
xs''=[2,4] - [3]
            
xs'' =[2] - [4]

xs'' =[] -[2]
"""
def espejar(xs:list[int])->list[int]:
    """
    Requiere:nada
    Devuelve: una nueva lista que contiene los mismos elementos
    que xs, pero en el orden inverso
    """
#    i=len(xs)-1
#    l=[]
    if(len(xs)==0):
        return []
    else:
        #l=espejar(xs[:i])
        #l[xs[-1]]=l[xs[i]]
        #return l    

        return [xs[-1]] + espejar(xs[:-1])
espejar([1,2,2,5,9])

