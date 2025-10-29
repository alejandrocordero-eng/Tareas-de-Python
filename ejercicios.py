# Ejercicio 1: Tuplas
vulnerabilidades = ('SQL Injection', 'Cross-Site Scripting', 'Buffer Overflow', 'Denegación de Servicio')

print("--- Ejercicio 1: Tuplas ---")
print(f"a) Segundo elemento: {vulnerabilidades[1]}")
print(f"b) Dos últimos elementos: {vulnerabilidades[2:]}")

try:
    print("c) Intentando modificar el primer elemento (comentado para evitar error):")
    print("Las tuplas son inmutables, por lo que no se pueden modificar sus elementos después de su creación.")
except TypeError as e:
    print(f"c) Error al intentar modificar un elemento: {e}")


# Ejercicio 2: Listas
print("\n--- Ejercicio 2: Listas ---")
puertos_abiertos = [22, 80, 443, 8080]
print(f"Lista inicial: {puertos_abiertos}")

puertos_abiertos.append(21)
print(f"a) Lista después de agregar 21: {puertos_abiertos}")

puertos_abiertos.remove(8080)
print(f"b) Lista después de eliminar 8080: {puertos_abiertos}")

puertos_abiertos.sort()
print(f"c) Lista ordenada: {puertos_abiertos}")


# Ejercicio 3: Diccionarios
print("\n--- Ejercicio 3: Diccionarios ---")
dispositivo_red = {
    'IP': '192.168.1.10',
    'Hostname': 'Firewall-Corp',
    'Estado': 'Activo'
}
print(f"Diccionario inicial: {dispositivo_red}")

print(f"a) Valor de 'Hostname': {dispositivo_red['Hostname']}")

dispositivo_red['Ubicación'] = 'Centro de Datos'
print(f"b) Diccionario después de agregar 'Ubicación': {dispositivo_red}")

dispositivo_red['Estado'] = 'Inactivo'
print(f"c) Diccionario después de cambiar 'Estado': {dispositivo_red}")

print(f"d) Diccionario actualizado completo: {dispositivo_red}")