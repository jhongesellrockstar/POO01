"""
Dada una lista de palabras, crea un diccionario donde cada clave sea una palabra y su valor sea la longitud de esa palabra.
Luego, muestra solo las palabras cuya longitud sea mayor a 5.
"""
class Palabra:
    def __init__(self, texto):
        self.texto = texto
        self.longitud = len(texto)

    def es_larga(self):
        return self.longitud > 5


palabras = ["manzana", "pera", "banana", "kiwi", "sandía", "cereza", "frambuesa"]
objetos_palabras = [Palabra(p) for p in palabras]


for palabra in objetos_palabras:
    if palabra.es_larga():
        print(f"Palabra: {palabra.texto}, Longitud: {palabra.longitud}")
