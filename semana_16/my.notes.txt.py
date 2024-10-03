# Escritura en el archivo my_notes.txt
# Abrimos el archivo en modo escritura ('w') para crear un nuevo archivo o sobrescribir si ya existe
with open("my_notes.txt", "w") as file:
    # Escribimos tres líneas de notas personales en el archivo
    file.write("Hoy aprendí sobre la lectura y escritura de archivos en Python.\n")
    file.write("Practicar programación regularmente es importante.\n")
    file.write("Me siento motivado para seguir aprendiendo.\n")

# Lectura del archivo my_notes.txt
# Abrimos el archivo en modo lectura ('r') para leer su contenido
with open("my_notes.txt", "r") as file:
    # Leemos el archivo línea por línea utilizando readline() en un bucle
    line = file.readline()
    while line:  # Mientras haya líneas que leer
        print(line.strip())  # Mostramos la línea sin saltos adicionales
        line = file.readline()  # Leemos la siguiente línea
