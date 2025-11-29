"""
Diseñe la clase Coordinador con los atributos públicos de instancia:
> Código (Tipo entero)
> Nombre (Tipo cadena)
> Categoria (Tipo entero)
> Número de celular (int).
Implemente, además:
> Un método que retorne el sueldo del coordinador sabiendo que:
{Caterogía , Sueldo}
{0 , S/. 7500.00}
{1 , S/. 5850.00}
{2 , S/. 4500.00}
En otro archivo:
> Declare y cree un objeto de tipo Coordinador.
> Ingrese datos fijos.
> Visualice todos sus datos.
"""

class Coordinador:
    def __init__(self, codigo, nombre, categoria, numero_celular):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.numero_celular = numero_celular

    def sueldo(self):
        if self.categoria == 0:
            return 7500.00
        elif self.categoria == 1:
            return 5850.00
        elif self.categoria == 2:
            return 4500.00
        else:
            return 0.00  # Categoría no válida

ejecutar = Coordinador(30182, "Jhon Gesell Villanueva Portella", 0, 952354282)
print(f"Código: {ejecutar.codigo}") 
print(f"Nombre: {ejecutar.nombre}")
print(f"Categoría: {ejecutar.categoria}")   
print(f"Número de celular: {ejecutar.numero_celular}")
print(f"Sueldo: S/ {ejecutar.sueldo():.2f}")

