numero = int(input("Introduce un número para calcular su factorial: "))

# El factorial de 0 es 1, así que inicializamos en 1
factorial = 1

# Iteramos desde 1 HASTA el número (incluido)
for i in range(1, numero + 1):
    factorial = factorial * i
    # factorial *= i

print(f"El factorial de {numero} es {factorial}")