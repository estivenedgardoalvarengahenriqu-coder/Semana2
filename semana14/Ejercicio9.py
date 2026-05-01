def suma_pares(numeros):
    total = 0
    for n in numeros:
        if n % 2 == 0:
            total += n
    return total


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = suma_pares(lista)
print(f"Suma de números pares: {resultado}")
