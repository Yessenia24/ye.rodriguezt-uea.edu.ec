# inventario.py

class Inventario:
    def _init_(self):
        self.productos = {}  # Diccionario para almacenar los productos

    def agregar_producto(self, producto):
        self.productos[producto.id_producto] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]

    def actualizar_producto(self, producto):
        if producto.id_producto in self.productos:
            self.productos[producto.id_producto] = producto

    def buscar_producto(self, id_producto):
        return self.productos.get(id_producto)

    def mostrar_inventario(self):
        for producto in self.productos.values():
            print(producto)