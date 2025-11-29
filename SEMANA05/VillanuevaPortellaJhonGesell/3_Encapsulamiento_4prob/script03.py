class Poligono:
    def __init__(self, lados):
        # lista protegida (no privada): se sugiere no acceder directo fuera de la clase
        self._lados = list(lados)

    def get_lados(self):
        # devuelve copia para evitar modificar desde afuera
        return list(self._lados)

    def set_lados(self, nuevos):
        self._lados = list(nuevos)

    def area(self):
        # será sobreescrito en subclases
        return 0

class Triangulo(Poligono):
    # asumimos lados = [base, altura]
    def area(self):
        if len(self._lados) < 2:
            print("faltan datos para el triángulo")
            return 0
        base = float(self._lados[0])
        altura = float(self._lados[1])
        return (base * altura) / 2.0

class Rectangulo(Poligono):
    # asumimos lados = [largo, alto]
    def area(self):
        if len(self._lados) < 2:
            print("faltan datos para el rectángulo")
            return 0
        largo = float(self._lados[0])
        alto = float(self._lados[1])
        return largo * alto

# Pruebas
t = Triangulo([10, 6])
r = Rectangulo([12, 5])

print("área triángulo:", t.area())
print("área rectángulo:", r.area())