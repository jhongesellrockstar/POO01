#ABC=Abstract Base Class
from abc import ABC, abstractmethod

# Clase abstracta Vehiculo
class Vehiculo(ABC):
    
    # Método abstracto
    @abstractmethod
    def arrancar(self):
        pass

# Clase Coche que hereda de Vehiculo
class Coche(Vehiculo):
    
    # Implementación del método abstracto
    def arrancar(self):
        print("El coche está arrancando...")

# Clase Moto que hereda de Vehiculo
class Moto(Vehiculo):
    
    # Implementación del método abstracto
    def arrancar(self):
        print("La moto está arrancando...")

# No se puede instanciar directamente la clase abstracta
# vehiculo = Vehiculo() # Esto generaría un error

# Instanciar las clases hijas y llamar a los métodos
coche = Coche()
coche.arrancar()  # Salida: El coche está arrancando...

moto = Moto()
moto.arrancar()  # Salida: La moto está arrancando...
