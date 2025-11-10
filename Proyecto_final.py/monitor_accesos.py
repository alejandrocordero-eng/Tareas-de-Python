# --- Sistema de Monitoreo de Accesos ---

# --- COMPONENTES (Vectores y Matrices) ---
#  Vectores para almacenar usuarios y servidores válidos
usuarios_validos = ["admin", "user01", "dev_externo", "db_admin"]
servidores_validos = ["Servidor Web", "Servidor BD", "Servidor FTP"]

#  Matriz para almacenar los registros de intentos
# Cada fila será: [usuario, servidor, ip, tipo_acceso, hora]
intentos_log = [
    ["admin", "Servidor Web", "192.168.0.1", "exitoso", "10:30"],
    ["user01", "Servidor FTP", "192.168.0.5", "exitoso", "10:32"],
    ["hacker", "Servidor BD", "10.0.0.8", "fallido", "10:33"],
    ["admin", "Servidor BD", "192.168.0.1", "exitoso", "10:35"],
    ["dev_externo", "Servidor Web", "200.10.5.2", "fallido", "10:40"]
]

# --- FUNCIONES ---

def RegistrarIntento():
    """
     Pide datos al usuario y los registra en la matriz 'intentos_log'.
    Valida si el usuario y el servidor existen en los vectores.
    """
    print("\n--- Registrar Nuevo Intento de Acceso ---")
    usuario = input("Ingrese el usuario: ")
    servidor = input("Ingrese el servidor (Servidor Web, Servidor BD, Servidor FTP): ")
    ip = input("Ingrese la IP de origen: ")
    tipo_acceso = input("Ingrese el tipo (exitoso / fallido): ")
    hora = input("Ingrese la hora (HH:MM): ")

    #  Condicionales para validación
    if usuario not in usuarios_validos:
        print(f"ALERTA: El usuario '{usuario}' no es un usuario conocido.")
        # Podríamos decidir registrarlo igualmente como un intento anómalo
        # En este caso, lo registraremos pero 'tipo_acceso' será 'fallido'
        tipo_acceso = "fallido"
        
    if servidor not in servidores_validos:
        print(f"ALERTA: Intento de acceso a servidor desconocido: '{servidor}'")
        tipo_acceso = "fallido"

    # Se añade el nuevo intento a la matriz
    nuevo_intento = [usuario, servidor, ip, tipo_acceso, hora]
    intentos_log.append(nuevo_intento)
    
    print(f"Intento registrado con éxito: {nuevo_intento}")
    

def MostrarReporte():
    """
     Muestra todos los registros (la matriz completa) de forma ordenada.
    """
    print("\n--- Reporte Completo de Accesos ---")
    if not intentos_log:
        print("No hay intentos registrados.")
        return

    # Imprimimos una cabecera para la tabla
    print(f"{'Usuario':<15} | {'Servidor':<15} | {'IP Origen':<15} | {'Tipo':<10} | {'Hora':<5}")
    print("-" * 67)

    #  Bucle para recorrer la matriz
    for intento in intentos_log:
        # Desempaquetamos la fila (que es un vector)
        usuario, servidor, ip, tipo, hora = intento
        print(f"{usuario:<15} | {servidor:<15} | {ip:<15} | {tipo:<10} | {hora:<5}")

def GenerarAlertas():
    """
     Analiza la matriz 'intentos_log' y genera alertas 
    basadas en intentos fallidos.
    """
    print("\n--- Generando Alertas de Seguridad ---")
    alertas_encontradas = 0
    
    #  Bucle para analizar la matriz
    for intento in intentos_log:
        # Desempaquetamos el intento
        usuario, servidor, ip, tipo, hora = intento
        
        #  Condicional para detectar amenazas
        if tipo == "fallido":
            print(f"[ALERTA] Intento FALLIDO detectado:")
            print(f"  > Usuario:   {usuario}")
            print(f"  > Servidor:  {servidor}")
            print(f"  > IP Origen: {ip}")
            print(f"  > Hora:      {hora}")
            print("-" * 20)
            alertas_encontradas += 1
            
    if alertas_encontradas == 0:
        print("No se encontraron amenazas en los registros.")

# --- BUCLE PRINCIPAL (Menú de Interacción) ---
def main():
    """
    Función principal que ejecuta el menú del sistema.
    """
    opcion = ""
    #  Bucle principal del programa
    while opcion != "4":
        print("\n==========================================")
        print("   Sistema de Monitoreo de Accesos")
        print("==========================================")
        print("1. Registrar Intento de Acceso")
        print("2. Mostrar Reporte de Todos los Accesos")
        print("3. Generar Alertas de Seguridad")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            RegistrarIntento()
        elif opcion == "2":
            MostrarReporte()
        elif opcion == "3":
            GenerarAlertas()
        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta pronto!")
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# --- Punto de entrada del script ---
# Esto asegura que main() solo se ejecute cuando corres este archivo directamente
if __name__ == "__main__":
    main()