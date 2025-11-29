from abc import ABC, abstractmethod

# Clase base abstracta
class Dispositivo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False

    @abstractmethod
    def encender(self):
        pass

    def apagar(self):
        self.encendido = False
        print(self.marca, self.modelo, "apagado.")

    def reiniciar(self):
        if self.encendido:
            print(self.marca, self.modelo, "reiniciando...")
        else:
            print("No se puede reiniciar:", self.marca, self.modelo, "está apagado.")

    @abstractmethod
    def mostrar_informacion(self):
        pass


# Subclase Laptop
class Laptop(Dispositivo):
    def __init__(self, marca, modelo, cantidad_ram, procesador):
        Dispositivo.__init__(self, marca, modelo)
        self.cantidad_ram = cantidad_ram
        self.procesador = procesador

    def encender(self):
        self.encendido = True
        print("Laptop", self.marca, self.modelo, "encendida.")

    def mostrar_informacion(self):
        print("Laptop:", self.marca, self.modelo,
              "| RAM:", str(self.cantidad_ram) + "GB",
              "| CPU:", self.procesador)


# Subclase Tableta
class Tableta(Dispositivo):
    def __init__(self, marca, modelo, tamaño_pantalla, tipo_bateria):
        Dispositivo.__init__(self, marca, modelo)
        self.tamaño_pantalla = tamaño_pantalla
        self.tipo_bateria = tipo_bateria

    def encender(self):
        self.encendido = True
        print("Tableta", self.marca, self.modelo, "encendida.")

    def mostrar_informacion(self):
        print("Tableta:", self.marca, self.modelo,
              "| Pantalla:", str(self.tamaño_pantalla) + '"',
              "| Batería:", self.tipo_bateria)


# Ejecución directa sin bloque if
laptop1 = Laptop("Andes", "L14", 16, "Ryzen 7")
tableta1 = Tableta("Andes", "T10", 10.1, "Li-Ion 7000mAh")

laptop1.encender()
laptop1.mostrar_informacion()
laptop1.reiniciar()
laptop1.apagar()

tableta1.encender()
tableta1.mostrar_informacion()
tableta1.reiniciar()
tableta1.apagar()
