class CuentaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.__titular = titular
        self.__saldo = float(saldo)

    # getter / setter SOLO para saldo
    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, nuevo_saldo):
        if float(nuevo_saldo) < 0:
            print("saldo no puede ser negativo")
            return
        self.__saldo = float(nuevo_saldo)

    def mostrar(self):
        print("titular:", self.__titular, "| saldo:", self.__saldo)

    def depositar(self, monto):
        if monto <= 0:
            print("monto inválido")
            return
        self.__saldo = self.__saldo + float(monto)

    def retirar(self, monto):
        if monto <= 0:
            print("monto inválido")
            return
        if monto > self.__saldo:
            print("fondos insuficientes")
            return
        self.__saldo = self.__saldo - float(monto)

    def transferir(self, otra_cuenta, monto):
        if monto <= 0:
            print("monto inválido")
            return
        if monto > self.__saldo:
            print("fondos insuficientes para transferir")
            return
        # debita y acredita
        self.__saldo = self.__saldo - float(monto)
        otra_cuenta.set_saldo(otra_cuenta.get_saldo() + float(monto))

# Pruebas
c1 = CuentaBancaria("María", 1000)
c2 = CuentaBancaria("Pedro", 300)

c1.mostrar()
c2.mostrar()

c1.transferir(c2, 250)
c1.mostrar()
c2.mostrar()

c2.transferir(c1, 100)
c1.mostrar()
c2.mostrar()