# EJERCICIO 7: Promedio de notas


def ejercicio_7():
    print("\n=== Ejercicio 7: Promedio de notas ===")
    notas_validas = []

    while True:
        nota = float(input("Ingresa una nota (−1 para terminar): "))
        if nota == -1:
            break
        if nota < 0 or nota > 10:
            print("  Nota inválida, se ignora.")
        else:
            notas_validas.append(nota)

    if notas_validas:
        suma = 0
        for nota in notas_validas:
            suma += nota
        promedio = suma / len(notas_validas)
        print(f"\nNotas válidas ingresadas: {notas_validas}")
        print(f"Promedio: {promedio:.2f}\n")
    else:
        print("No se ingresaron notas válidas.\n")
