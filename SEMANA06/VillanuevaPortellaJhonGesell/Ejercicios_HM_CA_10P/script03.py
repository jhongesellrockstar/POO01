# script03.py
class Dispositivo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        return f"{self.marca} {self.modelo}"

class Smartphone(Dispositivo):
    def __init__(self, marca, modelo, sistema_operativo, numero_telefono):
        super().__init__(marca, modelo)
        self.sistema_operativo = sistema_operativo
        self.numero_telefono = numero_telefono

class Tablet(Dispositivo):
    def __init__(self, marca, modelo, tamaño_pantalla, tipo_conectividad):
        super().__init__(marca, modelo)
        self.tamaño_pantalla = tamaño_pantalla
        self.tipo_conectividad = tipo_conectividad

class DispositivoPortatil(Smartphone, Tablet):
    def __init__(self, marca, modelo, sistema_operativo, numero_telefono,
                 tamaño_pantalla, tipo_conectividad):
        Smartphone.__init__(self, marca, modelo, sistema_operativo, numero_telefono)
        Tablet.__init__(self, marca, modelo, tamaño_pantalla, tipo_conectividad)

    def compatible_con(self, accesorio:str) -> bool:
        accesorio = accesorio.lower()
        if "bluetooth" in accesorio:
            return True
        if "usb-c" in accesorio and "usb" in self.tipo_conectividad.lower():
            return True
        return False

if __name__ == "__main__":
    d = DispositivoPortatil("Zeta", "OneX", "Android", "+51-900000000", 10.5, "WiFi/USB-C")
    print(d.mostrar_info())
    for acc in ["Teclado Bluetooth", "Cargador USB-C", "Lápiz propietario"]:
        print(acc, "->", "Compatible" if d.compatible_con(acc) else "No compatible")
