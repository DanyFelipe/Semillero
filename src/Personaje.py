from abc import ABC, abstractmethod

class Personaje(ABC):

    def __init__(self, nombre, edad, genero, raza):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.raza = raza

    @abstractmethod
    def habilidades(self):
        pass