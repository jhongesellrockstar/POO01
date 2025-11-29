"""
Diseñe la clase Expositor con los atributos públicos de instancia:
> Código (Tipo entero)
> Nombre (Tipo cadena)
> Horas trabajadas (Tipo entero)
> Tarifa por hora (Tipo real)
Implemente además:
> Un método que retorne el sueldo bruto (horas * tarifa).
> Un método que retorne el descuento por AFP (10% del sueldo bruto).
> Un método que retorne el descuento por EPS (5% del sueldo bruto).
> Un método que retorne el sueldo neto (sueldo bruto - descuentoAFP - descuentoEPS).
En otro archivo:
> Declare y cree un objeto de tipo Expositor.
> Ingrese datos fijos.
> Visualice todos sus datos.
"""
class Expositor:
    def __init__(self, codigo, nombre, horas_trabajadas, tarifa_por_hora):
        self.codigo = codigo
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def sueldo_bruto(self):
        return self.horas_trabajadas * self.tarifa_por_hora

    def descuento_afp(self):
        return self.sueldo_bruto() * 0.10

    def descuento_eps(self):
        return self.sueldo_bruto() * 0.05

    def sueldo_neto(self):
        return self.sueldo_bruto() - self.descuento_afp() - self.descuento_eps()

ejecutar = Expositor(30182, "Jhon Gesell Villanueva Portella", 160, 70.0)
print(f"Código: {ejecutar.codigo}")
print(f"Nombre: {ejecutar.nombre}")
print(f"Horas trabajadas: {ejecutar.horas_trabajadas} horas")
print(f"Tarifa por hora: S/ {ejecutar.tarifa_por_hora:.2f}")
print(f"Sueldo bruto: S/ {ejecutar.sueldo_bruto():.2f}")
print(f"Descuento AFP: S/ {ejecutar.descuento_afp():.2f}")
print(f"Descuento EPS: S/ {ejecutar.descuento_eps():.2f}")
print(f"Sueldo neto: S/ {ejecutar.sueldo_neto():.2f}")
