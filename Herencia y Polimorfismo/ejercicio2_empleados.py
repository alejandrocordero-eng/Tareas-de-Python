# Definición de clases
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_bono(self):
        pass

class Gerente(Empleado):
    def calcular_bono(self):
        # Bono del 20%
        return self.salario * 0.20

class Tecnico(Empleado):
    def calcular_bono(self):
        # Bono del 10%
        return self.salario * 0.10

# Probando el código
gerente = Gerente("Maria", 5000)
tecnico = Tecnico("Juan", 3000)

print("--- Ejercicio 2 ---")
print(f"Bono del Gerente {gerente.nombre}: ${gerente.calcular_bono()}")
print(f"Bono del Técnico {tecnico.nombre}: ${tecnico.calcular_bono()}")