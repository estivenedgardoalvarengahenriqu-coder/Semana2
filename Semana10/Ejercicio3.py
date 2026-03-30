##Ejercicio 3: Solicitar al usuario un texto y un número. Enviar esos datos a una función que aplique la transformación según la opción elegida.


def transformar(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return "Opción no válida"


# Solicitar datos al usuario
texto_usuario = input("Escribe un texto: ")
numero = int(
    input("Elige una opción (1=Mayúsculas, 2=Minúsculas, 3=Primera mayúscula): ")
)

# Enviar datos a la función y mostrar resultado
resultado = transformar(texto_usuario, numero)
print("Resultado:", resultado)
