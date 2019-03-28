from Artefacto import Artefacto


class Personaje(Artefacto):
    def __init__(self, vida , vel):
        Artefacto.__init__(self, vel)
        self.vida = vida