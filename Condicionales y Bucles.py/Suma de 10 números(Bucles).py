suma_total = 0
print("Introduce 10 números para sumar:")

# range(10) genera números del 0 al 9 (10 vueltas en total)
for i in range(10):
    numero = float(input(f"Número {i + 1}: "))
    suma_total += numero

print(f"La suma total de los 10 números es: {suma_total}")