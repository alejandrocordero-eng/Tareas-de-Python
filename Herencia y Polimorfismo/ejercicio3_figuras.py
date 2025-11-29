import math

# Definición de clases
class Figura:
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

# Probando el código
circulo = Circulo(5)
cuadrado = Cuadrado(4)

print("--- Ejercicio 3 ---")
# El :.2f sirve para limitar a 2 decimales
print(f"Área del círculo: {circulo.area():.2f}") 
print(f"Área del cuadrado: {cuadrado.area()}")