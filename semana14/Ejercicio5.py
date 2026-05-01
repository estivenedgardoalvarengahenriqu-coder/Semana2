def solo_positivos(numeros):
    positivos = []
    for n in numeros:
        if n > 0:
            positivos.append(n)
    return positivos


lista = [-3, 5, -1, 0, 8, -7, 2, 4]
resultado = solo_positivos(lista)
print(f"Números positivos: {resultado}")
