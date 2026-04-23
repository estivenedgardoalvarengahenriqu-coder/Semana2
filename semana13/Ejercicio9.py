import random

# EJERCICIO 9: Juego de adivinar número


def ejercicio_9():
    print("\n=== Ejercicio 9: Juego de adivinar número ===")
    secreto = random.randint(1, 100)
    intentos = []

    print("He pensado un número entre 1 y 100. ¡Adivínalo!")

    while True:
        intento = int(input("Tu intento: "))
        intentos.append(intento)
        if intento == secreto:
            print(f"¡Correcto! El número era {secreto}.")
            break
        elif intento < secreto:
            print("  Demasiado bajo. Intenta con un número mayor.")
        else:
            print("  Demasiado alto. Intenta con un número menor.")

    print(f"\nTus intentos ({len(intentos)}):")
    for i in range(len(intentos)):
        print(f"  Intento {i + 1}: {intentos[i]}")
    print()
