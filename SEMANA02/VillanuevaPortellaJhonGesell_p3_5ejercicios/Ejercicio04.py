"""
Diseñe la clase Trabajador con los atributos públicos de instancia:
> Código (Tipo entero)
> Nombre (Tipo cadena)
> horas trabajadas (Tipo entero)
> tarifa horaria (Tipo real)
Implemente además:
> Un método que retorne el sueldo bruto (horas * tarifa).
> Un método que retorne el descuento de acuerdo a la siguiente tabla:
{Sueldo Bruto , Descuento}
{< 4500 , 12% del sueldo bruto}
{>= 4500 y < 6500 , 14% del sueldo bruto}
{>= 6500 , 16% del sueldo bruto}
> Un método que retorne el sueldo neto (sueldo bruto - descuento).
En otro archivo:
> Declare y cree un objeto de tipo Trabajador.
> Ingrese datos fijos.
> Visualice todos sus datos.
"""
class Trabajador:
    def __init__(self, codigo, nombre, horas_trabajadas, tarifa_horaria):
        self.codigo = codigo
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_horaria = tarifa_horaria

    def sueldo_bruto(self):
        return self.horas_trabajadas * self.tarifa_horaria

    def descuento(self):
        sueldo = self.sueldo_bruto()
        if sueldo < 4500:
            return sueldo * 0.12
        elif 4500 <= sueldo < 6500:
            return sueldo * 0.14
        else:
            return sueldo * 0.16

    def sueldo_neto(self):
        return self.sueldo_bruto() - self.descuento()

ejecutar = Trabajador(30182, "Jhon Gesell Villanueva Portella", 160, 70.0)
print(f"Código: {ejecutar.codigo}")
print(f"Nombre: {ejecutar.nombre}")
print(f"Horas trabajadas: {ejecutar.horas_trabajadas} horas")
print(f"Tarifa horaria: S/ {ejecutar.tarifa_horaria:.2f}")
print(f"Sueldo bruto: S/ {ejecutar.sueldo_bruto():.2f}")
print(f"Descuento: S/ {ejecutar.descuento():.2f}")
print(f"Sueldo neto: S/ {ejecutar.sueldo_neto():.2f}")

