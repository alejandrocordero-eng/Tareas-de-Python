# --- Ejercicio 6: Guardar como lógico (Booleano) ---
# [Extraído de la fuente 11]
print("--- Ejercicio 6 ---")
# Pedimos el número (1 o 0) como entero
respuesta_num = int(input("6. ¿Tienes internet en casa? (1 = Sí, 0 = No): "))
# Convertimos el entero a booleano: bool(1) es True, bool(0) es False
tiene_internet = bool(respuesta_num)
print(f"Valor lógico guardado: {tiene_internet}\n")