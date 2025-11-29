class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self.__id_producto = Producto.contador_productos
        self.__nombre = nombre
        self.__precio = precio


    @property
    def id_producto(self):
        return self.__id_producto

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    def __str__(self):
        return f'Id Producto: {self.id_producto}, Nombre: {self.nombre}, Precio: {self.precio}'

if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.00)
    print(producto1)
    producto2 = Producto('Pantalón', 150.00)
    print(producto2)
    print('---------------\n')
    print(producto1.__str__())