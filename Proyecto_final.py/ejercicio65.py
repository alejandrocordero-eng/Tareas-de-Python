import tkinter as tk
from tkinter import ttk # Importante para Combobox

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Ejercicio 65: Combobox")

        self.label1 = tk.Label(self.ventana1, text="Seleccione un día:")
        self.label1.grid(column=0, row=0)

        self.dato = tk.StringVar()
        self.combobox1 = ttk.Combobox(self.ventana1, width=10, textvariable=self.dato)
        self.combobox1.grid(column=0, row=1)
        
        # Definimos los valores de la lista
        self.combobox1['values'] = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")
        self.combobox1.current(0) # Selecciona el primero por defecto

        self.boton1 = tk.Button(self.ventana1, text="Ver", command=self.recuperar)
        self.boton1.grid(column=0, row=2)

        self.label2 = tk.Label(self.ventana1, text="Día seleccionado:")
        self.label2.grid(column=0, row=3)

        self.ventana1.mainloop()

    def recuperar(self):
        self.label2.configure(text=f"Día seleccionado: {self.dato.get()}")

aplicacion1 = Aplicacion()