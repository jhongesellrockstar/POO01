class Persona:
    def __init__(self, nom, ape):
        self.nombre=nom
        self.apellido=ape
        
    def __str__(self):
      return f'{self.nombre} , {self.apellido}'

persona1=Persona('Jose', 'Rodriguez')
print(persona1) 
