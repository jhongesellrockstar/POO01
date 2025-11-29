"""
Diseñe la clase Equipo con los atributos públicos:
> Código (tipo entero)
> Marca (Tipo cadena)
> Color (Tipo cadena)
> Precio en dolares (Tipo real)
Implemente, además:
> Un método que retorne el precio del equipo en soles. Considere que: 1 dólar = 3.32 soles.
> Un método que retorne el precio del equipo en euros. Considere que: 1 euro = 1.16 dolares.
En la clase principal, a la pulsación del bogtón procesar:
> Declare y cree un objeto de tipo equipo.
> Ingrese datos fijos.
> Visualice todos sus usuarios.
"""
class Equipo:
    def __init__(self, codigo, marca, color, precio_dolares):
        self.codigo = codigo
        self.marca = marca
        self.color = color
        self.precio_dolares = precio_dolares

    def precio_en_soles(self):
        return self.precio_dolares * 3.32

    def precio_en_euros(self):
        return self.precio_dolares / 1.16
    
ejecutar = Equipo(30182, "Nvidia", "Negro", 1000.00)
print(f"Código: {ejecutar.codigo}")
print(f"Marca: {ejecutar.marca}")
print(f"Color: {ejecutar.color}")
print(f"Precio en dólares: ${ejecutar.precio_dolares:.2f}")
print(f"Precio en soles: S/ {ejecutar.precio_en_soles():.2f}")
print(f"Precio en euros: € {ejecutar.precio_en_euros():.2f}")
