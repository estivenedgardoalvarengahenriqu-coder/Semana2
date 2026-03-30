## Ejercicio 7: Crear una función que reciba un texto y una lista de números (entre 1 y 3). La función debe aplicar cada transformación en orden y devolver el resultado final.


def transformar_multiple(texto, lista_opciones):
    resultado = texto
    for n in lista_opciones:
        if n == 1:
            resultado = resultado.upper()
        elif n == 2:
            resultado = resultado.lower()
        elif n == 3:
            resultado = resultado.capitalize()
        else:
            return "Opción inválida"
    return resultado


# Ejemplo
texto_inicial = "hola mundo"
opciones = [3, 1, 2]  # Aplica capitalize → upper → lower
print(transformar_multiple(texto_inicial, opciones))
