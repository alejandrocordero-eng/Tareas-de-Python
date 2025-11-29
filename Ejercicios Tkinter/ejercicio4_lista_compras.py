import tkinter as tk

def agregar_item():
    nuevo_elemento = entry_item.get()
    if nuevo_elemento:  # Verificar que no esté vacío
        lista.insert(tk.END, nuevo_elemento) # Insertar al final (END)
        entry_item.delete(0, tk.END)  # Limpiar la entrada

ventana = tk.Tk()
ventana.title("Ejercicio 4: Lista")
ventana.geometry("300x300")

# Entrada para el nuevo elemento
entry_item = tk.Entry(ventana)
entry_item.pack(pady=5)

# Botón para añadir
boton_agregar = tk.Button(ventana, text="Añadir a la lista", command=agregar_item)
boton_agregar.pack(pady=5)

# Listbox (La lista visual)
lista = tk.Listbox(ventana)
lista.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# Agregamos unos elementos de prueba
lista.insert(tk.END, "Manzana")
lista.insert(tk.END, "Pera")

ventana.mainloop()