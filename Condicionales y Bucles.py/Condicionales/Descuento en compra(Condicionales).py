monto = float(input("Introduce el monto de la compra: "))

if monto > 500:
    descuento = monto * 0.10  # Calcula el 10%
    monto_final = monto - descuento
    print(f"Tienes un descuento de {descuento:.2f}")
    print(f"El total a pagar es: {monto_final:.2f}")
else:
    print("No aplica descuento.")
    print(f"El total a pagar es: {monto:.2f}")