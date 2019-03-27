import unittest
from Nave import Nave
from Asteroide import Asteroide
from Invasor import Invasor


class TestInvasor(unittest.TestCase):

    def test_chocar(self):
        invasor = Invasor(100, 30)
        nave = Nave(100, 100)
        invasor.chocar(nave)
        print("TEST - chocar nave ")
        self.assertTrue(nave.vida == 0)
    
    def test_destruir(self):
        invasor = Invasor(100, 50)
        nave = Nave(100, 60)
        invasor.destruir(nave)
        print("TEST - destruir nave ")
        self.assertTrue(nave.vida == 40)
    
    def test_destruir_SinDano(self):
        invasor = Invasor(100, 0)
        nave = Nave(100, 60)
        invasor.destruir(nave)
        print("TEST - destruir nave sin daño ")
        self.assertTrue(nave.vida == 100)

    def test_destruir_TodoDano(self):
        invasor = Invasor(100, 100)
        nave = Nave(100, 60)
        invasor.destruir(nave)
        print("TEST - destruir nave con todo el daño")
        self.assertLessEqual(nave.vida, 0)


if __name__ == "__main__":
    unittest.main(exit=False)