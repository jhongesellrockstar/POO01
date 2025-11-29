class Socio:
    def __init__(self):
        self.nombre = input("Nombre del socio: ").strip()
        self.antiguedad = self._leer_entero("Antigüedad (años): ")

    def _leer_entero(self, msg):
        while True:
            try:
                n = int(input(msg))
                if n >= 0: return n
                print("Debe ser >= 0.")
            except ValueError:
                print("Entrada no válida.")

class Club:
    def __init__(self):
        print("Cargando 3 socios...")
        self.socios = [Socio(), Socio(), Socio()]

    def socio_mayor_antiguedad(self):
        return max(self.socios, key=lambda s: s.antiguedad)

    def imprimir_mayor_antiguedad(self):
        s = self.socio_mayor_antiguedad()
        print(f"Socio con mayor antigüedad: {s.nombre} ({s.antiguedad} años)")

club = Club()
club.imprimir_mayor_antiguedad()
