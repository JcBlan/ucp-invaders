import unittest
from Nave import Nave
from Asteroide import Asteroide
from Invasor import Invasor


class TestInvasor(unittest.TestCase):

    def test_chocar_Nave(self):
        invasor = Invasor(100, 30)
        nave = Nave(100, 100)
        invasor.chocar(nave)
        self.assertTrue(nave.vida == 0)



if __name__ == "__main__":
    unittest.main(exit=False)