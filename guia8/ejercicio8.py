def indice_jaccard(a:set[int], b=set[int])->float:
    """
    Requiere: len(a) y len(b) > 0
    Devuelve: el indice Jaccard entre a y b
    """
    return len(a&b)/len(a|b)

indice_jaccard({1,2,3},{3,4}) #Devuelve 0.25

def k_shingles(s:str, k:int)->set[str]:
    stop=False
    n:int=0
    vr:set[str]=set()
    while(not stop):
        vr.add(s[n:k])
        if(k == len(s)):
            stop=True
        n,k= n+1, k+1
    return vr
k_shingles('hola mundo', 5) # Devuelve {' mund', 'a mun', 'hola ', 'la mu', 'mundo', 'ola m'}

def indice_jaccard_k_shingles(a:str, b:str)->float:
    """
    Requiere: len(a),len(b) > 0
    Devuelve: la similitud Jaccard entre los k_shingles de
    a y b 
    """
    k_a=k_shingles(a,3)
    k_b=k_shingles(b,3)
    return len(k_a&k_b)/len(k_a|k_b)
indice_jaccard_k_shingles('hola mundo', 'mundo hola') # Devuelve 0.4545