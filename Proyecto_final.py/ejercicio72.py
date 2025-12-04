import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Ejercicio 72: Canvas")

        # Crear lienzo negro
        self.canvas1 = tk.Canvas(self.ventana1, width=400, height=300, background="black")
        self.canvas1.grid(column=0, row=0)

        # Dibujar una línea roja (simulando un tráfico de red)
        self.canvas1.create_line(0, 0, 400, 300, fill="red", width=2)
        
        # Dibujar un rectángulo verde (simulando un servidor seguro)
        self.canvas1.create_rectangle(50, 50, 150, 150, fill="green", outline="white")
        
        # Dibujar texto
        self.canvas1.create_text(200, 200, text="SISTEMA SEGURO", fill="white", font="Arial 15")

        self.ventana1.mainloop()

aplicacion1 = Aplicacion()