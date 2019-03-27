import unittest



class TestDestruir(unittest.TestCase):
    def test_destruir(self):
        invasor = Invasor(100, 30)
        nave = Nave(100, 50)
        invasor.destruir(nave)
        self.assertLess(nave.vida , 100)


