#Ejercicio 8. Para este ejercicio, adaptar los programas de búsqueda vistos en clase.
#(a) Escribir un programa que, dados una lista de enteros A y un entero x, retorne todos los
#elementos de A menores o iguales que x. Estimar su complejidad algorítmica (en peor caso).
#(b) Igual al punto anterior, pero sabiendo que la lista está ordenada

# [2,3,4,5,1,6,1]
# 5
# retorna [2,3,4,5,1,1]
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
def menores_igual_a(li:list[int], a:int)->list[int]:
  vr:list[int]=[]
  for i in range(0,len(li)):
    if(li[i]<=a):
      vr.append(li[i])
  return vr
lista=[2,3,4,5,1,6,1]
#print(menores_igual_a(lista,5))


#[2,9,10,15,18]
# 11
# [2,9,10]
#BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
def menores_igual_a_ordenada(li:list[int], a:int)->list[int]:
  vr:list[int]=li
  for i in range(0,len(li)):
    if(li[i]>a):
      vr=li[:i]
      break

  return vr
lista2=[2,9,10,15,18]
print(menores_igual_a_ordenada(lista2,15))
