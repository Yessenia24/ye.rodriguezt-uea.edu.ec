import json

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id] = {
            "nombre": producto.nombre,
            "cantidad": producto.cantidad,
            "precio": producto.precio
        }

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
        else:
            print("El producto no existe en el inventario.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad:
                self.productos[id]["cantidad"] = cantidad
            if precio:
                self.productos[id]["precio"] = precio
        else:
            print("El producto no existe en el inventario.")

    def buscar_producto(self, nombre):
        resultados = [producto for producto in self.productos.values() if producto["nombre"].lower() == nombre.lower()]
        return resultados

    def mostrar_productos(self):
        for id, producto in self.productos.items():
            print(f"ID: {id}, Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")

    def guardar_inventario(self, archivo="inventario.json"):
        with open(archivo, "w") as file:
            json.dump(self.productos, file)

    def cargar_inventario(self, archivo="inventario.json"):
        try:
            with open(archivo, "r") as file:
                self.productos = json.load(file)
        except FileNotFoundError:
            print("No se encontró el archivo de inventario.")
