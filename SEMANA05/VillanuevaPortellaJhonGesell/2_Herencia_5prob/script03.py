class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = float(salario)

    def datos(self):
        print("empleado:", self.__nombre, "| salario:", self.__salario)

    # utilitario para que las subclases ajusten el salario
    def _sumar_salario(self, monto):
        self.__salario = self.__salario + float(monto)

class Gerente(Empleado):
    def subir_subsidio(self, monto):
        self._sumar_salario(monto)
        print("subsidio aplicado al gerente por:", monto)

class Vendedor(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)
        self.__total_vendido = 0.0

    def vender(self, monto):
        self.__total_vendido = self.__total_vendido + float(monto)
        print("venta registrada por:", monto)

    def resumen_ventas(self):
        print("total vendido:", self.__total_vendido)

# Pruebas
ger = Gerente("Ana", 3500)
ven = Vendedor("Luis", 1800)

ger.datos()
ger.subir_subsidio(400)
ger.datos()

ven.datos()
ven.vender(2500)
ven.vender(800)
ven.resumen_ventas()