import unittest
from Nave import Nave
from Invasor import Invasor



class TestDestruir(unittest.TestCase):
    def test_destruir(self):
        invasor = Invasor(100, 30)
        nave = Nave(100, 50)
        nave.destruir(invasor)
        self.assertTrue(invasor.vida == 85)
    
    def test_No_destruir(self):
        invasor = Invasor(100, 100)
        nave = Nave(100, 100)
        nave.destruir(invasor)
        self.assertTrue(invasor.vida == 0)

    def test_destruir_completo(self):
        invasor = Invasor(100, 0)
        nave = Nave(100, 0)
        nave.destruir(invasor)
        self.assertTrue(invasor.vida == 100)
    
if __name__ == "__main__":
    unittest.main(exit=False)


