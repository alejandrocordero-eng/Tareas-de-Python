import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Ejercicio 62: Radiobuttons")

        # Entradas de números
        self.label1 = tk.Label(self.ventana1, text="Valor 1:")
        self.label1.grid(column=0, row=0)
        self.dato1 = tk.StringVar()
        self.entry1 = tk.Entry(self.ventana1, width=10, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)

        self.label2 = tk.Label(self.ventana1, text="Valor 2:")
        self.label2.grid(column=0, row=1)
        self.dato2 = tk.StringVar()
        self.entry2 = tk.Entry(self.ventana1, width=10, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1)

        # Variable para guardar la selección (1=Sumar, 2=Restar)
        self.seleccion = tk.IntVar()
        self.seleccion.set(1) # Valor por defecto

        # Creamos los Radiobuttons
        self.radio1 = tk.Radiobutton(self.ventana1, text="Sumar", variable=self.seleccion, value=1)
        self.radio1.grid(column=1, row=2)
        
        self.radio2 = tk.Radiobutton(self.ventana1, text="Restar", variable=self.seleccion, value=2)
        self.radio2.grid(column=1, row=3)

        self.boton1 = tk.Button(self.ventana1, text="Operar", command=self.operar)
        self.boton1.grid(column=1, row=4)

        self.label_resultado = tk.Label(self.ventana1, text="Resultado")
        self.label_resultado.grid(column=1, row=5)

        self.ventana1.mainloop()

    def operar(self):
        v1 = int(self.dato1.get())
        v2 = int(self.dato2.get())
        
        # Lógica según el Radiobutton seleccionado
        if self.seleccion.get() == 1:
            suma = v1 + v2
            self.label_resultado.configure(text=f"Suma: {suma}")
        else:
            resta = v1 - v2
            self.label_resultado.configure(text=f"Resta: {resta}")

aplicacion1 = Aplicacion()