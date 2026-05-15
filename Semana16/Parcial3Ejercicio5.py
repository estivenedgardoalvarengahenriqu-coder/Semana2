# Ejercicio 5: Transformación de Nombres por Normativa de Privacidad
# Para proteger la identidad, invertimos el orden del nombre y formateamos cada letra

# Le pedimos al usuario su nombre completo
nombre_completo = input("Ingrese su nombre completo (Nombre Apellido): ")

# Separamos el nombre en una lista y lo invertimos para que el apellido quede primero
partes = nombre_completo.split()
invertido = partes[::-1]

print("\nNombre transformado:")

# Recorremos cada palabra de la lista invertida (apellido primero, luego nombre)
for palabra in invertido:
    resultado = ""

    # Recorremos letra por letra para armar el formato con puntos
    for letra in palabra:
        resultado += letra + "."

    # Quitamos el punto final que sobra y mostramos la palabra formateada
    print(resultado[:-1])
