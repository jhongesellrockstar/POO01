class Persona:
	def __init__ (self):
		self.nombre=input('Ingrese el nombre:')
		self.edad=int(input('Ingrese la edad:'))

	def imprimir(self):
		print('Nombre:',self.nombre)
		print('Edad:', self.edad)

class Empleado (Persona):
	def __init__(self):
		super().__init__()
		self.sueldo=float(input('Ingrese Sueldo:'))
		
	def imprimir(self):
		super().imprimir()
		print('Sueldo:', self.sueldo)

	def paga_impuestos(self):
		if self.sueldo>3000:
			print(self.nombre, 'debe pagar impuesto')
		else:
			print(self.nombre, 'no paga impuesto')
   
#Bloque Principal

empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()
