from Personaje import Personaje

class Mago(Personaje):

    def __init__(self, nombre, edad, genero, raza):
        super().__init__(nombre, edad, genero, raza)

    def habilidades(self):
        return ["Bola de fuego", "Invocar escudo mágico", "Teletransporte"]