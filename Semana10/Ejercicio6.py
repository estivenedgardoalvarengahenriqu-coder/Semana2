##Ejercicio 6: Crear una función que reciba un texto y un número, transforme el texto según la opción y luego devuelva la cantidad de caracteres del resultado.


def transformar_y_contar(texto, n):
    if n == 1:
        resultado = texto.upper()
    elif n == 2:
        resultado = texto.lower()
    elif n == 3:
        resultado = texto.capitalize()
    else:
        return "Opción inválida"

    return len(resultado)


# Ejemplo
print(transformar_y_contar("hola mundo", 1))
