import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Ejercicio 66: Menú")
        self.ventana1.geometry("300x200")

        # Crear la barra de menú
        menubar = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar)

        # Crear el primer menú "Opciones"
        opciones1 = tk.Menu(menubar, tearoff=0)
        opciones1.add_command(label="Cambiar dimensión", command=self.fijar_tamano)
        opciones1.add_separator()
        opciones1.add_command(label="Salir", command=self.ventana1.destroy)

        # Añadir "Opciones" a la barra principal
        menubar.add_cascade(label="Opciones", menu=opciones1)

        self.ventana1.mainloop()

    def fijar_tamano(self):
        self.ventana1.geometry("500x300")

aplicacion1 = Aplicacion()