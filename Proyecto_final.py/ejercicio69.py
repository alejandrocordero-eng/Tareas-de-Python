import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Ejercicio 69: LabelFrame")

        # Creamos un marco con título
        self.labelframe1 = ttk.LabelFrame(self.ventana1, text="Datos del Servidor")
        self.labelframe1.grid(column=0, row=0, padx=10, pady=10)

        # Metemos cosas DENTRO del labelframe1
        self.label1 = ttk.Label(self.labelframe1, text="IP:")
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.entry1 = ttk.Entry(self.labelframe1)
        self.entry1.grid(column=1, row=0, padx=5, pady=5)

        self.label2 = ttk.Label(self.labelframe1, text="Puerto:")
        self.label2.grid(column=0, row=1, padx=5, pady=5)
        self.entry2 = ttk.Entry(self.labelframe1)
        self.entry2.grid(column=1, row=1, padx=5, pady=5)

        self.ventana1.mainloop()

aplicacion1 = Aplicacion()