import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Ejercicio 71: Notebook")

        self.cuaderno1 = ttk.Notebook(self.ventana1)
        
        # Pestaña 1
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Monitor de Red")
        self.label1 = ttk.Label(self.pagina1, text="Aquí iría el monitoreo...")
        self.label1.grid(column=0, row=0, padx=20, pady=20)

        # Pestaña 2
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Firewall")
        self.label2 = ttk.Label(self.pagina2, text="Configuración de reglas...")
        self.label2.grid(column=0, row=0, padx=20, pady=20)

        self.cuaderno1.grid(column=0, row=0)

        self.ventana1.mainloop()

aplicacion1 = Aplicacion()