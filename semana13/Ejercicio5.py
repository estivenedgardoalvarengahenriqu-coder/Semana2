# EJERCICIO 5: Validación de contraseña
# ============================================================
def ejercicio_5():
    print("\n=== Ejercicio 5: Validación de contraseña ===")
    contrasena_correcta = "python123"
    intentos_fallidos = []
    intentos = 0

    while True:
        intento = input("Ingresa la contraseña: ")
        if intento == contrasena_correcta:
            print("¡Contraseña correcta! Acceso concedido.")
            break
        else:
            intentos += 1
            intentos_fallidos.append(intento)
            print("Contraseña incorrecta. Intenta de nuevo.")

    print(f"\nIntentos fallidos ({len(intentos_fallidos)}):")
    for i in range(len(intentos_fallidos)):
        print(f"  Intento {i + 1}: '{intentos_fallidos[i]}'")
    print()
