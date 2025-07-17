import unittest
from obtener_clima import obtener_clima

class TestBotClima(unittest.TestCase):
    def test_frio(self):
        temperatura: int = 10
        respuesta_bot: str = obtener_clima(temperatura)
        respuesta_esperada: str = 'frio'
        self.assertEqual(respuesta_bot, respuesta_esperada)

    def test_templado(self):
        temperatura: int =  11
        respuesta_bot: str =  obtener_clima(temperatura)
        respuesta_esperada: str =  'templado'
        self.assertEqual(respuesta_bot, respuesta_esperada)

    def test_agradable(self):
        temperatura: int =  17
        respuesta_bot: str =  obtener_clima(temperatura)
        respuesta_esperada: str =  'agradable'
        self.assertEqual(respuesta_bot, respuesta_esperada)

    def test_caluroso(self):
        temperatura: int =  26
        respuesta_bot: str =  obtener_clima(temperatura)
        respuesta_esperada: str =  'caluroso'
        self.assertEqual(respuesta_bot, respuesta_esperada)

    # COMPLETAR CON CASOS PARA TODAS LAS RESPUESTAS POSIBLES!


unittest.main()
