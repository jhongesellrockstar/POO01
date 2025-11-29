from Producto import Producto


class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes
        self.__productos = list(productos)

    def agregar_producto(self, producto):
        self.__productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self.__productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ''
        for producto in self.__productos:
            productos_str += producto.__str__() + '|'

        return f'Orden: {self.__id_orden}, \nProductos: {productos_str}'

if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.00)
    producto2 = Producto('Pantalón', 150.00)
    productos1 = [producto1, producto2]
    orden1 = Orden(productos1)
    print(orden1)
    orden2 = Orden(productos1)
    print(orden2)
    
    print('---------------\n')
    print(producto1.__str__())
