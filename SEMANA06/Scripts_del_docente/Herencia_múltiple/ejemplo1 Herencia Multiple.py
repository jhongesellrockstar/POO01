class FiguraGeometrica:
    def __init__(self,ancho,alto):
        self.ancho=ancho
        self.alto=alto
        
class Color:
    def __init__(self,color):
        self.color=color
        
class Cuadrado(FiguraGeometrica,Color):
    def __init__(self,lado,color):
        FiguraGeometrica.__init__(self,lado,lado)
        Color.__init__(self,color)
        
    def calcular_area(self):
        return self.ancho*self.alto

print('Creacion del objeto Cuadrado'.center(50,'-'))
cuadrado1=Cuadrado(5,"rojo")
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)
print(f'Calculo del area del cuadrado: {cuadrado1.calcular_area()}')
print(Cuadrado.mro())     