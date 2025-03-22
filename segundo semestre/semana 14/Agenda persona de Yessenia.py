import tkinter as tk
from tkinter import ttk, messagebox
import datetime

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal de Yessenia")
        self.root.configure(bg="#E6E6FA")  # Color de fondo rosa

        # Estilo para los botones
        style = ttk.Style()
        style.configure("TButton", padding=5, font=('Times New Roman', 12), background="#81D4FA", foreground="black")

        # Frame para la lista de eventos
        self.frame_lista = ttk.Frame(root, padding=10)
        self.frame_lista.pack(pady=10)

        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Frame para la entrada de datos
        self.frame_entrada = ttk.Frame(root, padding=10)
        self.frame_entrada.pack(pady=10)

        ttk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0)
        self.fecha_entry = ttk.Entry(self.frame_entrada)
        self.fecha_entry.grid(row=0, column=1)

        ttk.Label(self.frame_entrada, text="Hora:").grid(row=1, column=0)
        self.hora_entry = ttk.Entry(self.frame_entrada)
        self.hora_entry.grid(row=1, column=1)

        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0)
        self.descripcion_entry = ttk.Entry(self.frame_entrada)
        self.descripcion_entry.grid(row=2, column=1)

        # Frame para los botones
        self.frame_botones = ttk.Frame(root, padding=10)
        self.frame_botones.pack(pady=10)

        ttk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0, padx=5)
        ttk.Button(self.frame_botones, text="Eliminar Evento", command=self.eliminar_evento).grid(row=0, column=1, padx=5)
        ttk.Button(self.frame_botones, text="Salir", command=root.quit).grid(row=0, column=2, padx=5)

        self.eventos = []

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        try:
            datetime.datetime.strptime(fecha, "%Y-%m-%d")
            datetime.datetime.strptime(hora, "%H:%M")
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha u hora incorrecto (YYYY-MM-DD HH:MM)")
            return

        self.eventos.append({"fecha": fecha, "hora": hora, "descripcion": descripcion})
        self.actualizar_lista()
        self.limpiar_entradas()

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showerror("Error", "Selecciona un evento para eliminar.")
            return

        if messagebox.askyesno("Confirmar", "¿Seguro que quieres eliminar este evento?"):
            item = seleccion[0]
            indice = self.tree.index(item)
            del self.eventos[indice]
            self.tree.delete(item)

    def actualizar_lista(self):
        self.tree.delete(*self.tree.get_children())
        for evento in self.eventos:
            self.tree.insert("", tk.END, values=(evento["fecha"], evento["hora"], evento["descripcion"]))

    def limpiar_entradas(self):
        self.fecha_entry.delete(0, tk.END)
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
