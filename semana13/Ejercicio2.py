# EJERCICIO 2: Contador de positivos y negativos


def ejercicio_2():
    print("\n=== Ejercicio 2: Contador de positivos y negativos ===")
    positivos = 0
    negativos = 0
    resultados = []

    while True:
        n = int(input("Ingresa un número (0 para salir): "))
        if n == 0:
            break
        elif n > 0:
            positivos += 1
            resultados.append(("Positivo", n))
        else:
            negativos += 1
            resultados.append(("Negativo", n))

    print("\n--- Resumen de resultados ---")
    for tipo, valor in resultados:
        print(f"  {valor} → {tipo}")
    print(f"\nTotal positivos: {positivos}")
    print(f"Total negativos: {negativos}\n")
