palabras = ["computadora", "ratón", "pantalla", "teclado", "usb", "cable"]

# Crear diccionario usando comprensión de diccionario
longitudes = {palabra: len(palabra) for palabra in palabras}
print(type(longitudes))

# Mostrar palabras con longitud > 5
print("Palabras con más de 5 letras:")
for palabra, longitud in longitudes.items():
    if longitud > 5:
        print(f"- {palabra} ({longitud} letras)")
