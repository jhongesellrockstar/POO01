# problema_CA_2.py
from abc import ABC, abstractmethod

class FiltroTexto(ABC):
    @abstractmethod
    def filtrar(self, nombres):
        pass

class NombresConVocal(FiltroTexto):
    def filtrar(self, nombres):
        vocales = tuple("aeiouáéíóúAEIOUÁÉÍÓÚ")
        return list(filter(lambda s: isinstance(s, str) and len(s) > 0 and s[0] in vocales, nombres))


Nombres = ["Ana", "Luis", "Oscar", "Elena", "Pedro", "Ulises", "Carla"]
filtro = NombresConVocal()
print("Nombres que comienzan con vocal:", filtro.filtrar(Nombres))
