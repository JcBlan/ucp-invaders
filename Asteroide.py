from Nave import Nave
from Invasor import Invasor
from Artefacto import Artefacto

class Asteroide(Artefacto):

    def __init__(self, vel):
        Artefacto.__init__(self, vel)
    
    def chocarNave(self, nave):
        nave.vida -= (self.velocidad * nave.velocidad) / 200

    def chocarInvasor(self, invasor):
        invasor.vida -= (self.velocidad * invasor.velocidad) / 200