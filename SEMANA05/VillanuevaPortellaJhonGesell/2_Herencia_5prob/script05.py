class Cuenta:
    def __init__(self, titular, saldo=0.0):
        self.__titular = titular
        self.__saldo = float(saldo)

    def depositar(self, monto):
        if monto > 0:
            self.__saldo = self.__saldo + float(monto)
            print("depósito:", monto)
        else:
            print("monto inválido")

    def retirar(self, monto):
        if monto <= 0:
            print("monto inválido")
            return
        if monto > self.__saldo:
            print("fondos insuficientes")
            return
        self.__saldo = self.__saldo - float(monto)
        print("retiro:", monto)

    def mostrar(self):
        print("titular:", self.__titular, "| saldo:", self.__saldo)

    # accesores mínimos para que las subclases puedan operar
    def _get_saldo(self):
        return self.__saldo

    def _set_saldo(self, nuevo):
        self.__saldo = float(nuevo)

class CuentaAhorros(Cuenta):
    def __init__(self, titular, saldo=0.0, tasa=0.02):
        super().__init__(titular, saldo)
        self.__tasa = float(tasa)  # interés simple anual simulado

    def aplicar_interes(self):
        interes = self._get_saldo() * self.__tasa
        self._set_saldo(self._get_saldo() + interes)
        print("interés aplicado:", interes)

class CuentaCorriente(Cuenta):
    def __init__(self, titular, saldo=0.0, sobregiro_max=500.0):
        super().__init__(titular, saldo)
        self.__sobregiro_max = float(sobregiro_max)

    def retirar(self, monto):
        if monto <= 0:
            print("monto inválido")
            return
        # permite saldo negativo hasta -sobregiro_max
        if self._get_saldo() - monto < -self.__sobregiro_max:
            print("límite de sobregiro excedido")
            return
        self._set_saldo(self._get_saldo() - monto)
        print("retiro (corriente):", monto)

# Pruebas
ah = CuentaAhorros("María", 1200, 0.05)
cc = CuentaCorriente("Pedro", 200, 300)

ah.mostrar()
ah.depositar(300)
ah.aplicar_interes()
ah.mostrar()

cc.mostrar()
cc.retirar(400)   # queda en -200 (permitido)
cc.retirar(200)   # excede el sobregiro (-400) -> permitido
cc.retirar(200)   # excedería el límite -> rechazado
cc.mostrar()