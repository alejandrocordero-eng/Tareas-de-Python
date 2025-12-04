import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Ejercicio 59")
        
        self.boton1 = tk.Button(self.ventana1, text="Finalizar", command=self.finalizar)
        self.boton1.grid(column=0, row=0)
        
        self.ventana1.mainloop()

    def finalizar(self):
        # Cierra la ventana
        self.ventana1.destroy()

aplicacion1 = Aplicacion()