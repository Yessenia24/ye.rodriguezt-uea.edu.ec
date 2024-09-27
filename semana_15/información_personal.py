#Crear el diccionario inicial
informacion_personal = {
    "nombre": "Fernanda Torres",
    "edad": 32,
    "ciudad": "EL chaco",
    "profesion": "Ingeniera"
}

#Acceder al valor de "ciudad" y modificarlo
informacion_personal["ciudad"] = "Quito"

#Actualizar la clave de la profesión
informacion_personal["profesion"] = "Doctora"

#Verificar si la clave "telefono" existe y agregarla si no está
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "2329-100"

#Eliminar la clave "edad"
informacion_personal.pop("edad")

# Imprimir cada clave y valor usando iteración
print("Diccionario final:")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")