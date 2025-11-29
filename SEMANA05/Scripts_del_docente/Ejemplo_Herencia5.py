class Automovil:
    def __init__(self,marca,modelo,precio):
        self.marca=marca
        self.modelo=modelo
        self.precio=precio
        self.disponible=True
        
    def venta(self):
        if self.disponible:
            self.disponible=False
            return f'El vehiculo {self.marca} {self.modelo} ha sido vendido'
        else:
            return f'El vehiculo {self.marca} {self.modelo} no esta disponible'
        
    def check_disponible(self):
        return self.disponible
    
    def get_precio(self):
        return self.precio

    def star_engine(self):
        raise NotImplementedError('Este metodo debe ser implementado en la subclase')
    
    def stop_engine(self):
        raise NotImplementedError('Este metodo debe ser implementado en la subclase')
    
class Carro(Automovil):
    def star_engine(self):
        if self.disponible:
            return f'El motor del auto {self.marca} esta en marcha'
        else:
            return f'El auto {self.marca} no esta disponible'    
        
    def stop_engine(self):
        if self.disponible:
            return f'El auto {self.marca} esta detenido'
        else:
            return f'El auto {self.marca} no esta disponible'
        
class bicicleta(Automovil):
    def star_engine(self):
        if self.disponible:
            return f'La Bicicleta {self.marca} esta en marcha'
        else:
            return f'La bicicleta {self.marca} no esta disponible'    
        
    def stop_engine(self):
        if self.disponible:
            return f'La Bicicleta {self.marca} esta detenida'
        else:
            return f'La Bicicleta {self.marca} no esta disponible'
        
class Camion(Automovil):
    def star_engine(self):
        if self.disponible:
            return f'El motor del camion {self.marca} esta en marcha'
        else:
            return f'El camion {self.marca} no esta disponible'    
        
    def stop_engine(self):
        if self.disponible:
            return f'El camion {self.marca} esta detenido'
        else:
            return f'El camion {self.marca} no esta disponible'
        
class Usuario:
    def __init__(self,nombre):
        self.nombre=nombre
        self.autoComprado=[]
        
    def comprarAuto(self,vehiculo:Automovil):
        if vehiculo.check_disponible():
            vehiculo.venta()
            self.autoComprado.append(vehiculo)
        else:
            print(f'el auto {vehiculo.marca} no esta disponible')
            
    def consultaAuto(self,vehiculo:Automovil):
        if vehiculo.check_disponible():
            availability='Disponible'
        else:
           availability='No disponible'
        print(f'El auto {vehiculo.narca}, esta {availability} y su costo es de {vehiculo.get_precio()}')
            
class Dealer:
    def __init__(self):
        self.inventory=[]
        self.clientes=[]
        
    def add_auto(self,vehiculo:Automovil):
        self.inventory.append(vehiculo)
        print(f'El vehiculo {vehiculo.marca}, modelo {vehiculo.modelo} ha sido añadido')
            
    def usariosRegistrados(self,cliente:Usuario):
        self.clientes.append(cliente)
        print(f' El cliente {cliente.nombre} ha sido añadido')
        
    def mostrar_vehiculos(self):
        print('Vehiculos en el Inventario')
        for vehiculo in self.inventory:
            if vehiculo.check_disponible():
                print(f'Vehiculo {vehiculo.marca} por {vehiculo.get_precio()}')
    
        
car1=Carro('BMW','Sedan',70000)
bike1=bicicleta('Monark','Montañera',5000)
camion1=Camion('Volvo','FH16', 150000)

user1=Usuario('Jaime')

dealer1=Dealer()
dealer1.add_auto(car1)
dealer1.add_auto(bike1)
dealer1.add_auto(camion1)
dealer1.mostrar_vehiculos()

user1.comprarAuto(car1)
dealer1.mostrar_vehiculos()


            
    