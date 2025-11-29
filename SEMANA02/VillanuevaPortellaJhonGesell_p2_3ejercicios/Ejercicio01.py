"""
Disenie la clase Docente con los atributos publicos
> Codigo (Tipo entero)
> Nombre (Tipo cadena)
> Horas trabajadas (Tipo entero)
> Tarifa por hora (Tipo real)
Implemente, ademas:
> Un método público que retorne el sueldo (horas*tarifa)
Tomando la clase Docente:
> Declare y cree un objeto tipo Docente
> Ingrese datos fijos
> Visualice todos sus datos
"""


class Docente:
    def __init__(self, codigo, nombre, horas_trabajadas, tarifa_por_hora):
        self.codigo = codigo
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def sueldo(self):
        return self.horas_trabajadas * self.tarifa_por_hora

    def mostrar_datos(self):
        print("Código:", self.codigo)
        print("Nombre:", self.nombre)
        print("Horas trabajadas:", self.horas_trabajadas)
        print("Tarifa por hora:", self.tarifa_por_hora)
        print("Sueldo total:", self.sueldo())


trabajador = Docente(70585223, "Jhon", 10, 70.0)
trabajador.mostrar_datos()
