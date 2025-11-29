class Alumno:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__notas = []  # privada

    def agregar_nota(self, nota):
        # validación típica (escala 0-20)
        n = float(nota)
        if n < 0 or n > 20:
            print("nota fuera de rango (0-20)")
            return
        self.__notas.append(n)

    def obtener_notas(self):
        # no exponemos la lista real: devolvemos copia
        return list(self.__notas)

    def promedio(self):
        if len(self.__notas) == 0:
            return 0
        return sum(self.__notas) / len(self.__notas)

    def mostrar(self):
        print("alumno:", self.__nombre, "| notas:", self.obtener_notas(), "| prom:", self.promedio())

# Pruebas
a = Alumno("Jhon")
a.agregar_nota(18)
a.agregar_nota(15)
a.agregar_nota(20)
a.agregar_nota(25)   # fuera de rango -> rechazada
a.mostrar()