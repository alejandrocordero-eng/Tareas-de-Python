suma = 0

while True:
    numero = int(input("Introduce un número (escribe 0 para terminar): "))
    
    if numero == 0:
        break  # Rompe (sale) del bucle
    
    suma = suma + numero  # Acumula el número
    # suma += numero

print(f"La suma total es: {suma}")