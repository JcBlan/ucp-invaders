import unittest
from Nave import Nave
from Asteroide import Asteroide
from InvasorGhost import InvasorGhost


class TestInvasor(unittest.TestCase):
    
    def test_chocar(self):
        invasor = InvasorGhost(100, 30)
        nave = Nave(100, 50)
        invasor.chocar(nave)
        print("TEST - chocar nave ")
        self.assertTrue(nave.vida == 100)
    
    def test_chocar_TodaVel(self):
        invasor = InvasorGhost(100, 100)
        nave = Nave(100, 100)
        invasor.chocar(nave)
        print("TEST - chocar nave toda velocidad")
        self.assertTrue(nave.vida == 100)
    
    
    def test_chocar_SinVel(self):
        invasor = InvasorGhost(100, 100)
        nave = Nave(100, 0)
        invasor.chocar(nave)
        print("TEST - chocar nave sin velocidad")
        self.assertTrue(nave.vida == 100)
    
    def test_destruir_Nave(self):
        invasorGhost = InvasorGhost(100, 50)
        nave = Nave(100, 60)
        nave.destruirGhost(invasorGhost)
        print("TEST - destruir invasorGhost ")
        self.assertTrue(invasorGhost.vida == 100)
    
    
    def test_destruir_Invasor(self):
        invasorGhost = InvasorGhost(100, 50)
        nave = Nave(100, 60)
        invasorGhost.destruir(nave)
        print("TEST - destruir nave ")
        self.assertTrue(nave.vida == 40)
    


if __name__ == "__main__":
    unittest.main(exit=False)