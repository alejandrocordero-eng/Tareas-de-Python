class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

# Ejemplo de uso:
mi_rect = Rectangulo(10, 5)
print(f"El área es: {mi_rect.calcular_area()}")