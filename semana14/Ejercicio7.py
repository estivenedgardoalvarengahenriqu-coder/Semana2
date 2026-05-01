def contar_mayores_edad(edades):
    contador = 0
    for edad in edades:
        if edad >= 18:
            contador += 1
    return contador


edades = [15, 22, 17, 30, 16, 25, 19, 13]
mayores = contar_mayores_edad(edades)
print(f"Personas mayores de edad: {mayores}")
