def obtener_clima(temp: int) -> str:
    '''
    Requiere: nada
    Devuelve: como esta el clima, menor o igual a 10 "frio", mayor a 10 y menor a 17 "templado", mayor igual a 17 y menor igual a 25 "agradable", sino "caluroso"
    '''
    clima:str=''
    if(temp<=10):
        clima="frio"
    elif(temp>10 and temp<17):
        clima="templado"
    elif(temp>=17 and temp<=25):
        clima="agradable"
    else:
        clima="caluroso"
    return clima

#print(obtener_clima(5.6))
