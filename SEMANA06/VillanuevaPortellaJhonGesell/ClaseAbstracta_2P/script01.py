# problema_CA_1.py
from abc import ABC, abstractmethod

class FiltroNumerico(ABC):
    @abstractmethod
    def filtrar(self, datos):
        """Retorna una nueva lista con los elementos que cumplen el criterio."""
        pass

class ImparesMayoresCinco(FiltroNumerico):
    def filtrar(self, datos):
        # Usando lambda + filter: impares y > 5
        return list(filter(lambda n: (n % 2 != 0) and (n > 5), datos))

datos = [3, 6, 9, 12, 15, 2, 7, 5, 10]
filtro = ImparesMayoresCinco()
resultado = filtro.filtrar(datos)
print("Impares mayores a 5:", resultado)
