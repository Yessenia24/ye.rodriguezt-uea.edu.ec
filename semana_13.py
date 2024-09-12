def calcular_temperatura_promedio(matriz_temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad durante un período de tiempo basado en una matriz 3D.
    Args:
    matriz_temperaturas (list): Una lista 3D donde cada elemento es una lista de semanas,
                                y cada semana es una lista de diccionarios con las temperaturas diarias.
    Returns:
    dict: Un diccionario con la temperatura promedio de cada ciudad.
    """
    promedios = {}
    # Iterar sobre cada ciudad en la matriz
    for i, ciudad in enumerate(matriz_temperaturas):
        total_temperatura = 0
        num_dias = 0

        # Iterar sobre cada semana en la ciudad
        for semana in ciudad:
            # Iterar sobre cada día en la semana
            for dia in semana:
                total_temperatura += dia["temp"]
                num_dias += 1

        # Calcular el promedio de la ciudad
        if num_dias > 0:
            promedio = total_temperatura / num_dias
        else:
            promedio = 0

        # Almacenar el promedio en el diccionario
        promedios[f"Ciudad {i + 1}"] = promedio

    return promedios
    # Definición de la Función calcular_temperatura_promedio:


# La función toma una lista 3D matriz_temperaturas, que representa las temperaturas diarias para múltiples ciudades a lo largo de varias semanas.
# Se inicializa un diccionario promedios para almacenar el promedio de temperatura de cada ciudad.

# Datos de ejemplo
# Utilizamos enumerate para iterar sobre cada ciudad en la matriz. i representa el índice de la ciudad, y ciudad es la lista de semanas para esa ciudad.
# #Para cada ciudad, se inicializan total_temperatura y num_dias en 0.
# Iteramos sobre las semanas y luego sobre los días de cada semana, acumulando la temperatura total y el conteo de días.
# Calcular y mostrar los promedios
temperaturas = [
    [  # Ciudad 1
        [  # Semana 1
            {"day": "Lunes", "temp": 65},
            {"day": "Martes", "temp": 67},
            {"day": "Miércoles", "temp": 70},
            {"day": "Jueves", "temp": 68},
            {"day": "Viernes", "temp": 72},
            {"day": "Sábado", "temp": 75},
            {"day": "Domingo", "temp": 78}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 66},
            {"day": "Martes", "temp": 68},
            {"day": "Miércoles", "temp": 71},
            {"day": "Jueves", "temp": 69},
            {"day": "Viernes", "temp": 73},
            {"day": "Sábado", "temp": 76},
            {"day": "Domingo", "temp": 79}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 64},
            {"day": "Martes", "temp": 66},
            {"day": "Miércoles", "temp": 69},
            {"day": "Jueves", "temp": 67},
            {"day": "Viernes", "temp": 71},
            {"day": "Sábado", "temp": 74},
            {"day": "Domingo", "temp": 77}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 63},
            {"day": "Martes", "temp": 65},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 66},
            {"day": "Viernes", "temp": 70},
            {"day": "Sábado", "temp": 73},
            {"day": "Domingo", "temp": 76}
        ]
    ],
    [  # Ciudad 2
        [  # Semana 1
            {"day": "Lunes", "temp": 55},
            {"day": "Martes", "temp": 57},
            {"day": "Miércoles", "temp": 60},
            {"day": "Jueves", "temp": 58},
            {"day": "Viernes", "temp": 62},
            {"day": "Sábado", "temp": 65},
            {"day": "Domingo", "temp": 68}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 56},
            {"day": "Martes", "temp": 58},
            {"day": "Miércoles", "temp": 61},
            {"day": "Jueves", "temp": 59},
            {"day": "Viernes", "temp": 63},
            {"day": "Sábado", "temp": 66},
            {"day": "Domingo", "temp": 69}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 54},
            {"day": "Martes", "temp": 56},
            {"day": "Miércoles", "temp": 59},
            {"day": "Jueves", "temp": 57},
            {"day": "Viernes", "temp": 61},
            {"day": "Sábado", "temp": 64},
            {"day": "Domingo", "temp": 67}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 53},
            {"day": "Martes", "temp": 55},
            {"day": "Miércoles", "temp": 58},
            {"day": "Jueves", "temp": 56},
            {"day": "Viernes", "temp": 60},
            {"day": "Sábado", "temp": 63},
            {"day": "Domingo", "temp": 66}
        ]
    ],
    [  # Ciudad 3
        [  # Semana 1
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 77},
            {"day": "Miércoles", "temp": 80},
            {"day": "Jueves", "temp": 78},
            {"day": "Viernes", "temp": 82},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 88}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 76},
            {"day": "Martes", "temp": 78},
            {"day": "Miércoles", "temp": 81},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 83},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 89}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 74},
            {"day": "Martes", "temp": 76},
            {"day": "Miércoles", "temp": 79},
            {"day": "Jueves", "temp": 77},
            {"day": "Viernes", "temp": 81},
            {"day": "Sábado", "temp": 84},
            {"day": "Domingo", "temp": 87}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 73},
            {"day": "Martes", "temp": 75},
            {"day": "Miércoles", "temp": 78},
            {"day": "Jueves", "temp": 76},
            {"day": "Viernes", "temp": 80},
            {"day": "Sábado", "temp": 83},
            {"day": "Domingo", "temp": 86}
        ]
    ]
]

promedios = calcular_temperatura_promedio(temperaturas)
print(promedios)

# Después de acumular las temperaturas, calculamos el promedio dividiendo la temperatura total por el número de días.
# Si num_dias es mayor que 0, calculamos el promedio; de lo contrario, asignamos un promedio de 0.
# Definimos los datos de ejemplo y llamamos a la función calcular_temperatura_promedio para obtener y mostrar los promedios de cada ciudad