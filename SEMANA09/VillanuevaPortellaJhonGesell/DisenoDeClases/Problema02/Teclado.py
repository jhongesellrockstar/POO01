from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contadorTeclados = 0

    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)
        Teclado.contadorTeclados += 1
        self.idTeclado = Teclado.contadorTeclados

    def __str__(self):
        return f"Teclado[id={self.idTeclado}, {super().__str__()}]"
