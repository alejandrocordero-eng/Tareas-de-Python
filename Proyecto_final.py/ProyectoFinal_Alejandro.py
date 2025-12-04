import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import scrolledtext as st  # <--- Agregamos esto para el reporte
import mysql.connector

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Mantenimiento de Artículos") 
        
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        self.carga_articulos()
        self.consulta_por_codigo()
        self.listado_completo()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def carga_articulos(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de artículos")
        
        ttk.Label(self.pagina1, text="Descripción del artículo:").grid(column=0, row=0, padx=4, pady=4)
        self.descripcion_carga = tk.StringVar()
        ttk.Entry(self.pagina1, textvariable=self.descripcion_carga).grid(column=1, row=0, padx=4, pady=4)

        ttk.Label(self.pagina1, text="Precio:").grid(column=0, row=1, padx=4, pady=4)
        self.precio_carga = tk.StringVar()
        ttk.Entry(self.pagina1, textvariable=self.precio_carga).grid(column=1, row=1, padx=4, pady=4)

        ttk.Button(self.pagina1, text="Confirmar", command=self.agregar).grid(column=1, row=2, padx=4, pady=4)

    def agregar(self):
        try:
            datos = (self.descripcion_carga.get(), self.precio_carga.get())
            conexion = mysql.connector.connect(host="localhost", user="root", password="", database="bd1")
            cursor = conexion.cursor()
            sql = "INSERT INTO articulos (descripcion, precio) VALUES (%s, %s)"
            cursor.execute(sql, datos)
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Información", "Los datos fueron cargados")
            self.descripcion_carga.set("")
            self.precio_carga.set("")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error de conexión: {err}")

    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código")

        ttk.Label(self.pagina2, text="Código:").grid(column=0, row=0, padx=4, pady=4)
        self.codigo_consulta = tk.StringVar()
        ttk.Entry(self.pagina2, textvariable=self.codigo_consulta).grid(column=1, row=0, padx=4, pady=4)
        
        ttk.Button(self.pagina2, text="Consultar", command=self.consultar).grid(column=1, row=1, padx=4, pady=4)
        
        self.label_descripcion = ttk.Label(self.pagina2, text="Descripción:")
        self.label_descripcion.grid(column=0, row=2, padx=4, pady=4, columnspan=2, sticky="w")
        self.label_precio = ttk.Label(self.pagina2, text="Precio:")
        self.label_precio.grid(column=0, row=3, padx=4, pady=4, columnspan=2, sticky="w")

    def consultar(self):
        try:
            datos = (self.codigo_consulta.get(), )
            conexion = mysql.connector.connect(host="localhost", user="root", password="", database="bd1")
            cursor = conexion.cursor()
            cursor.execute("SELECT descripcion, precio FROM articulos WHERE codigo=%s", datos)
            resultado = cursor.fetchall()
            if len(resultado) > 0:
                self.label_descripcion.configure(text=f"Descripción: {resultado[0][0]}")
                self.label_precio.configure(text=f"Precio: {resultado[0][1]}")
            else:
                messagebox.showinfo("Información", "No existe un artículo con dicho código")
            conexion.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error de conexión: {err}")

    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        self.boton_listar = ttk.Button(self.pagina3, text="Ver lista completa", command=self.listar)
        self.boton_listar.grid(column=0, row=0, padx=10, pady=10)
        # Usamos ScrolledText para que si hay muchos articulos, aparezca la barra
        self.scrolledtext1 = st.ScrolledText(self.pagina3, width=50, height=10)
        self.scrolledtext1.grid(column=0, row=1, padx=10, pady=10)

    def listar(self):
        try:
            conexion = mysql.connector.connect(host="localhost", user="root", password="", database="bd1")
            cursor = conexion.cursor()
            cursor.execute("SELECT codigo, descripcion, precio FROM articulos")
            resultado = cursor.fetchall()
            self.scrolledtext1.delete(1.0, tk.END)
            for fila in resultado:
                self.scrolledtext1.insert(tk.END, f"Código: {fila[0]}\nDescripción: {fila[1]}\nPrecio: {fila[2]}\n{'-'*50}\n")
            conexion.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error de conexión: {err}")

# BLOQUE PRINCIPAL PARA EJECUTAR LA APP
if __name__ == "__main__":
    aplicacion1 = Aplicacion()