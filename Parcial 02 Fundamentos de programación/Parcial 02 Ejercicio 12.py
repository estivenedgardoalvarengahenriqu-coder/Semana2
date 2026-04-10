## Ejercicio 12
##1. Toma el nombre de archivo "Sunombre.txt".
##2. Remueve el sufijo ".txt" y posteriormente remueve el prefijo "ING. ".
##3. Toma el texto que quede limpio, convertido a minúsculas.

archivo = "Estiven.txt"

# primero quito la extension del archivo
nuevo = archivo.removesuffix(".txt")

# Removemos el sufijo ".txt"
nuevo = nuevo.removesuffix(".txt")

# Removemos el prefijo "ING"
nuevo = nuevo.removeprefix("ING.")

# Y convertir todo a minuscula
nuevo = nuevo.lower()

print(nuevo)
