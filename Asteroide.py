from Nave import Nave
from Invasor import Invasor

class Asteroide(object):

    def __init__(self, vel):
        self.velocidad = vel
    
    def chocarNave(self, nave):
        nave.vida -= (self.velocidad * nave.velocidad) / 200

    def chocarInvasor(self, invasor):
        invasor.vida -= (self.velocidad * invasor.velocidad) / 200