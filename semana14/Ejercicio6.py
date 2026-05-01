import random


def contar_mayores_50(numeros):
    contador = 0
    for n in numeros:
        if n > 50:
            contador += 1
    return contador


aleatorios = []
for i in range(10):
    aleatorios.append(random.randint(1, 100))

print(f"Números generados: {aleatorios}")
print(f"Mayores a 50: {contar_mayores_50(aleatorios)}")
