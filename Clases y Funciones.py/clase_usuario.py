class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"Usuario: {self.nombre}, Edad: {self.edad}")

# Ejemplo de uso:
usuario1 = Usuario("Carlos", 25)
usuario1.mostrar_datos()