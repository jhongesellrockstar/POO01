from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contadorRatones = 0

    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)
        Raton.contadorRatones += 1
        self.idRaton = Raton.contadorRatones

    def __str__(self):
        return f"Raton[id={self.idRaton}, {super().__str__()}]"
