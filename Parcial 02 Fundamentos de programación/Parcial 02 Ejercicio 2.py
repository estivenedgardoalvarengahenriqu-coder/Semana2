##Ejercicio 2
##1. Toma la cadena de texto "Su nombre"".
##2. Convierte el texto para que la primera letra de cada una de las palabras este en mayúscula.


## Tomar la cadena de texto
texto = "estiven alvarenga"
print(texto)

## Convertir la primera letra de cada palabra en mayúscula
texto_titulo = texto.title()
print(texto_titulo)

## Reemplazar "Su Nombre" por "Su Apellido"
texto_reemplazado = texto_titulo.replace("Estiven", "Alvarenga")
print(texto_reemplazado)
