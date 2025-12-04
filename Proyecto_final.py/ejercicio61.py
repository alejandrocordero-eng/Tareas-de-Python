import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Ejercicio 61")
        
        # Etiqueta y caja para el primer número
        self.label1 = tk.Label(self.ventana1, text="Ingrese primer valor:")
        self.label1.grid(column=0, row=0)
        self.dato1 = tk.StringVar()
        self.entry1 = tk.Entry(self.ventana1, width=10, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)
        
        # Etiqueta y caja para el segundo número
        self.label2 = tk.Label(self.ventana1, text="Ingrese segundo valor:")
        self.label2.grid(column=0, row=1)
        self.dato2 = tk.StringVar()
        self.entry2 = tk.Entry(self.ventana1, width=10, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1)
        
        # Botón para sumar
        self.boton1 = tk.Button(self.ventana1, text="Sumar", command=self.sumar)
        self.boton1.grid(column=1, row=2)
        
        # Etiqueta para el resultado
        self.label3 = tk.Label(self.ventana1, text="Resultado")
        self.label3.grid(column=1, row=3)
        
        self.ventana1.mainloop()

    def sumar(self):
        # Convertimos el texto a entero para poder sumar
        v1 = int(self.dato1.get())
        v2 = int(self.dato2.get())
        suma = v1 + v2
        self.label3.configure(text=f"Resultado: {suma}")

aplicacion1 = Aplicacion()