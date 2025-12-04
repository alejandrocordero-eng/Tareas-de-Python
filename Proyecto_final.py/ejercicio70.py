import tkinter as tk
from tkinter import scrolledtext as st

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Ejercicio 70: ScrolledText")

        self.entrada = tk.Entry(self.ventana1, width=20)
        self.entrada.grid(column=0, row=0, padx=10, pady=10)

        self.boton = tk.Button(self.ventana1, text="Agregar al Log", command=self.agregar)
        self.boton.grid(column=1, row=0)

        # Área de texto con barra de desplazamiento automática
        self.scrolledtext1 = st.ScrolledText(self.ventana1, width=30, height=10)
        self.scrolledtext1.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

        self.ventana1.mainloop()

    def agregar(self):
        # Insertar texto al final (tk.END)
        self.scrolledtext1.insert(tk.END, "Log: " + self.entrada.get() + "\n")
        self.entrada.delete(0, tk.END)

aplicacion1 = Aplicacion()