import tkinter as tk

# Variables para guardar la posición anterior del mouse
last_x, last_y = 0, 0

def obtener_coordenadas(event):
    global last_x, last_y
    # Guardar coordenadas donde se hizo clic
    last_x, last_y = event.x, event.y

def dibujar(event):
    global last_x, last_y
    # Crear una línea desde la última posición hasta la actual
    canvas.create_line((last_x, last_y, event.x, event.y), fill="black", width=2)
    # Actualizar la última posición
    last_x, last_y = event.x, event.y

ventana = tk.Tk()
ventana.title("Ejercicio 5: Dibujar")

# Crear el lienzo (Canvas) con fondo blanco
canvas = tk.Canvas(ventana, bg="white", width=400, height=300)
canvas.pack()

# Vincular eventos del mouse
# <Button-1> es el clic izquierdo (para empezar a dibujar)
canvas.bind("<Button-1>", obtener_coordenadas)
# <B1-Motion> es mover el mouse con el botón presionado
canvas.bind("<B1-Motion>", dibujar)

tk.Label(ventana, text="Mantén presionado el clic para dibujar").pack()

ventana.mainloop()