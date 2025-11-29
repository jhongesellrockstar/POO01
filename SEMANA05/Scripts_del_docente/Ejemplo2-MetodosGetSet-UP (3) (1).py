class Persona:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.apellido = apellido
        self.edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def mostrar_detalle(self):
        print(f'Persona: {self.__nombre} {self.apellido} {self.edad}')

persona1 = Persona('Juan', 'Perez', 28)
persona1.nombre = 'Juan Carlos'
persona1.mostrar_detalle()
