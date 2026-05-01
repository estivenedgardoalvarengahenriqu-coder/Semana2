def contar_pares_impares(numeros):
    pares = 0
    impares = 0
    for n in numeros:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = contar_pares_impares(lista)
print(f"Pares: {pares}, Impares: {impares}")