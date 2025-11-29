# Problema05
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f'lista: {self.nombre}, edad: {self.edad}'
        
    def __eq__(self, otra):
        self.otra = otra
        return self.edad == otra
    
    def __gt__(self, otra):
        return self.edad > otra.edad
    
    def __lt__(self, otra):
        return self.edad < otra.edad
    

persona1 = Persona('Juan', 25)
persona2 = Persona('Maria', 30)
print(persona1)
print(persona2)
print(persona1 == persona2)
print(persona1 > persona2)
print(persona1 < persona2) 

