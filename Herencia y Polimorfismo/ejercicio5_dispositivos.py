# Definición de clases
class Dispositivo:
    def encender(self):
        print("Dispositivo encendido.")

class Laptop(Dispositivo):
    def encender(self):
        print("Cargando sistema operativo... Laptop lista.")

class Telefono(Dispositivo):
    def encender(self):
        print("Encendiendo pantalla táctil... Teléfono listo.")

# Probando el código
laptop = Laptop()
celular = Telefono()

print("--- Ejercicio 5 ---")
laptop.encender()
celular.encender()