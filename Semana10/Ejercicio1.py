##Ejercicio 1:  Crear una función que reciba un texto y un número


def transformar_texto(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return "Opción no válida"


# Ejemplos de uso
print(transformar_texto("hola mundo", 1))  # HOLA MUNDO
print(transformar_texto("HOLA MUNDO", 2))  # hola mundo
print(transformar_texto("hola mundo", 3))  # Hola mundo
