# Clase padre
class Poligono:
    def __init__(self, nombre):
        self.__nombre = nombre   # atributo protegido

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre


# Clase hija Cuadrilatero
class Cuadrilatero(Poligono):
    def __init__(self, nombre, num_lados, tipo):
        super().__init__(nombre)
        self.__num_lados = num_lados      # atributo privado
        self.__tipo = tipo                # atributo privado

    # getters y setters
    def get_num_lados(self):
        return self.__num_lados

    def set_num_lados(self, num_lados):
        self.__num_lados = num_lados

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo


# Clase hija Rectangulo
class Rectangulo(Cuadrilatero):
    def __init__(self, nombre, num_lados, tipo, largo, alto):
        super().__init__(nombre, num_lados, tipo)
        self.__largo = largo      # atributos protegidos
        self.__alto = alto

    # getters y setters
    def get_largo(self):
        return self.__largo

    def set_largo(self, largo):
        self.__largo = largo

    def get_alto(self):
        return self.__alto

    def set_alto(self, alto):
        self.__alto = alto

    # métodos específicos
    def area(self):
        return self.__largo * self.__alto

    def perimetro(self):
        return 2 * (self.__largo + self.__alto)

    def listado(self):
        print("=== Datos del Rectángulo ===")
        print("Nombre:", self.get_nombre())
        print("Número de lados:", self.get_num_lados())
        print("Tipo:", self.get_tipo())
        print("Largo:", self.__largo)
        print("Alto:", self.__alto)
        print("Área:", self.area())
        print("Perímetro:", self.perimetro())


# ---- Uso directo ----
rect = Rectangulo("Rectángulo", 4, "Regular", 12, 6)
rect.listado()
