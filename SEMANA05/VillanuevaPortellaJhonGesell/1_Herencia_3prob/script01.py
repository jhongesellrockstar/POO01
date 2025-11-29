# Clase padre
class Operacion:
    def __init__(self, v1=0, v2=0):
        self.valor1 = v1
        self.valor2 = v2
        self.resultado = 0

    def cargar1(self, v):
        self.valor1 = v

    def cargar2(self, v):
        self.valor2 = v

    def mostrar_resultado(self):
        print("El resultado es:", self.resultado)


# Clase hija Suma
class Suma(Operacion):
    def operar(self):
        self.resultado = self.valor1 + self.valor2


# Clase hija Resta
class Resta(Operacion):
    def operar(self):
        self.resultado = self.valor1 - self.valor2


# Prueba
opera01 = Suma(4, 3)
opera01.operar()
opera01.mostrar_resultado()
