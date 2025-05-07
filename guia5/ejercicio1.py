# A
"""
(a) Escribir una función que tome como argumento el nombre de un archivo de texto y retorne
un string con las longitudes de las líneas del archivo (sin contar el carácter especial de fin
de línea), separadas por espacios. Por ejemplo, para un archivo con el siguiente contenido,
debería devolver el string '8 7 4 12 '.
"""
def longitudes_lineas_archivo(f) -> str:
    """
    Requiere:nada
    Devuelve:un string con las longitudes de las líneas del archivo (sin contar el carácter especial de fin
    de línea), separadas por espacios
    """
    vr:str=""
    for linea in f:
        linea=linea.rstrip()
        vr=vr + " " + str(len(linea))
    return vr
f=open("archivo_prueba.txt") 
print(longitudes_lineas_archivo(f))
f.close()
#B
"""
(b) Escribir una función similar a la anterior, que reciba como segundo argumento el nombre de
un archivo nuevo. Esta función, en lugar de devolver un string, debe escribir en el archivo
nuevo las longitudes de las líneas del archivo  original, una por línea.
"""
def longitudes_lineas_en_archivo2(archivo1,archivo2):
    """
    Requiere:nada
    Devuelve: un archivo2 con las longitudes de las líneas del archivo1    (sin contar el carácter especial de fin
    de línea), una por linea
    """
    for linea in archivo1:
        linea=linea.rstrip()
        archivo2.write(str(len(linea)) + "\n")
        
    
archivo1=open("archivo_prueba.txt")
archivo2=open("archivo_vacio.txt", "w")
longitudes_lineas_en_archivo2(archivo1, archivo2)