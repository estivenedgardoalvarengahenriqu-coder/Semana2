##Ejercicio 4: Crear una función que reciba una lista de palabras y un número. La función debe transformar cada palabra de la lista según la opción seleccionada (1, 2 o 3).


def transformar_lista(lista, n):
    resultado = []

    for palabra in lista:
        if n == 1:
            resultado.append(palabra.upper())
        elif n == 2:
            resultado.append(palabra.lower())
        elif n == 3:
            resultado.append(palabra.capitalize())
        else:
            return "Error"

    return resultado


# Ejemplo
palabras = ["hola", "MUNDO", "python"]
print(transformar_lista(palabras, 3))
