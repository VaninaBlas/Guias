def cortar_texto(t:str, sep:str)-> str:
    """
    Requiere: len(sep)=1
    Devuelve: el texto que hay entre la ultima aparicion de sep y el ultimo
    elemento de t, si no hay sep en t devuelve el texto entero
    """
    i:int=1
    vr:str=""
    texto:str=""
    while(i<=len(t)):
        if(t[-i] == sep ):
            vr=vr +texto
            i=len(t)
        if not(sep in t):
            vr=t
            i=len(t)
        texto= t[-i] + texto
        i=i+1
    return vr


def texto_separado_en_sep(txt:str, sep:str) -> list[str]:
    """
    Requiere: len(sep)=1
    Devuelve: una nueva lista, donde separa txt en cada aparición de sep
    """
    i:int=0
    vr:list[str]=[]
    texto:str=""
    while(i<len(txt)):
        if(txt[i]==sep):
            vr.append(cortar_texto(texto, sep))
        texto=texto+txt[i]
        i=i+1
    return vr
texto_separado_en_sep('a;bb;c;;ddd;', ";") # Devuelve ['a', 'bb', 'c', '', 'ddd']

"""
linea 7-o(1)
linea 8-o(1)
linea 9-o(1)

linea 10-o(len(t))
if / o(max(len(t), 1,1))
linea 11-o(len(t)) ??
linea 12-o(1)
linea 13-o(1)
if / o(max(len(t),1,1))
linea 14-o(len(t)) /????
linea 15-o(1)
linea 16-o(1)

linea 17-o( ) /??????

linea 18-O(1)

linea 19-o(1)

------------------------------------------------------------------------

linea 27-O(1)
linea 28-o(1)
linea 29-o(1)

linea 30-o(len(txt))
if / o(max(len(txt), o()))
linea 31-o(len(txt)) 
linea 32-o() /?????
-
linea 33-o() /?????? / o(len(txt))
linea 34-o(1) 

linea 35-o(1)
"""