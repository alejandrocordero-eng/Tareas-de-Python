numero_tabla = int(input("¿Qué tabla de multiplicar quieres ver? "))

print(f"--- Tabla del {numero_tabla} ---")

# range(1, 11) genera números del 1 hasta ANTES del 11 (o sea, 1 al 10)
for i in range(1, 11):
    resultado = numero_tabla * i
    print(f"{numero_tabla} x {i} = {resultado}")