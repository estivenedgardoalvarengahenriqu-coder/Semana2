##Ejercicio 8
##1. Define un bloque de texto de 3 lineas usando comillas triples (puedes usar un fragmento del poema de la guia).
##2. Cuenta cuantas veces aparece la letra "a" en todo el bloque de texto.
##3. Divide el bloque de texto por sus saltos de linea (splitlines) para convertirlo en una lista de oraciones independientes.


## Definir un bloque de texto de 3 líneas con comillas triples
poema = """Es porque un pajarito de la montaña ha hecho
en el hueco de un árbol, su nido matinal,
que el árbol amanece con música en el pecho."""
print(poema)

## Contar cuántas veces aparece la letra "a"
conteo_a = poema.count("a")
print(f"La letra 'a' aparece {conteo_a} veces")

## Dividir el bloque de texto por saltos de línea
lineas = poema.splitlines()
print(lineas)
