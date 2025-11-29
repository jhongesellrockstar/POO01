class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

class Automovil(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

print('Creamos un objeto de la clase Vehiculo')
vehiculo = Vehiculo('Rojo', 4)
print(f'color: {vehiculo.color}')
print(f'ruedas: {vehiculo.ruedas}')

print('Creamos un objeto de la clase hija Coche')
coche = Automovil('Azul', 4, 150)
print(f'color: {coche.color}')
print(f'ruedas: {coche.ruedas}')
print(f'velocidad: {coche.velocidad}')

print('Creamos un objeto de la clase hija Bicicleta')
bicicleta = Bicicleta('Blanca', 2, 'Urbano')
print(f'color: {bicicleta.color}')
print(f'ruedas: {bicicleta.ruedas}')
print(f'tipo: {bicicleta.tipo}')
