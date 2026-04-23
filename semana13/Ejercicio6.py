# EJERCICIO 6: Números primos en rango
# ============================================================
def ejercicio_6():
    print("\n=== Ejercicio 6: Números primos en rango ===")
    while True:
        n = int(input("Ingresa un número n (0 para salir): "))
        if n == 0:
            break
        print(f"Números primos del 1 al {n}:")
        for num in range(2, n + 1):
            es_primo = True
            for divisor in range(2, num):
                if num % divisor == 0:
                    es_primo = False
                    break
            if es_primo:
                print(num, end=" ")
        print()
    print("Ejercicio 6 finalizado.\n")
