from Nave import Nave

class Asteroide(object):

    def __init__(self, vel):
        self.velocidad = vel
    
    def chocar(self, nave):
        nave.vida -= self.velocidad * 2