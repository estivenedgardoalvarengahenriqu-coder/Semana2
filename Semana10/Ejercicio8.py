##Ejercicio 8: Crear un programa con menú que permita al usuario
##ingresar un texto y elegir una opción (1, 2 o 3).
##El programa debe usar una función para aplicar la transformación seleccionada.


def transformar(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return "Opción inválida"


# Programa principal con menú
print("Programa de Transformación de Texto")
texto = input("Ingresa un texto: ")

print("Opciones:")
print("1 - Mayúsculas")
print("2 - Minúsculas")
print("3 - Primera letra mayúscula")

opcion = int(input("Elige una opción (1, 2 o 3): "))

resultado = transformar(texto, opcion)
print("Resultado:", resultado)
