class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Utiliza una tupla para almacenar el autor y el título, ya que estos no cambiarán.
        self.informacion = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.informacion[0]}, Autor: {self.informacion[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Lista para almacenar los libros actualmente prestados.
        self.libros_prestados = []

    def __str__(self):
        return f"Nombre: {self.nombre}, ID: {self.id_usuario}"


class Biblioteca:
    def __init__(self):
        # Diccionario para almacenar los libros disponibles, con el ISBN como clave.
        self.libros_disponibles = {}
        # Conjunto para asegurar IDs de usuario únicos.
        self.usuarios_registrados = set()
        # Diccionario para almacenar usuarios registrados por ID.
        self.usuarios_dict = {}

    def registrar_usuario(self, nombre, id_usuario):
        if id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados.add(id_usuario)
            self.usuarios_dict[id_usuario] = Usuario(nombre, id_usuario)
            print(f"Usuario {nombre} registrado con éxito.")
        else:
            print("ID de usuario ya existe.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            self.usuarios_registrados.remove(id_usuario)
            del self.usuarios_dict[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print("ID de usuario no encontrado.")

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro {libro.informacion[0]} agregado con éxito.")
        else:
            print("ISBN ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} quitado con éxito.")
        else:
            print("ISBN no encontrado en la biblioteca.")

    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros_disponibles and id_usuario in self.usuarios_registrados:
            libro = self.libros_disponibles[isbn]
            usuario = self.usuarios_dict[id_usuario]
            usuario.libros_prestados.append(libro)
            print(f"Libro {libro.informacion[0]} prestado a {usuario.nombre}.")
        else:
            print("ISBN o ID de usuario no válido.")

    def devolver_libro(self, isbn, id_usuario):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_dict[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    print(f"Libro {libro.informacion[0]} devuelto por {usuario.nombre}.")
                    return
            print("Libro no encontrado entre los prestados.")
        else:
            print("ID de usuario no válido.")

    def buscar_libros(self, criterio, valor):
        resultados = []
        if criterio == "titulo":
            for libro in self.libros_disponibles.values():
                if valor.lower() in libro.informacion[0].lower():
                    resultados.append(libro)
        elif criterio == "autor":
            for libro in self.libros_disponibles.values():
                if valor.lower() in libro.informacion[1].lower():
                    resultados.append(libro)
        elif criterio == "categoria":
            for libro in self.libros_disponibles.values():
                if valor.lower() in libro.categoria.lower():
                    resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_dict[id_usuario]
            return usuario.libros_prestados
        else:
            print("ID de usuario no válido.")
            return []


# Pruebas del sistema
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Registrar usuarios
    biblioteca.registrar_usuario("Yessenia Rodriguez", "U001")
    biblioteca.registrar_usuario("Gabriela Torres", "U002")

    # Agregar libros
    libro1 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", "Fantasía", "978-0-395-19395-8")
    libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Literatura", "978-0-06-088328-7")
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    # Prestar libros
    biblioteca.prestar_libro("978-0-395-19395-8", "U001")
    biblioteca.prestar_libro("978-0-06-088328-7", "U002")

    # Listar libros prestados
    print("\nLibros prestados a Yessenia Rodriguez:")
    for libro in biblioteca.listar_libros_prestados("U001"):
        print(libro)

    # Buscar libros
    print("\nBuscar libros por autor 'Tolkien':")
    resultados = biblioteca.buscar_libros("autor", "Tolkien")
    for libro in resultados:
        print(libro)

    # Devolver libros
    biblioteca.devolver_libro("978-0-395-19395-8", "U001")

    # Listar libros prestados después de devolución
    print("\nLibros prestados a Gabriela Torres después de devolución:")
    for libro in biblioteca.listar_libros_prestados("U001"):
        print(libro)
