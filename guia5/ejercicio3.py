def eliminar_comentarios(filename_fuente:str, filename_destino:str):
    """
    Requiere:nada
    Devuelve: el archivo1 pero sin sus comentarios
    """
    f_fuente=open(filename_fuente, "r")
    f_destino=open(filename_destino, "w")
    for linea in f_fuente:
        linea=linea.rstrip()
        f_destino.write(por_linea(linea) + "\n")
    return f_destino

def por_linea (s:str):
    """
    Requiere:nada
    Devuelve: la linea con el contenido hasta #
    """
    i=0
    linea_limpia=""
    while(i<len(s)):
        if(s[i]=="#"):
            i=len(s)
        else:
            linea_limpia=linea_limpia+s[i]
        i=i+1
    return linea_limpia
eliminar_comentarios("fuente_by_amarillo.txt", "destino_by_cui.txt")