class Vehiculo:
    contador_vehiculos = 0

    def __init__(self, marca):
        self.marca = marca
        Vehiculo.contador_vehiculos += 1

# Crear varios objetos
v1 = Vehiculo("Toyota")
v2 = Vehiculo("Ford")
v3 = Vehiculo("Honda")

# Mostrar cuántos vehículos se crearon
print(f"Vehículos creados: {Vehiculo.contador_vehiculos}")
