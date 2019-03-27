
class Nave(object):
    
    def __init__(self, vida, vel):
        self.vida = vida
        self.velocidad = vel


    def destruir(self, invasor):
        invasor.vida  -= ((self.velocidad * invasor.velocidad) / 100)

    def destruirGhost(self, ghost):
        pass
