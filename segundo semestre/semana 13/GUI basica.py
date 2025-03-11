import tkinter as tk  # Importa la librería Tkinter (con alias tk para simplificar)
from tkinter import ttk # Importa themed widgets

# Función para agregar el texto del campo a la lista
def agregar_elemento():
    texto = entrada.get()  # Obtiene el texto del campo de texto
    if texto:  # Verifica que no esté vacío
        lista.insert(tk.END, texto)  # Agrega el texto a la lista
        entrada.delete(0, tk.END)  # Limpia el campo de texto

# Función para limpiar la selección o toda la lista
def limpiar_elemento():
    try:
        seleccion = lista.curselection()[0]  # Obtiene el índice del elemento seleccionado
        lista.delete(seleccion)  # Elimina el elemento seleccionado
    except IndexError:  # Si no hay nada seleccionado
        lista.delete(0, tk.END)  # Elimina todo

# Creación de la ventana principal
ventana = tk.Tk()
ventana.title("Mi Aplicación GUI") # Establece el título de la ventana

# Componentes
etiqueta = tk.Label(ventana, text="Ingrese texto:")  # Crea una etiqueta
etiqueta.pack(pady=5)  # Coloca la etiqueta en la ventana

entrada = tk.Entry(ventana)  # Crea un campo de texto
entrada.pack(pady=5)  # Coloca el campo de texto

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_elemento)  # Crea un botón "Agregar"
boton_agregar.pack(pady=5)  # Coloca el botón

# Crear un Treeview (tabla)
tabla = ttk.Treeview(ventana, columns=("Texto"))
tabla.heading("#0", text="Índice")
tabla.heading("Texto", text="Texto Ingresado")
tabla.pack()

# Función para agregar texto a la tabla
def agregar_a_tabla():
    texto = entrada.get()
    if texto:
        tabla.insert("", tk.END, text=tabla.index(tk.END) + 1, values=(texto,))
        entrada.delete(0, tk.END)

# Función para limpiar la selección de la tabla
def limpiar_tabla():
    seleccion = tabla.selection()
    if seleccion:
        for item in seleccion:
            tabla.delete(item)
    else:
        # Limpiar todos los elementos de la tabla
        for item in tabla.get_children():
            tabla.delete(item)

boton_agregar_tabla = tk.Button(ventana, text="Agregar a Tabla", command=agregar_a_tabla)
boton_agregar_tabla.pack(pady=5)

boton_limpiar_tabla = tk.Button(ventana, text="Limpiar Tabla", command=limpiar_tabla)
boton_limpiar_tabla.pack(pady=5)


boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_elemento)  # Crea un botón "Limpiar"
boton_limpiar.pack(pady=5)  # Coloca el botón

# Iniciar el bucle principal de la GUI
ventana.mainloop()
