class Coche:
    def __init__(self, marca, velocidad):
        self.marca = marca
        self.velocidad = velocidad

    def aumentar_velocidad(self, aumento):
        self.velocidad += aumento
        print(f"Velocidad actual: {self.velocidad} km/h")

# Ejemplo de uso:
auto = Coche("Toyota", 60)
auto.aumentar_velocidad(20) # Sube a 80 km/h