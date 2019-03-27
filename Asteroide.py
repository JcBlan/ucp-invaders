from Nave import Nave
from Invasor import Invasor

class Asteroide(object):

    def __init__(self, vel):
        self.velocidad = vel
    
    def chocar(self, nave):
        nave.vida -= (self.velocidad * nave.velocidad) / 200
