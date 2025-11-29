from abc import ABC, abstractmethod

# Clase abstracta base
class Usuario(ABC):
    def __init__(self, nombre, correo):
        self.__nombre = nombre
        self.__correo = correo
        self.libros = []

    @abstractmethod
    def recomendar_libro(self):
        pass

    def registrar_libro(self, libro):
        if not isinstance(libro, Libro):
            raise ValueError("Solo se pueden registrar objetos de tipo Libro.")
        self.libros.append(libro)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.__nombre} ({self.__correo})"

# Comportamiento académico
class Academico:
    def obtener_estadisticas_libros(self):
        largos = list(filter(lambda l: len(l.titulo) > 15, self.libros))
        destacados = list(filter(lambda l: l.calificacion >= 4.5, self.libros))
        return {
            "libros_largos": list(map(lambda l: l.titulo, largos)),
            "libros_destacados": list(map(lambda l: l.titulo, destacados))
        }

# Comportamiento lector
class Lector:
    def mostrar_libros(self):
        for libro in self.libros:
            print(libro)

# Herencia múltiple
class Estudiante(Usuario, Academico, Lector):
    def recomendar_libro(self):
        return "Recomendación: libros introductorios y de estudio."

class Profesor(Usuario, Academico, Lector):
    def recomendar_libro(self):
        return "Recomendación: libros especializados y de investigación."

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, calificacion):
        self.titulo = titulo
        self.autor = autor
        self.calificacion = calificacion

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} - Calificación: {self.calificacion}"

# Pruebas
if __name__ == "__main__":
    try:
        est = Estudiante("Ana", "ana@correo.com")
        prof = Profesor("Dr. Luis", "luis@uni.edu.pe")

        libro1 = Libro("Introducción a la Física", "Feynman", 4.8)
        libro2 = Libro("Cálculo", "Stewart", 4.2)
        libro3 = Libro("Teoría Cuántica de Campos", "Peskin", 4.9)

        est.registrar_libro(libro1)
        est.registrar_libro(libro2)
        prof.registrar_libro(libro3)

        print(est)
        est.mostrar_libros()
        print(est.recomendar_libro())
        print(est.obtener_estadisticas_libros())

        print(prof)
        prof.mostrar_libros()
        print(prof.recomendar_libro())
        print(prof.obtener_estadisticas_libros())

        est.registrar_libro("no es un libro")  # Provoca excepción

    except Exception as e:
        print("Error:", e)
