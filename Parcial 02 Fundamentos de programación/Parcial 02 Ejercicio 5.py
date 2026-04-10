##Ejercicio 5
## 1. Inicia con la cadena "pYTHON".
## 2. Invierte las mayusculas por minusculas y las minusculas por mayusculas.
## 3. Alinea este nuevo texto hacia la izquierda en un espacio de 15 caracteres, rellenando los espacios vacios con asteriscos ("*").

## Iniciar con la cadena "pYTHON"
texto = "pYTHON"
print(texto)

## Invertir mayúsculas por minúsculas y minúsculas por mayúsculas
texto_invertido = texto.swapcase()
print(texto_invertido)

## Alinear a la izquierda en 15 caracteres rellenando con asteriscos
texto_alineado = texto_invertido.ljust(15, "*")
print(texto_alineado)
