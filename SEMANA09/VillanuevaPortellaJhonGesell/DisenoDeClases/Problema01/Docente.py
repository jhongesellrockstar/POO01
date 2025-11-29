from Alumno import Alumno

class Docente:
    contador_docentes = 0

    def __init__(self, nombre, horas, tarifa_por_hora):
        Docente.contador_docentes += 1
        self.id_docente = Docente.contador_docentes
        self.nombre = nombre
        self.horas = horas
        self.tarifa_por_hora = tarifa_por_hora
        self.sueldo = horas * tarifa_por_hora
        self.alumnos = []  # lista de objetos Alumno

    def agregar_alumno(self, alumno: Alumno):
        self.alumnos.append(alumno)

    def __str__(self):
        alumnos_nombres = ', '.join([a.nombre for a in self.alumnos]) or "Sin alumnos"
        return (f"Docente(id={self.id_docente}, nombre={self.nombre}, "
                f"horas={self.horas}, tarifa={self.tarifa_por_hora}, "
                f"sueldo={self.sueldo}, alumnos=[{alumnos_nombres}])")
