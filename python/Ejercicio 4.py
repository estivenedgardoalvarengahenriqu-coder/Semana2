print("=== EJERCICIO 4 - Validador básico de correo ===\n")

while True:
    correo = input("Ingrese su correo electrónico: ").strip()

    if correo == "":
        print("¡Error! No puede dejar el campo en blanco. Intente de nuevo.\n")
        continue

    # Aquí está la verificación principal
    if "@" in correo:
        print("\n" + "═" * 40)
        print("El correo parece válido ✓")
        print("═" * 40)
    else:
        print("\n" + "═" * 40)
        print("El correo no es válido ✗")
        print("  (falta el símbolo @)")
        print("═" * 40)

    # Preguntamos si quiere validar otro correo
    otro = input("\n¿Desea validar otro correo? (s/n): ").lower()
    if otro != "s":
        print("¡Gracias por usar el validador!")
        break
    print("-" * 40 + "\n")
