import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Ejercicio 64: Listbox")

        self.listbox1 = tk.Listbox(self.ventana1)
        self.listbox1.grid(column=0, row=0)
        
        # Llenamos la lista
        self.listbox1.insert(0, "Papas")
        self.listbox1.insert(1, "Manzanas")
        self.listbox1.insert(2, "Peras")
        self.listbox1.insert(3, "Sandía")

        self.boton1 = tk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
        self.boton1.grid(column=0, row=1)

        self.label1 = tk.Label(self.ventana1, text="Seleccionado:")
        self.label1.grid(column=0, row=2)

        self.ventana1.mainloop()

    def recuperar(self):
        # curselection devuelve una tupla con los índices seleccionados
        if len(self.listbox1.curselection()) != 0:
            item = self.listbox1.get(self.listbox1.curselection()[0])
            self.label1.configure(text=f"Seleccionado: {item}")

aplicacion1 = Aplicacion()