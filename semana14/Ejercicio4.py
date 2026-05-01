def encontrar_mayor(numeros):
    mayor = numeros[0]
    for n in numeros:
        if n > mayor:
            mayor = n
    return mayor


numeros = []
for i in range(8):
    n = int(input(f"Ingrese número {i+1}: "))
    numeros.append(n)

mayor = encontrar_mayor(numeros)
print(f"El número mayor es: {mayor}")
