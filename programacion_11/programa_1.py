#Crear una matriz bidimensional (3*3)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Busqueda de un valor especifico en la matriz
valor_buscado = 8
if any(valor_buscado in fila for fila in matriz):
    print(f"Se encontro {valor_buscado} en la matriz.")
else:
    print(f"{valor_buscado} no se encontro en la matriz.")