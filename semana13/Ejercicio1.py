# EJERCICIO 1: Números pares en rango


def ejercicio_1():
    print("\n=== Ejercicio 1: Números pares en rango ===")
    while True:
        n = int(input("Ingresa un número (0 para salir): "))
        if n == 0:
            break
        print(f"Números pares del 1 al {n}:")
        for i in range(1, n + 1):
            if i % 2 == 0:
                print(i, end=" ")
        print()
    print("Ejercicio 1 finalizado.\n")
