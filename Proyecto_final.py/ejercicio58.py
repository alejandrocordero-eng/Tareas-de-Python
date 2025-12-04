import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Ejercicio 58")
        
        # Creamos una etiqueta (Label) con texto
        self.label1 = tk.Label(self.ventana1, text="Sistema de Facturación")
        # .grid() ubica el elemento en la ventana (columna 0, fila 0)
        self.label1.grid(column=0, row=0)
        
        self.label2 = tk.Label(self.ventana1, text="2025")
        self.label2.grid(column=0, row=1)
        
        self.ventana1.mainloop()

aplicacion1 = Aplicacion()
