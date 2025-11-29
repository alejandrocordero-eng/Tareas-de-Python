# Definición de clases
class Animal:
    def hablar(self):
        pass # Método vacío

class Perro(Animal):
    def hablar(self):
        return "¡Guau guau!"

class Gato(Animal):
    def hablar(self):
        return "¡Miau miau!"

# Probando el código
perro = Perro()
gato = Gato()

print("--- Ejercicio 1 ---")
print(f"El perro dice: {perro.hablar()}")
print(f"El gato dice: {gato.hablar()}")