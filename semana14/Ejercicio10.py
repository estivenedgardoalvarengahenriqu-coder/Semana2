def ordenar_numeros(numeros):
    n = len(numeros)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numeros[j] > numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
    return numeros


numeros = []
for i in range(6):
    n = int(input(f"Ingrese número {i+1}: "))
    numeros.append(n)

ordenados = ordenar_numeros(numeros)
print(f"Ordenados: {ordenados}")
