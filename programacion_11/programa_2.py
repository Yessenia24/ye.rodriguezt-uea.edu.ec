#Crear una matriz bidimensional (3*3)
matriz=[
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]
#valor que estamos buscando
valor_buscado= 7

#Inicializar variables para rastraer la posicion del valor
fila_encontrada= -2
columna_encontrada= -2

#recorrer la matriz para buscar el valor
for fila in range (len (matriz)):
    for columna in range (len(matriz[fila])):
        if matriz[fila][columna]== valor_buscado:
            fila_encontrada = fila
            columna_encontrada = columna
        break
    #salir del bucle exterior si se encuentra el valor

# verificar si se encontro el valor mostrar la posicion

if fila_encontrada != -1:
    print(f"se encontro{valor_buscado} en la fila {fila_encontrada} y columna {columna_encontrada}")

else:
    print (f"{valor_buscado} no se encontro en la matriz.")