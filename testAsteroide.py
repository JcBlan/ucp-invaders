import unittest
from Nave import Nave
from Asteroide import Asteroide
from Invasor import Invasor


class TestAsteroide(unittest.TestCase):
    
    def test_chocar_Nave(self):
        nave = Nave(100, 50)
        asteroide = Asteroide(40)
        asteroide.chocarNave(nave)
        print("TEST - chocar nave ")
        self.assertTrue(nave.vida == 90)

    def test_chocar_Nave_SinDano(self):
        nave = Nave(100, 50)
        asteroide = Asteroide(0)
        asteroide.chocarNave(nave)
        print("TEST - chocar nave sin daño ")
        self.assertTrue(nave.vida == 100)
    
    
    def test_chocar_Nave_TodaVel(self):
        nave = Nave(100, 100)
        asteroide = Asteroide(100)
        asteroide.chocarNave(nave)
        print("TEST - chocar nave con toda velocidad ")
        self.assertTrue(nave.vida == 50)

    def test_chocar_Invasor(self):
        invasor = Invasor(100, 50)
        asteroide = Asteroide(60)
        asteroide.chocarInvasor(invasor)
        print("TEST - chocar invasor")
        self.assertTrue(invasor.vida == 85)

    
    def test_chocar_Invasor_SinDano(self):
        invasor = Invasor(100, 50)
        asteroide = Asteroide(0)
        asteroide.chocarInvasor(invasor)
        print("TEST - chocar invasor sin daño")
        self.assertTrue(invasor.vida == 100)

    def test_chocar_Invasor_TodaVel(self):
        invasor = Invasor(100, 100)
        asteroide = Asteroide(100)
        asteroide.chocarInvasor(invasor)
        print("TEST - chocar invasor con toda la velocidad")
        self.assertTrue(invasor.vida == 50)
    

if __name__ == "__main__":
    unittest.main(exit=False)
