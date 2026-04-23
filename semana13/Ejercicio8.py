# EJERCICIO 8: Patrón de asteriscos (filas impares)


def ejercicio_8():
    print("\n=== Ejercicio 8: Patrón de asteriscos ===")
    while True:
        n = int(input("Ingresa un número (0 para salir): "))
        if n == 0:
            break
        print(f"Triángulo de asteriscos (solo filas impares) hasta {n}:")
        for i in range(1, n + 1):
            if i % 2 != 0:
                print("* " * i)
    print("Ejercicio 8 finalizado.\n")
