class CuentaBancaria:
    def __init__(self, titular, balance):
        self.titular = titular
        self.balance = balance

    def depositar(self, cantidad):
        self.balance += cantidad
        print(f"Depositado: {cantidad}. Nuevo balance: {self.balance}")

    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Retirado: {cantidad}. Restante: {self.balance}")
        else:
            print("Fondos insuficientes")

# Ejemplo:
cuenta = CuentaBancaria("Ana", 1000)
cuenta.retirar(200)