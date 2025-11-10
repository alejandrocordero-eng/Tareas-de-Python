suma_notas = 0
cantidad_notas = 5

print(f"Introduce {cantidad_notas} notas:")

for i in range(cantidad_notas):
    nota = float(input(f"Nota {i + 1}: "))
    suma_notas += nota

# El promedio se calcula DESPUÉS de terminar el bucle
promedio = suma_notas / cantidad_notas

print(f"La suma total de las notas es: {suma_notas}")
print(f"El promedio final es: {promedio:.2f}")