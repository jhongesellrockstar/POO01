class Operaciones:
    def __init__(self):
        self.valor1 = int(input("Ingrese primer valor: "))
        self.valor2 = int(input("Ingrese segundo valor: "))
        self.sumar(); self.restar(); self.multiplicar(); self.dividir()

    def sumar(self):        print("La suma es:", self.valor1 + self.valor2)
    def restar(self):       print("La resta es:", self.valor1 - self.valor2)
    def multiplicar(self):  print("El producto es:", self.valor1 * self.valor2)
    def dividir(self):
        if self.valor2 == 0: print("La división no es posible (divisor 0).")
        else:                print("La división es:", self.valor1 / self.valor2)

Operacion1 = Operaciones()
