"""
def primera_ocurrencia(elem:int,ls:list[int])->int:
    '''
    Requiere: ls contiene al menos una ocurrencia de elem
    Devuelve: el indice de la primera ocurrencia de elem en ls
    '''
    i:int=0
    while ls[i] != elem:
        i=i+1
    return i
a:list[int]=[1,2,4,1,5]
print(primera_ocurrencia(1,a))
print(primera_ocurrencia(5,a))
"""
# reescribirlo usando for en lugar de while
def primera_ocurrencia(elem:int,ls:list[int])->int:
    '''
    Requiere: ls contiene al menos una ocurrencia de elem
    Devuelve: el indice de la primera ocurrencia de elem en ls
    '''
    for i in range(0,len(ls)):
        if(ls[i] == elem):
            break
    return i
a:list[int]=[1,2,4,1,5]
print(primera_ocurrencia(1,a)) # output:0
print(primera_ocurrencia(5,a)) # output:4
# esta forma unque se trata de una forma perfectamente válida, 
# no es demasiado pythónica (mentira)

#Reescribirlo usando for (i,x) in enumerate(a). Buscar y leer la
# documentación de enumerate.

def primera_ocurrencia(elem:int,ls:list[int])->int:
    '''
    Requiere: ls contiene al menos una ocurrencia de elem
    Devuelve: el indice de la primera ocurrencia de elem en ls
    '''
    for (i,x) in enumerate(ls):
        if(x==elem):
            break
    return i

a:list[int]=[1,2,4,1,5]
print(primera_ocurrencia(1,a)) # output:0
print(primera_ocurrencia(5,a)) # output:4