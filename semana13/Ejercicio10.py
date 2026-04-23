# EJERCICIO 10: Suma acumulativa con límite


def ejercicio_10():
    print("\n=== Ejercicio 10: Suma acumulativa con límite ===")
    suma = 0
    validos = []

    while suma <= 100:
        n = int(input(f"Ingresa un número (suma actual: {suma}): "))
        if n < 0:
            print("  Número negativo ignorado.")
        else:
            suma += n
            validos.append(n)

    print(f"\nLa suma superó 100 (suma final: {suma})")
    print("Números válidos ingresados:")
    for num in validos:
        print(f"  {num}")
    print()
