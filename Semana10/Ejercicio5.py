##Ejercicio 5: Crear una función que reciba un texto y un número. Si el número no es 1, 2 o 3, debe mostrar un mensaje de “opción inválida”


def transformar(texto, n):
    if n == 1:
        return texto.upper()
    elif n == 2:
        return texto.lower()
    elif n == 3:
        return texto.capitalize()
    else:
        return "Opción inválida"


# Ejemplo
print(transformar("hola mundo", 4))
