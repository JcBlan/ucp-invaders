import unittest
from Nave import Nave
from Invasor import Invasor



class TestDestruir(unittest.TestCase):
    def test_destruir(self):
        invasor = Invasor(100, 30)
        nave = Nave(100, 50)
        nave.destruir(invasor)
        print("TEST - destruir invasor")
        self.assertTrue(invasor.vida == 85)
    
    def test_destruir_TodoDano(self):
        invasor = Invasor(100, 100)
        nave = Nave(100, 100)
        nave.destruir(invasor)
        print("TEST - destruir invasor con todo el daño")
        self.assertTrue(invasor.vida == 0)

    def test_destruir_Invasor_SinDano(self):
        invasor = Invasor(100, 0)
        nave = Nave(100, 0)
        nave.destruir(invasor)
        print("TEST - destruir invasor sin daño ")
        self.assertTrue(invasor.vida == 100)
    
if __name__ == "__main__":
    unittest.main(exit=False)


