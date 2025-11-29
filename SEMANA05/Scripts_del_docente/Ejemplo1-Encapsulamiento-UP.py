class Persona:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def mostrar_detalle(self):
        print(f'Persona: {self.__nombre} {self.apellido} {self.edad}')

persona1 = Persona('Juan', 'Perez', 28)
persona1.__nombre = 'Juan Carlos'
persona1.mostrar_detalle()



