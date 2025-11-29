# Clase base
class Vehiculo:
    def __init__(self, marca, anio):
        self.marca = marca
        self.anio = anio

    def calcular_impuesto(self):
        raise NotImplementedError("Este método debe ser sobrescrito")


# Subclases con polimorfismo
class Auto(Vehiculo):
    def __init__(self, marca, anio, cilindrada):
        super().__init__(marca, anio)
        self.cilindrada = cilindrada

    def calcular_impuesto(self):
        return 0.01 * self.cilindrada


class Moto(Vehiculo):
    def __init__(self, marca, anio, peso):
        super().__init__(marca, anio)
        self.peso = peso

    def calcular_impuesto(self):
        return 0.005 * self.peso


# Lista de vehículos
vehiculos = [
    Auto("Toyota", 2018, 1600),
    Moto("Yamaha", 2020, 300),
    Auto("Honda", 2015, 2000),
    Moto("Suzuki", 2017, 150)
]

# Usando map y lambda para calcular los impuestos
impuestos = list(map(lambda v: v.calcular_impuesto(), vehiculos))
print("Impuestos calculados:", impuestos)

# Filtrar vehículos con impuesto mayor a 15
vehiculos_costosos = list(filter(lambda v: v.calcular_impuesto() > 15, vehiculos))

print("\nVehículos con impuesto mayor a 15:")
for v in vehiculos_costosos:
    tipo = "Auto" if isinstance(v, Auto) else "Moto"
    print(f"{tipo} {v.marca} ({v.anio}) - Impuesto: {v.calcular_impuesto():.2f}")

# Lista de marcas de los vehículos que pagan poco impuesto (<10)
marcas_baratas = [v.marca for v in vehiculos if v.calcular_impuesto() < 10]
print("\nMarcas con bajo impuesto:", marcas_baratas)
