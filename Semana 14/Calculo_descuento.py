# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Cálculo del monto de descuento
    descuento = (porcentaje_descuento / 100) * monto_total
    # Devolviendo el monto del descuento
    return descuento

# Programa principal

# Llamada 1: Usando solo el monto total con el descuento predeterminado (10%)
monto_total_1 = 700  # Ejemplo de una compra de $600
descuento_1 = calcular_descuento(monto_total_1)
monto_final_1 = monto_total_1 - descuento_1

# Imprimir resultados de la primera llamada
print(f"Compra 1: Monto total = ${monto_total_1}")
print(f"Descuento (10%) = ${descuento_1}")
print(f"Monto final a pagar = ${monto_final_1}")

print()  # Línea en blanco para separar los resultados

# Llamada 2: Proporcionando el monto total y un porcentaje de descuento específico (por ejemplo, 15%)
monto_total_2 = float(input("Ingrese el monto total: ")) # Ejemplo de una compra de $1000
porcentaje_descuento_2 = int(input("Ingrese el procentaje de descuento: "))  # Porcentaje de descuento del 15%
descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
monto_final_2 = monto_total_2 - descuento_2

# Imprimir resultados de la segunda llamada
print(f"Compra 2: Monto total = ${monto_total_2}")
print(f"Descuento ({porcentaje_descuento_2}%) = ${descuento_2}")
print(f"Monto final a pagar = ${monto_final_2}")