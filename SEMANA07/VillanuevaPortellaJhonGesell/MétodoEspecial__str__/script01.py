# Problem01:
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Vehiculo[Color : {self.color}, Ruedas : {self.ruedas}]'
    
class Automovil(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'Automovil[{super().__str__()}, Velocidad : {self.velocidad}]'
    
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'Bicicleta[{super().__str__()}, Tipo : {self.tipo}]'
    
vehiculo1 = Vehiculo('Rojo', 4)
automovil1 = Automovil('Azul', 4, 150)
bicicleta1 = Bicicleta('Blanca', 2, 'Urbano')

print(vehiculo1)
print(automovil1)
print(bicicleta1)
