from Artefacto import Artefacto

class Nave(Artefacto):
    
    def __init__(self, vida, vel):
        self.vida = vida
        Artefacto.__init__(self, vel)


    def destruir(self, invasor):
        invasor.vida  -= ((self.velocidad * invasor.velocidad) / 100)

    def destruirGhost(self, ghost):
        pass
