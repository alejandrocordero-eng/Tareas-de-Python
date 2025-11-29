class Estudiante:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones # Lista de números

    def calcular_promedio(self):
        if not self.calificaciones:
            return 0
        suma = sum(self.calificaciones)
        cantidad = len(self.calificaciones)
        return suma / cantidad

# Ejemplo:
alumno = Estudiante("Luis", [90, 85, 100])
print(f"Promedio: {alumno.calcular_promedio()}")