class Libro:
    def __init__(self,nombreLib,autor):
        self.nombreLib=nombreLib
        self.autor=autor
        self.activo=True
        
    def prestar(self):
        if self.activo:
            self.activo=False
            print(f'El libro {self.nombreLib} ha sido prestado ')
        else:
            print('El libro {self.nombreLib} no esta disponible')
            
    
    def retorno(self):
        self.activo=True
        print(f'El libro {self.nombreLib} ha sido devuelto')
            
            
class Usuario:
    def __init__(self, nombre,codigo ):
        self.nombre=nombre
        self.codigo=codigo
        self.listaLibros=[]
        
    def prestarLibro(self,libro):
        if libro.activo:
            libro.prestar()
            self.listaLibros.append(libro)
        else:
            print(f'El libro {libro.nombreLib} no esta disponible')
            
    def retornoLibro(self,libro):
        if libro in self.listaLibros:
            libro.retorno()
            self.listaLibros.remove(libro)
        else:
            print(f'El libro {libro.nombreLib} no esta en la ista de prestado')
            
class Biblioteca:
    def __init__(self):
        self.libros=[]
        self.usuarios=[]
        
    def addLibro(self,libro):
        self.libros.append(libro)
        print(f'El libro {libro.nombreLib} ha sido agregado')
        
    def registroUser(self,users):
        self.usuarios.append(users)
        print(f'el usuario {users.nombre} ha sido registrado')
        
    def LibrosDisponibles(self):
        print('Libros Disponibles')
        for libro in self.libros:
            if libro.activo:
                print(f'{libro.nombreLib} por {libro.autor}')
                
libro1=Libro('Dracula', 'Bram Stoker')
libro2=Libro('La momia','Jane Webb')

user1=Usuario('Van Helsing','001')

#adicion de libros
bib1=Biblioteca()
bib1.addLibro(libro1)
bib1.addLibro(libro2)
print('*********************************************************')
bib1.registroUser(user1)
print('*********************************************************')
#mostrar libro
bib1.LibrosDisponibles()
print('*********************************************************')
#Realizar prestamo de libro
user1.prestarLibro(libro1)
print('*********************************************************')
#mostrar libro
bib1.LibrosDisponibles()
print('*********************************************************')
#Realizar prestamo de libro
user1.prestarLibro(libro1)
print('*********************************************************')
#mostrar libro
bib1.LibrosDisponibles()
print('*********************************************************')
#Retornar libro
user1.retornoLibro(libro1)
print('*********************************************************')
#mostrar libro
bib1.LibrosDisponibles()
       
    

            
        
        
    
        
        
        
        
    