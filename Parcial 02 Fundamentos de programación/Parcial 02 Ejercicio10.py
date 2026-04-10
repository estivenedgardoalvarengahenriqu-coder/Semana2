##Ejercicio 10
##1. Toma la cadena "Python2026".
##2. Verifica si el texto es estrictamente alfanumérico (solo letras y números, sin espacios ni símbolos).
##3. Si lo es, convierte el texto a minúsculas y luego separa la palabra de los números reemplazando "2026" por una cadena vacia "".


## Tomar la cadena "Python2026"
texto = "Python2026"
print(texto)

## Verificar si es estrictamente alfanumérico
es_alfanumerico = texto.isalnum()
print(es_alfanumerico)

## Si lo es, convertir a minúsculas y separar la palabra de los números
if es_alfanumerico:
    texto_minusculas = texto.lower()
    print(texto_minusculas)
    solo_palabra = texto_minusculas.replace("2026", "")
    print(solo_palabra)
