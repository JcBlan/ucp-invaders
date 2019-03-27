import unittest
from Nave import Nave
from Asteroide import Asteroide


class TestAsteroide(unittest.TestCase):
    
    def test_chocar_nave(self):
        nave = Nave(100, 50)
        asteroide = Asteroide(40)
        asteroide.chocar(nave)
        self.assertTrue(nave.vida == 20)

if __name__ == "__main__":
    unittest.main(exit=False)
