from abc import ABC, abstractmethod
import math

# Clase abstracta para las formas geométricas
class FormaGeometrica(ABC):
    
    # Método abstracto para calcular el área
    @abstractmethod
    def area(self):
        pass

    # Método abstracto para calcular el perímetro
    @abstractmethod
    def perimetro(self):
        pass

# Clase Circulo que hereda de FormaGeometrica
class Circulo(FormaGeometrica):
    
    def __init__(self, radio):
        self.radio = radio
    
    # Implementación del método para calcular el área del círculo
    def area(self):
        return math.pi * (self.radio ** 2)
    
    # Implementación del método para calcular el perímetro del círculo
    def perimetro(self):
        return 2 * math.pi * self.radio

# Clase Cuadrado que hereda de FormaGeometrica
class Cuadrado(FormaGeometrica):
    
    def __init__(self, lado):
        self.lado = lado
    
    # Implementación del método para calcular el área del cuadrado
    def area(self):
        return self.lado ** 2
    
    # Implementación del método para calcular el perímetro del cuadrado
    def perimetro(self):
        return 4 * self.lado

# No se puede instanciar directamente la clase abstracta FormaGeometrica
# forma = FormaGeometrica()  # Esto generaría un error

# Instancias de las clases hijas
circulo = Circulo(5)
print(f"Área del círculo: {circulo.area():.2f}")       # Salida: Área del círculo: 78.54
print(f"Perímetro del círculo: {circulo.perimetro():.2f}")  # Salida: Perímetro del círculo: 31.42

cuadrado = Cuadrado(4)
print(f"Área del cuadrado: {cuadrado.area()}")       # Salida: Área del cuadrado: 16
print(f"Perímetro del cuadrado: {cuadrado.perimetro()}")  # Salida: Perímetro del cuadrado: 16
