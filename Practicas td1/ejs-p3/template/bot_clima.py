from obtener_clima import obtener_clima

def bot(clima: str) -> str:
    '''
    Requiere: clima perteneciente a {frio, templado, agradable, caluroso}
    Devuelve: Un mensaje adaptado al clima recibido.
    '''
    return 'Genial! Hoy el clima está {}. Que tengas un excelente día! :)'.format(clima)


temp_actual: int = int(input('Hola! Soy tu Bot del tiempo :D\n¿Cuál es la temperatura actual?: '))
clima: str = obtener_clima(temp_actual)
print(bot(clima))
