##Ejercicio 3
## 1. Crea una variable con el texto "ING. Su nombre".
## 2. Remueve el prefijo "ING. " de la cadena.
## 3. Convierte el texto restante completamente a letras mayusculas.


## Declaración de la variable
nombre = "ING. Su nombre"
print(nombre)

## Remover el prefijo "ING. "
nombre_sin_prefijo = nombre.removeprefix("ING. ")
print(nombre_sin_prefijo)

## Convertir a mayúsculas
nombre_mayusculas = nombre_sin_prefijo.upper()
print(nombre_mayusculas)
