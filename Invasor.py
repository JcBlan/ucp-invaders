from Nave import Nave

class Invasor(object):
    
    def __init__(self, life, vel):
        self.vida = life
        self.velocidad = vel

    def chocar(self, nave):
        nave.vida = 0 

    def destruir(self, nave):
        nave.vida -= self.velocidad * 1.2   

    