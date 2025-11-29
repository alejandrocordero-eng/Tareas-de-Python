import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejercicio 1: Bienvenida")
ventana.geometry("300x200")  # Tamaño de la ventana

# Crear el Label (Etiqueta)
mensaje = tk.Label(ventana, text="¡Bienvenido a mi aplicación con Tkinter!", font=("Arial", 12))
mensaje.pack(pady=50)  # pady añade espacio vertical

# Iniciar el bucle de la aplicación
ventana.mainloop()