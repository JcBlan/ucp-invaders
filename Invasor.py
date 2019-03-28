from Nave import Nave
from Artefacto import Artefacto

class Invasor(Artefacto):
    
    def __init__(self, life, vel):
        self.vida = life
        Artefacto.__init__(self, vel)

    def chocar(self, nave):
        nave.vida = 0 

    def destruir(self, nave):
        nave.vida -= self.velocidad * 1.2   

    