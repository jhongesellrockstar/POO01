class Cuenta:
    def __init__(self, titular: str, monto: float = 0.0):
        self.titular = titular
        self.monto = float(monto)

    # Métodos comunes
    def depositar(self, importe: float):
        if importe <= 0:
            raise ValueError("El importe a depositar debe ser positivo.")
        self.monto += importe

    def extraer(self, importe: float):
        if importe <= 0:
            raise ValueError("El importe a extraer debe ser positivo.")
        if importe > self.monto:
            raise ValueError("Fondos insuficientes.")
        self.monto -= importe

    def mostrar(self):
        print(f"Titular: {self.titular} | Saldo: {self.monto:.2f} soles")

    # Ganancia por intereses (interfaz): cada subclase define su lógica
    def calcular_interes(self):
        return 0.0

    # Actualiza el saldo aplicando intereses (si corresponde)
    def actualizar_saldo(self):
        interes = self.calcular_interes()
        self.monto += interes
        return interes


class CajaAhorro(Cuenta):
    """No genera intereses."""
    def calcular_interes(self):
        return 0.0


class PlazoFijo(Cuenta):
    """
    Genera intereses simples en el plazo indicado (días), con una tasa anual.
    tasa_anual en decimal (p.ej., 0.12 = 12% anual).
    """
    def __init__(self, titular, monto, dias, tasa_anual):
        super().__init__(titular, monto)
        if dias <= 0:
            raise ValueError("El plazo (días) debe ser positivo.")
        if tasa_anual < 0:
            raise ValueError("La tasa anual no puede ser negativa.")
        self.dias = int(dias)
        self.tasa_anual = float(tasa_anual)

    def calcular_interes(self) -> float:
        # Interés simple proporcional a los días: monto * tasa_anual * (días/365)
        return self.monto * self.tasa_anual * (self.dias / 365.0)

    def mostrar(self):
        super().mostrar()
        print(f"Plazo: {self.dias} días | Tasa anual: {self.tasa_anual*100:.2f}%")

"""
print("=== Objeto de CajaAhorro ===")
ca = CajaAhorro("Ana Pérez", 1500)
ca.depositar(500)
ca.extraer(200)

ca.mostrar()
ganancia_ca = ca.actualizar_saldo()  # 0.0 por definición
print(f"Interés aplicado (CajaAhorro): {ganancia_ca:.2f}\n")
"""



"""
print("=== Objeto de PlazoFijo ===")
pf = PlazoFijo("Luis Gómez", 10000, dias=90, tasa_anual=0.10)  # 10% anual, 90 días
pf.mostrar()
ganancia_pf = pf.actualizar_saldo()
print(f"Interés aplicado (PlazoFijo): {ganancia_pf:.2f}")
pf.mostrar()
"""



print("=== Objeto de CajaAhorro ===")
ca = CajaAhorro("Ana Pérez", 1500)
ca.depositar(500)
ca.extraer(200)

ca.mostrar()
ganancia_ca = ca.actualizar_saldo()  # 0.0 por definición
print(f"Interés aplicado (CajaAhorro): {ganancia_ca:.2f}\n")