numero_secreto = 7
print("¡Adivina el número secreto (entre 1 y 10)!")

while True:
    intento = int(input("Introduce tu número: "))
    
    if intento == numero_secreto:
        print("¡Felicidades! ¡Adivinaste!")
        break # Salimos del bucle al adivinar
    else:
        print("Incorrecto. Intenta de nuevo.")