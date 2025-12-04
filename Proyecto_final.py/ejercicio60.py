import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.valor = 1
        self.ventana1 = tk.Tk()
        self.ventana1.title("Ejercicio 60")
        
        self.label1 = tk.Label(self.ventana1, text=self.valor)
        self.label1.grid(column=0, row=0)
        
        self.label1.configure(foreground="red") # Texto rojo

        self.boton1 = tk.Button(self.ventana1, text="Incrementar", command=self.incrementar)
        self.boton1.grid(column=0, row=1)

        self.ventana1.mainloop()

    def incrementar(self):
        self.valor = self.valor + 1
        self.label1.configure(text=self.valor)

aplicacion1 = Aplicacion()