def calcular_promedio(notas):
    total = 0
    for nota in notas:
        total += nota
    promedio = total / len(notas)
    return promedio


notas = [7.5, 6.0, 8.2, 5.5, 9.0, 4.8]
promedio = calcular_promedio(notas)
print(f"Promedio: {promedio:.2f}")

if promedio >= 6.0:
    print("El grupo APRUEBA")
else:
    print("El grupo REPRUEBA")
