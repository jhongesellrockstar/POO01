class CuentaCorreo:
    def __init__(self):
        self.idNombre=input('digitae su nombre id :')  # Nombre
        self.idApellido=input('Digite su apellido: ') #Apellido
        self.dominio=input('Digitar Dominio: ') # gmail, hotmail, etc
        self.password=input('Digitar password:' )
        self.ImprimirCuenta()
        self.ValidarPass()
        
    def ImprimirCuenta(self):
            print(f' Su cuenta de correo es: {self.idApellido}.{self.idNombre}@{self.dominio}.com')
        
    def ValidarPass(self):
        cont=1
        while cont<=2:
            cont +=1
            verpass=input('Ingrese nuevamente su contraseña: ')
            if self.password==verpass:
                print('Validacion Exitosa')
                return
            else:
                print(f'Intento {cont-1}')
                print("Error de Password"  )
                
            
          
print('Primera Cuenta')
cuenta1=CuentaCorreo()
print('\n Segunda Cuenta')
cuenta2=CuentaCorreo()