def f2c(tempFahr: float) -> float:
    """
    Requiere:nada 
    Devuelve: la temp en celcius
    """
    cel:float = 5/9 * (tempFahr-32)
    return cel

ejemplo1:float=80.0
ejemplo1= f2c(ejemplo1)
print(ejemplo1)

ejemplo2:float=90.0
ejemplo2=(f2c(ejemplo2))
print(ejemplo2)

ejemplo3:float=20.0
ejemplo3=(f2c(ejemplo3))
print(ejemplo3)

ejemplo4:float=28.0
ejemplo4=(f2c(ejemplo4))
print(ejemplo4)

ejemplo5:float=12.0
ejemplo5=(f2c(ejemplo5))
print(ejemplo5)
