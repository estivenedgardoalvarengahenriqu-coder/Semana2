##Ejercicio 11
##1. Toma la cadena "  el nido matinal  ".
##2. Limpia los espacios en blanco de los extremos y haz que la primera letra de cada palabra pase a ser mayuscula.
##3. Toma ese texto procesado y centralo en un espacio total de 30 caracteres, rellenando los espacios a los lados con guiones medios ("-").


## Tomar la cadena "  el nido matinal  "
texto = "  el nido matinal  "
print(texto)

## Limpiar espacios y primera letra de cada palabra en mayúscula
texto_limpio = texto.strip().title()
print(texto_limpio)

## Centrar en 30 caracteres rellenando con guiones medios
texto_centrado = texto_limpio.center(30, "-")
print(texto_centrado)
