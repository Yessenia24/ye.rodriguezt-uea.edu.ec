import tkinter as tk
from tkinter import messagebox

class ListaTareasApp:
    def __init__(self, root):
        # Configuración de la ventana principal
        self.root = root
        self.root.title("Gestor de Tareas")

        # Campo de entrada para nuevas tareas
        self.entrada_tarea = tk.Entry(root, width=40)
        self.entrada_tarea.pack(pady=10)
        self.entrada_tarea.bind("<Return>", self.añadir_tarea)  # Evento Enter

        # Botones
        self.boton_añadir = tk.Button(root, text="Añadir Tarea", command=self.añadir_tarea)
        self.boton_añadir.pack(pady=5)

        self.boton_completar = tk.Button(root, text="Marcar como Completada", command=self.marcar_completada)
        self.boton_completar.pack(pady=5)

        self.boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.pack(pady=5)

        # Lista de tareas
        self.lista_tareas = tk.Listbox(root, width=50, height=10)
        self.lista_tareas.pack(pady=10)
        self.lista_tareas.bind("<Double-Button-1>", self.marcar_completada)  # Evento doble clic

    def añadir_tarea(self, event=None):
        """Añade una nueva tarea a la lista."""
        tarea = self.entrada_tarea.get().strip()
        if tarea:
            self.lista_tareas.insert(tk.END, tarea)
            self.entrada_tarea.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor, escribe una tarea.")

    def marcar_completada(self, event=None):
        """Marca la tarea seleccionada como completada."""
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            tarea = self.lista_tareas.get(seleccion)
            self.lista_tareas.delete(seleccion)
            self.lista_tareas.insert(tk.END, f"✓ {tarea}")  # Añadir un check visual

    def eliminar_tarea(self):
        """Elimina la tarea seleccionada de la lista."""
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            self.lista_tareas.delete(seleccion)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()
