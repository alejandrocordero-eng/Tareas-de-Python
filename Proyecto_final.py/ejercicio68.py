import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Ejercicio 68: Login")

        self.label1 = tk.Label(self.ventana1, text="Usuario:")
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        self.usuario = tk.StringVar()
        self.entry1 = tk.Entry(self.ventana1, textvariable=self.usuario)
        self.entry1.grid(column=1, row=0, padx=5, pady=5)

        self.label2 = tk.Label(self.ventana1, text="Contraseña:")
        self.label2.grid(column=0, row=1, padx=5, pady=5)
        self.clave = tk.StringVar()
        # Aquí está la magia de seguridad: show="*"
        self.entry2 = tk.Entry(self.ventana1, textvariable=self.clave, show="*")
        self.entry2.grid(column=1, row=1, padx=5, pady=5)

        self.boton1 = tk.Button(self.ventana1, text="Ingresar", command=self.ingresar)
        self.boton1.grid(column=1, row=2, padx=5, pady=5)

        self.ventana1.mainloop()

    def ingresar(self):
        self.ventana1.title(f"Ingresando como: {self.usuario.get()}")

aplicacion1 = Aplicacion()