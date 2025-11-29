import tkinter as tk

def sumar():
    try:
        # Convertimos el texto a números flotantes para permitir decimales
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Por favor, ingresa números válidos")

ventana = tk.Tk()
ventana.title("Ejercicio 3: Sumadora")
ventana.geometry("300x250")

tk.Label(ventana, text="Número 1:").pack()
entry_num1 = tk.Entry(ventana)
entry_num1.pack()

tk.Label(ventana, text="Número 2:").pack()
entry_num2 = tk.Entry(ventana)
entry_num2.pack()

boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=10)

label_resultado = tk.Label(ventana, text="Resultado: ")
label_resultado.pack()

ventana.mainloop()