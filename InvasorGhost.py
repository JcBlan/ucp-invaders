from Nave import Nave
from Personaje import Personaje

class InvasorGhost(Personaje):
    
    def __init__(self, vida, vel):
        Personaje.__init__(self, vida, vel)

    def chocar(self, nave):
        nave.vida = nave.vida

    def destruir(self, nave):
        nave.vida -= self.velocidad * 1.2   