'''
- Crear la clase padre "Poligono", con el atributo protegido "nombre".
- Heredar de la clase "Polígono" a la clase "Cuadrilatero" con los
  atributos privados:
    o num_lados: Indica el número de lados 
    o tipo: Indica si es regular o irregular
- Heredar de la clase "Cuadrilatero" a la clase "Rectangulo" con los 
  atributos protegidos:
    o largo: Expresa la medida en un valor numérico.
    o alto: Expresa la medida en un valor numérico.
  Además implemnetar:
    o Los métodos get y set de los atributos de instancia
    o El método "area", que retorna el valor del área
    o El método "perimetro" que retorna el valor del perímetro
    o El metodo listado que muestra todo lo referente a la clase
      "Recangulo"
- Crear un objeto de tipo rectángulo y utilizar el método listado()
  para mostrar lo referente al objeto de tipo "Rectángulo"

'''
class Poligono:
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre


class Cuadrilatero(Poligono):
    def __init__(self, nombre, lados, tipo):
        super().__init__(nombre)
        self.__lados = lados
        self.__tipo = tipo

    @property
    def lados(self):
        return self.__lados

    @property
    def tipo(self):
        return self.__tipo


class Rectangulo(Cuadrilatero):
    def __init__(self, nombre, lados, tipo, largo, alto):
        super().__init__(nombre, lados, tipo)
        self.__largo = largo
        self.__alto = alto

    @property
    def largo(self):
        return self.__largo

    @largo.setter
    def largo(self, valor):
        self.__largo = valor

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, valor):
        self.__alto = valor

    # Método area
    def area(self):
        return self.largo * self.alto

    def perimetro(self):
        return 2 * (self.largo + self.alto)

    def listado(self):
        print("Nombre: ", self.nombre)
        print("Lados: ", self.lados)
        print("Tipo: ", self.tipo)
        print("Largo: ", self.largo)
        print("Alto: ", self.alto)
        print("Área: ", self.area())
        print("Perímetro: ", self.perimetro())


def listado_f(obj):
    print("Nombre: ", obj.nombre)
    print("Lados: ", obj.lados)
    print("Tipo: ", obj.tipo)
    print("Largo: ", obj.largo)
    print("Alto: ", obj.alto)
    print("Área: ", obj.area())
    print("Perímetro: ", obj.perimetro())

r = Rectangulo("Rectángulo", 4, "Irregular", 12, 9)
#r.listado()
listado_f(r)
