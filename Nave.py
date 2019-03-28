from Personaje import Personaje

class Nave(Personaje):
    
    def __init__(self, vida, vel):
        Personaje.__init__(self, vida, vel)


    def destruir(self, invasor):
        invasor.vida  -= ((self.velocidad * invasor.velocidad) / 100)

    def destruirGhost(self, ghost):
        pass
