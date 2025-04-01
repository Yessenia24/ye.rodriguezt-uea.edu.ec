import tkinter as tk
from tkinter import messagebox

class ListaTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.tareas = []
        self.tareas_completadas = []
        self.seleccionado = None

        # Campo de entrada para nuevas tareas
        self.entry_tarea = tk.Entry(self.root, width=40)
        self.entry_tarea.pack(pady=10)

        # Botones para acciones
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()
        self.button_add = tk.Button(self.button_frame, text="Añadir", command=self.añadir_tarea)
        self.button_add.pack(side=tk.LEFT)
        self.button_completar = tk.Button(self.button_frame, text="Completar", command=self.completar_tarea)
        self.button_completar.pack(side=tk.LEFT)
        self.button_eliminar = tk.Button(self.button_frame, text="Eliminar", command=self.eliminar_tarea)
        self.button_eliminar.pack(side=tk.LEFT)

        # Lista de tareas
        self.lista_tareas = tk.Listbox(self.root, width=40)
        self.lista_tareas.pack(pady=10)

        # Atajos de teclado
        self.root.bind("<Return>", self.añadir_tarea_atajo)
        self.root.bind("c", self.completar_tarea_atajo)
        self.root.bind("d", self.eliminar_tarea_atajo)
        self.root.bind("<Delete>", self.eliminar_tarea_atajo)
        self.root.bind("<Escape>", self.cerrar_aplicacion)

    def añadir_tarea(self):
        tarea = self.entry_tarea.get()
        if tarea:
            self.tareas.append(tarea)
            self.lista_tareas.insert(tk.END, tarea)
            self.entry_tarea.delete(0, tk.END)

    def añadir_tarea_atajo(self, event):
        self.añadir_tarea()

    def completar_tarea(self):
        try:
            self.seleccionado = self.lista_tareas.curselection()[0]
            tarea = self.tareas.pop(self.seleccionado)
            self.tareas_completadas.append(tarea)
            self.lista_tareas.delete(self.seleccionado)
            self.lista_tareas.insert(tk.END, f"[Completada] {tarea}")
        except IndexError:
            messagebox.showwarning("Error", "Debes seleccionar una tarea")

    def completar_tarea_atajo(self, event):
        self.completar_tarea()

    def eliminar_tarea(self):
        try:
            self.seleccionado = self.lista_tareas.curselection()[0]
            tarea = self.lista_tareas.get(self.seleccionado)
            if tarea.startswith("[Completada]"):
                self.tareas_completadas.remove(tarea[11:])
            else:
                self.tareas.pop(self.seleccionado)
            self.lista_tareas.delete(self.seleccionado)
        except IndexError:
            messagebox.showwarning("Error", "Debes seleccionar una tarea")

    def eliminar_tarea_atajo(self, event):
        self.eliminar_tarea()

    def cerrar_aplicacion(self, event):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareas(root)
    root.mainloop()
