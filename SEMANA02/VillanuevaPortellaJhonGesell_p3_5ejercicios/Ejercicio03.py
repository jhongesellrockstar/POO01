"""
Diseñe la clase Filmación con los atributos públicos de instancia:
> Código (Tipo entero)
> Título (Tipo cadena)
> Duración en minutos (Tipo entero)
> Precio en soles (Tipo real)
Implemente además:
> Un método que retorne el precio del vídeo en dólares. Considere que: 1 dólar = 3.32 soles.
En otro archivo:
> Declare y cree un objeto de tipo Filmación.
> Ingrese datos fijos.
> Visualice todos sus datos.
"""
class Filmacion:
    def __init__(self, codigo, titulo, duracion_minutos, precio_soles):
        self.codigo = codigo
        self.titulo = titulo
        self.duracion_minutos = duracion_minutos
        self.precio_soles = precio_soles

    def precio_en_dolares(self):
        return self.precio_soles / 3.32

ejecutar = Filmacion(30182, "Inception", 148, 33.20)
print(f"Código: {ejecutar.codigo}")
print(f"Título: {ejecutar.titulo}")
print(f"Duración: {ejecutar.duracion_minutos} minutos")
print(f"Precio en soles: S/ {ejecutar.precio_soles:.2f}")
print(f"Precio en dólares: ${ejecutar.precio_en_dolares():.2f}")
