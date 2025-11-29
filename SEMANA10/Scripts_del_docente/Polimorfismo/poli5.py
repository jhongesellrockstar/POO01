'''Ejemplo: Sistema de vehículos, colores, y marcas
Enunciado:

Crea clases para diferentes tipos de vehículos (Auto, Camion, Motocicleta)
que heredan de una clase base Vehiculo.
Implementa en cada clase métodos descripcion(), __str__().
Crea clases adicionales para agregar atributos como Color y Marca.
Crea una clase VehiculoColorMarca que herede de Vehiculo, Color, 
y Marca (herencia múltiple).
Usa polimorfismo en una función que reciba una lista de vehículos y muestre 
su descripción y atributos.
Crea un diccionario que agrupe los vehículos por tipo y usa comprensiones
para listar los modelos con más de cierta capacidad o potencia.
Usa map() y lambda para calcular y mostrar el valor total de todos los vehículos.
Usa condicionales y bucles para mostrar mensajes específicos si hay vehículos
de cierto tipo o atributos.'''

# Importar ABC y abstractmethod
from abc import ABC, abstractmethod

# Clase base abstracta
class Vehiculo(ABC):
    def __init__(self, modelo):
        self.modelo = modelo

    @abstractmethod
    def descripcion(self):
        pass

    def __str__(self):
        return f"Modelo: {self.modelo}"

# Clases atributo
class Color:
    def __init__(self, color):
        self.color = color
    def __str__(self):
        return f"Color: {self.color}"

class Marca:
    def __init__(self, marca):
        self.marca = marca
    def __str__(self):
        return f"Marca: {self.marca}"

# Clases concreta de vehículos
class Auto(Vehiculo):
    def __init__(self, modelo, capacidad):
        super().__init__(modelo)
        self.capacidad = capacidad

    def descripcion(self):
        return f"Auto {self.modelo} con capacidad para {self.capacidad} personas."

class Camion(Vehiculo):
    def __init__(self, modelo, carga):
        super().__init__(modelo)
        self.carga = carga

    def descripcion(self):
        return f"Camion {self.modelo} con carga de {self.carga} toneladas."

class Motocicleta(Vehiculo):
    def __init__(self, modelo, potencia):
        super().__init__(modelo)
        self.potencia = potencia

    def descripcion(self):
        return f"Motocicleta {self.modelo} con potencia de {self.potencia} HP."

# Clase con herencia múltiple
class VehiculoColorMarca(Vehiculo, Color, Marca):
    def __init__(self, modelo, color, marca):
        Vehiculo.__init__(self, modelo)
        Color.__init__(self, color)
        Marca.__init__(self, marca)

    def descripcion(self):
        return f"{self.marca} {self.modelo} de color {self.color}"

# Función polimórfica para mostrar detalles
def mostrar_detalles_vehiculos(lista):
    for v in lista:
        print(v)
        print(v.descripcion())
        print()

# Crear la lista de vehículos
vehiculos = [
    Auto("Model S", 5),
    Camion("F-150", 2),
    Motocicleta("Ninja", 150),
    VehiculoColorMarca("Model X", "Rojo", "Tesla"),
    VehiculoColorMarca("Camaro", "Azul", "Chevrolet"),
    VehiculoColorMarca("Ducati", "Negro", "Ducati")
]

# Agrupar en diccionarios por tipo
diccionario_tipos = {
    "Auto": [v for v in vehiculos if isinstance(v, Auto)],
    "Camion": [v for v in vehiculos if isinstance(v, Camion)],
    "Motocicleta": [v for v in vehiculos if isinstance(v, Motocicleta)],
    "ColorMarca": [v for v in vehiculos if isinstance(v, VehiculoColorMarca)],
}

# Operación: calcular el valor total por tipo agrupado en el diccionario

print('calcular el valor total por tipo agrupado en el diccionario')
total_por_tipo = {}
for tipo, lista_objetos in diccionario_tipos.items():
    total = sum(
        v.capacidad * 1000 if isinstance(v, Auto) else
        v.carga * 500 if isinstance(v, Camion) else
        v.potencia * 200 if isinstance(v, Motocicleta) else
        0
        for v in lista_objetos
    )
    total_por_tipo[tipo] = total

# Mostrar los resultados
print("\nTotal estimado por tipo de vehículo en el Diccionario:")
for tipo, total in total_por_tipo.items():
    print(f"{tipo}: ${total}")
print()


# Mostrar detalles (polimorfismo)
print("Detalles de todos los vehículos:")
mostrar_detalles_vehiculos(vehiculos)

# Crear lista de costes usando map y lambda
costes = list(
    map(
        lambda v: v.capacidad * 1000 if isinstance(v, Auto) else
                  v.carga * 500 if isinstance(v, Camion) else
                  v.potencia * 200 if isinstance(v, Motocicleta) else
                  0,
        vehiculos
    )
)

# Mostrar los costes
print("Costes estimados de cada vehículo:", costes)

# Sumarlos todos
total_coste = sum(costes)
print(f"El coste total estimado de todos los vehículos es: ${total_coste}")

# Filtrar vehículos con capacidad mayor a 4 (auto) o carga mayor a 2 (camión)
vehiculos_grandes = [
    v for v in vehiculos 
    if (isinstance(v, Auto) and v.capacidad > 4) or (isinstance(v, Camion) and v.carga > 2)
]

# Mostrar vehículos grandes
print("\nVehículos con capacidad superior a 4 o carga superior a 2:")
for v in vehiculos_grandes:
    print(v)
    print(v.descripcion())
