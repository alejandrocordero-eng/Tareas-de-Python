import tkinter as tk

def mostrar_texto():
    # Obtener el texto del Entry
    texto_ingresado = entrada.get()
    # Actualizar el Label con ese texto
    etiqueta_resultado.config(text=f"Escribiste: {texto_ingresado}")

ventana = tk.Tk()
ventana.title("Ejercicio 2: Entry y Button")
ventana.geometry("300x200")

# Campo de entrada (Entry)
entrada = tk.Entry(ventana)
entrada.pack(pady=10)

# Botón
boton = tk.Button(ventana, text="Mostrar Mensaje", command=mostrar_texto)
boton.pack(pady=5)

# Etiqueta donde se mostrará el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=10)

ventana.mainloop()