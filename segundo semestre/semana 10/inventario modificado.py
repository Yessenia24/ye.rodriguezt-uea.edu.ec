import os

class Producto:
    def _init_(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def _str_(self):
        return f"{self.nombre}, {self.cantidad}, {self.precio}"

class Inventario:
    def _init_(self, archivo_inventario="inventario.txt"):
        self.productos = {}
        self.archivo_inventario = archivo_inventario
        self.cargar_inventario()

    def agregar_producto(self, producto):
        if producto.nombre in self.productos:
            print(f"Error: El producto '{producto.nombre}' ya existe en el inventario.")
            return
        self.productos[producto.nombre] = producto
        self.guardar_inventario()
        print(f"Producto '{producto.nombre}' añadido con éxito.")

    def actualizar_producto(self, nombre, cantidad=None, precio=None):
        if nombre not in self.productos:
            print(f"Error: El producto '{nombre}' no existe en el inventario.")
            return
        if cantidad is not None:
            self.productos[nombre].cantidad = cantidad
        if precio is not None:
            self.productos[nombre].precio = precio
        self.guardar_inventario()
        print(f"Producto '{nombre}' actualizado con éxito.")

    def eliminar_producto(self, nombre):
        if nombre not in self.productos:
            print(f"Error: El producto '{nombre}' no existe en el inventario.")
            return
        del self.productos[nombre]
        self.guardar_inventario()
        print(f"Producto '{nombre}' eliminado con éxito.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
            return
        for producto in self.productos.values():
            print(producto)

    def guardar_inventario(self):
        try:
            with open(self.archivo_inventario, "w") as archivo:
                for producto in self.productos.values():
                    archivo.write(f"{producto.nombre},{producto.cantidad},{producto.precio}\n")
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Ocurrió un error al guardar el inventario: {e}")

    def cargar_inventario(self):
        if not os.path.exists(self.archivo_inventario):
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
            return
        try:
            with open(self.archivo_inventario, "r") as archivo:
                for linea in archivo:
                    nombre, cantidad, precio = linea.strip().split(",")
                    self.productos[nombre] = Producto(nombre, int(cantidad), float(precio))
            print("Inventario cargado con éxito.")
        except FileNotFoundError:
            print("Error: Archivo de inventario no encontrado.")
        except ValueError:
            print("Error: El archivo de inventario está corrupto.")
        except Exception as e:
            print(f"Ocurrió un error al cargar el inventario: {e}")

def main():
    inventario = Inventario()
    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == "2":
            nombre = input("Nombre del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            inventario.actualizar_producto(nombre, int(cantidad) if cantidad else None, float(precio) if precio else None)
        elif opcion == "3":
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == "4":
            inventario.mostrar_inventario()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

if _name_ == "_main_":
          main()