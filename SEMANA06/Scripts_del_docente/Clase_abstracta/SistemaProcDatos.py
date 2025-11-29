from abc import ABC, abstractmethod

# Clase abstracta
class ProcesadorDatos(ABC):

    @abstractmethod
    def procesar(self, datos):
        pass

# Clase concreta que implementa una suma de valores positivos
class SumaPositivos(ProcesadorDatos):

    def procesar(self, datos):
        # Filtra solo positivos usando lambda y filter
        positivos = list(filter(lambda x: x > 0, datos))
        suma = sum(positivos)
        print(f"✅ Suma de positivos: {suma}")
        return suma

# Clase concreta que cuenta cuántos elementos son pares
class ContarPares(ProcesadorDatos):

    def procesar(self, datos):
        # Usa lambda con bucle para contar pares
        #pares = [x for x in datos if (lambda n: n % 2 == 0)(x)]
        pares = [x for x in datos if x % 2 == 0]

        print("🔢 Números pares encontrados:")
        for p in pares:
            print(f" - {p}")
        print(f"🔁 Total de pares: {len(pares)}")
        return len(pares)

# Uso
lista_datos = [4, -2, 7, 0, 11, -5, 8]

procesadores = [SumaPositivos(), ContarPares()]

for procesador in procesadores:
    procesador.procesar(lista_datos)
