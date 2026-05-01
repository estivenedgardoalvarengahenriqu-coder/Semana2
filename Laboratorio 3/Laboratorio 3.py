# Laboratorio 3 - Calculadora avanzada: while menú, select case operaciones, if validar división, for historial

historial = []


def mostrar_menu():
    print("\n" + "=" * 40)
    print("       CALCULADORA AVANZADA")
    print("=" * 40)
    print("  1. Sumar")
    print("  2. Restar")
    print("  3. Multiplicar")
    print("  4. Dividir")
    print("  5. Ver historial")
    print("  6. Salir")
    print("=" * 40)


def mostrar_historial():
    print("\n--- HISTORIAL DE OPERACIONES ---")
    if len(historial) == 0:
        print("  No hay operaciones registradas.")
    else:
        for i, registro in enumerate(historial, 1):
            print(f"  {i}. {registro}")
    print("--------------------------------")


def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("  ⚠ Error: Ingresa un número válido.")


# Bucle principal con while
while True:
    mostrar_menu()
    opcion = input("  Selecciona una opción: ").strip()

    # Select case con match
    match opcion:
        case "1":
            a = obtener_numero("  Ingresa el primer número: ")
            b = obtener_numero("  Ingresa el segundo número: ")
            resultado = a + b
            operacion = f"{a} + {b} = {resultado}"
            historial.append(operacion)
            print(f"\n  ✔ Resultado: {operacion}")

        case "2":
            a = obtener_numero("  Ingresa el primer número: ")
            b = obtener_numero("  Ingresa el segundo número: ")
            resultado = a - b
            operacion = f"{a} - {b} = {resultado}"
            historial.append(operacion)
            print(f"\n  ✔ Resultado: {operacion}")

        case "3":
            a = obtener_numero("  Ingresa el primer número: ")
            b = obtener_numero("  Ingresa el segundo número: ")
            resultado = a * b
            operacion = f"{a} × {b} = {resultado}"
            historial.append(operacion)
            print(f"\n  ✔ Resultado: {operacion}")

        case "4":
            a = obtener_numero("  Ingresa el primer número: ")
            b = obtener_numero("  Ingresa el segundo número: ")
            # Validación de división con if
            if b == 0:
                print("\n  ✘ Error: No se puede dividir entre cero.")
            else:
                resultado = a / b
                operacion = f"{a} ÷ {b} = {resultado:.4f}"
                historial.append(operacion)
                print(f"\n  ✔ Resultado: {operacion}")

        case "5":
            mostrar_historial()

        case "6":
            print("\n  ¡Hasta luego! 👋")
            # Mostrar historial final con for al salir
            if len(historial) > 0:
                print("\n--- Resumen final de operaciones ---")
                for i, registro in enumerate(historial, 1):
                    print(f"  {i}. {registro}")
            break

        case _:
            print("\n  ⚠ Opción no válida. Intenta de nuevo.")
