## Ejercicio 2: Crear una función que reciba una palabra y un número, y muestre el resultado en pantalla aplicando la transformación correspondiente (1, 2 o 3).


def transformar(palabra, n):
    if n == 1:
        resultado = palabra.upper()
    elif n == 2:
        resultado = palabra.lower()
    elif n == 3:
        resultado = palabra.capitalize()
    else:
        resultado = "Error"

    print(resultado)


# Ejemplos
transformar("hola", 1)  # HOLA
transformar("MUNDO", 2)  # mundo
transformar("python", 3)  # Python
