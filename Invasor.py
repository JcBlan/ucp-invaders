from Nave import Nave
from Personaje import Personaje

class Invasor(Personaje):
    
    def __init__(self, vida, vel):
        Personaje.__init__(self, vida, vel)

    def chocar(self, nave):
        nave.vida = 0 

    def destruir(self, nave):
        nave.vida -= self.velocidad * 1.2   

    