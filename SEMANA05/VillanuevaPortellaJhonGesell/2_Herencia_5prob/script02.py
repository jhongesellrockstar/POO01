class Vehiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    def mostrar_info(self):
        print(f"Marca: {self.__marca} | Modelo: {self.__modelo}")

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.__puertas = puertas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Puertas: {self.__puertas}")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindraje_cc):
        super().__init__(marca, modelo)
        self.__cilindraje_cc = cilindraje_cc

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cilindraje: {self.__cilindraje_cc} cc")

# prueba rápida
a = Automovil("Toyota", "Yaris", 4); a.mostrar_info()
m = Motocicleta("Honda", "CBR", 600); m.mostrar_info()
