# script07.py
from abc import ABC, abstractmethod
import random

class MetodoPago(ABC):
    def __init__(self, monto, numero_transaccion):
        self.monto = float(monto)
        self.numero_transaccion = numero_transaccion

    def validar_monto(self):
        if self.monto <= 0:
            raise ValueError("El monto debe ser positivo")

    @abstractmethod
    def pagar(self): ...

class TarjetaCredito(MetodoPago):
    def __init__(self, monto, numero_transaccion, numero_tarjeta):
        super().__init__(monto, numero_transaccion)
        self.numero_tarjeta = numero_tarjeta

    def pagar(self):
        self.validar_monto()
        print(f"Cobrando {self.monto:.2f} a la tarjeta ****{self.numero_tarjeta[-4:]} ... OK")

class PayPal(MetodoPago):
    def __init__(self, monto, numero_transaccion, email):
        super().__init__(monto, numero_transaccion)
        self.email = email

    def pagar(self):
        self.validar_monto()
        print(f"Transferencia PayPal a {self.email} por {self.monto:.2f} ... OK")

class Bitcoin(MetodoPago):
    def pagar(self):
        self.validar_monto()
        hash_tx = hex(random.getrandbits(64))[2:]
        print(f"Pago BTC {self.monto:.8f} BTC | tx={hash_tx}")

TarjetaCredito(120.5, "T-001", "4111111111111111").pagar()
PayPal(75, "P-002", "user@example.com").pagar()
Bitcoin(0.0042, "B-003").pagar()
