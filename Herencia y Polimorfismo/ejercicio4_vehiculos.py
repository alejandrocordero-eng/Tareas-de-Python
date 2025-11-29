# Definición de clases
class Vehiculo:
    def mover(self):
        print("Moviéndose...")

class Carro(Vehiculo):
    def mover(self):
        print("El carro avanza por la carretera.")

class Bicicleta(Vehiculo):
    def mover(self):
        print("La bicicleta avanza pedaleando.")

# Probando el código
mi_carro = Carro()
mi_bici = Bicicleta()

print("--- Ejercicio 4 ---")
mi_carro.mover()
mi_bici.mover()