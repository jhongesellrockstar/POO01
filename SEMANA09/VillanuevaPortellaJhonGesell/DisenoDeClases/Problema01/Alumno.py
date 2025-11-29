class Alumno:
    contador_alumnos = 0

    def __init__(self, nombre, ponderado, creditos):
        Alumno.contador_alumnos += 1
        self.id_alumno = Alumno.contador_alumnos
        self.nombre = nombre
        self.ponderado = ponderado
        self.creditos = creditos
        self.pension = creditos * 80  # según diagrama del docente

    def __str__(self):
        return (f"Alumno(id={self.id_alumno}, nombre={self.nombre}, "
                f"ponderado={self.ponderado}, creditos={self.creditos}, "
                f"pension={self.pension})")
