# Supongamos que tenemos 3 ciudades, 7 días de la semana, y 2 semanas.
# Cada celda contendrá la temperatura de la ciudad en un día específico de una semana específica.

# Ejemplo de matriz 3D con datos ficticios de temperaturas
temperaturas = [
    [  # Ciudad 1
        [23, 25, 22, 24, 26, 27, 25],  # Semana 1
        [24, 26, 23, 25, 27, 28, 26]  # Semana 2
    ],
    [  # Ciudad 2
        [18, 20, 19, 21, 22, 23, 21],  # Semana 1
        [19, 21, 20, 22, 23, 24, 22]  # Semana 2
    ],
    [  # Ciudad 3
        [30, 32, 31, 33, 34, 35, 33],  # Semana 1
        [31, 33, 32, 34, 35, 36, 34]  # Semana 2
    ]
]

# Número de ciudades, semanas y días
num_ciudades = len(temperaturas)
num_semanas = len(temperaturas[0])
num_dias = len(temperaturas[0][0])

# Calcular y mostrar el promedio de temperaturas por ciudad y semana
for ciudad in range(num_ciudades):
    for semana in range(num_semanas):
        suma_temperaturas = 0
        for dia in range(num_dias):
            suma_temperaturas += temperaturas[ciudad][semana][dia]

        promedio = suma_temperaturas / num_dias
        print(f"Promedio de temperaturas para la Ciudad {ciudad + 1} en la Semana {semana + 1}: {promedio:.2f}°C")
