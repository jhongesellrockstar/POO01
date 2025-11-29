class DispositivoEntrada:
    def __init__(self, tipo_entrada, marca):
        self.tipo_entrada = tipo_entrada
        self.marca = marca

    def __str__(self):
        return f"{self.marca} ({self.tipo_entrada})"
