# EJERCICIO 3: Tabla de multiplicar filtrada
# ============================================================
def ejercicio_3():
    print("\n=== Ejercicio 3: Tabla de multiplicar filtrada ===")
    while True:
        n = int(input("Ingresa un número (-1 para salir): "))
        if n == -1:
            break
        print(f"Resultados de la tabla del {n} mayores a 20:")
        for i in range(1, 11):
            resultado = n * i
            if resultado > 20:
                print(f"  {n} x {i} = {resultado}")
    print("Ejercicio 3 finalizado.\n")
