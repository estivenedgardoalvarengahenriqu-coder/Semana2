# EJERCICIO 4: Suma de números impares


def ejercicio_4():
    print("\n=== Ejercicio 4: Suma de números impares ===")
    impares = []
    suma = 0

    while True:
        n = int(input("Ingresa un número (0 para salir): "))
        if n == 0:
            break
        if n % 2 != 0:
            suma += n
            impares.append(n)

    print("\nNúmeros impares ingresados:")
    for num in impares:
        print(f"  {num}")
    print(f"Suma total de impares: {suma}\n")
