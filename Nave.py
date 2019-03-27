
class Nave():
    
    def __init__(self, vida, vel):
        self.vida = vida
        self.velocidad = vel


    def destruir(self, nave):
        self.vida  -= ((self.velocidad * nave.velocidad) / 100)