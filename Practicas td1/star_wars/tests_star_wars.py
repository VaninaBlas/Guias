import unittest

from star_wars import nave_estelar_cercana

class TestMision(unittest.TestCase):

    def test_verdaderos(self):
        self.assertTrue(nave_estelar_cercana([32638, 205, 258, 71115], 250), True)
        self.assertTrue(nave_estelar_cercana([34,67,23], 40 ), True)
        self.assertTrue(nave_estelar_cercana([12,98,23,56,42], 20), True)
        self.assertTrue(nave_estelar_cercana([100000,32000,50000,1234], 5000 ), True)
        self.assertTrue(nave_estelar_cercana([9000,10000,12000,1000], 100001 ), True)


    def test_falsos(self):
        self.assertFalse(nave_estelar_cercana([23,1,12,34,5,6,4], 0), False)
        self.assertFalse(nave_estelar_cercana([89000,30000,23000,12983], 1000), False)
        self.assertFalse(nave_estelar_cercana([450,600,200,800,350], 100 ), False)
        self.assertFalse(nave_estelar_cercana([89,99,44,122], 20 ), False)
        self.assertFalse(nave_estelar_cercana([120,34,90,87,45], 30 ), False)


unittest.main()