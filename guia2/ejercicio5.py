# ESTE CODIGO TIENE HORRORES !!!

def inverso(x: float) -> float:
    '''Requiere: x!=0
       Devuelve: el resultado de dividir 1 por x. 
    '''
    return 1/x


def cuadrado(n: int) -> int:
  ``` Requiere: Nada. # HORROR 3: no se pone ese signo para hacer comentarios
      Devuelve: el resutlado de elevar n al cuadrado.
  ```
  return n**n # HORROR 7: ASI NO SE SACA EL CUADRADO ESTO ES LO MISMO QUE 5**5, HAY UN * DE MAS

n:int = 3
print("El cuadrado de", n, "es", cuardado(n))# HORROR 6: esta mal escrito cuadrado

n:int = "hola" # HORROR 2: para que pones que es int si lo declaras str
print("El cuadrado de", n, "es", cuadrado(n)) # COMO CONSECUENCIA esto no funciona ya que n es str

x:float = 2.0
print("El inverso de", x, "es", inverso(x))) # HORROR 1: hay un ) de mas

#la declaracion hace que como consecuencia el print de error
x:float = O.0 # HORROR 4: ESO ES UNA O NO UN CERO y ni siquiera es posible declarar algo asi
print("El inverso de", x, "es", inverso(X)) # HORROR 5: esa X no existe!!! es en minuscula


