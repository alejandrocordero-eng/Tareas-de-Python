import tkinter as tk
from tkinter import messagebox

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Ejercicio 67: Messagebox")

        self.boton1 = tk.Button(self.ventana1, text="Mostrar Info", command=self.mostrar_info)
        self.boton1.grid(column=0, row=0, padx=10, pady=10)

        self.boton2 = tk.Button(self.ventana1, text="Mostrar Error", command=self.mostrar_error)
        self.boton2.grid(column=1, row=0, padx=10, pady=10)

        self.ventana1.mainloop()

    def mostrar_info(self):
        messagebox.showinfo("Información", "Operación exitosa")

    def mostrar_error(self):
        messagebox.showerror("Error Crítico", "Fallo en la conexión al servidor")

aplicacion1 = Aplicacion()