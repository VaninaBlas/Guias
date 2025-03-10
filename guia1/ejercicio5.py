#Ejercicio 5. En el ejercicio anterior apareció el carácter \. Se conoce a la barra invertida como
#carácter de escape, y su función dentro de una cadena de caracteres es darle un significado especial
#al carácter que figura inmediatamente a continuación. Por ejemplo, \n se usa como carácter de
#nueva línea. Escribir las siguientes instrucciones en la consola interactiva ipython:

print( " \"\n")
# al principio deja un espacio, el \ permite colocar una comilla " dentro de la cadena
# y el \n nos da un salto de linea
print(""" Cuidado con las " comillas ". """)
# el """ """ nos permite colocar comillas dentro de la cadena y que no nos genere un error
print( ' Tengamos " mucho cuidado " por favor . ')
# si decidimos usar " dentro de una cadena de ' es posible, tambien si se hace
# al reves

# Devuelve
# "
# 
# Cuidado con las " comillas ". 
# Tengamos " mucho cuidado " por favor . 
