from Nave import Nave

class Invasor(object):
    
    def __init__(self, life, vel):
        self.vida = life
        self.velocidad = vel

    def chocar(self, nave):
        nave.vida = 0    

    