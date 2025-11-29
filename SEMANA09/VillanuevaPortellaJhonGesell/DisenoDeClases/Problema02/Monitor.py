class Monitor:
    contadorMonitores = 0

    def __init__(self, marca, tamano):
        Monitor.contadorMonitores += 1
        self.idMonitor = Monitor.contadorMonitores
        self.marca = marca
        self.tamano = tamano  # ej. "24 pulgadas"

    def __str__(self):
        return f"Monitor[id={self.idMonitor}, marca={self.marca}, tamano={self.tamano}]"
