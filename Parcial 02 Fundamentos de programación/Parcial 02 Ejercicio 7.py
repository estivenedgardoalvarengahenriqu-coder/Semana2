##Ejercicio 7
##1. Toma el texto numérico "42".
##2. Rellenalo con ceros a la izquierda hasta que alcance una longitud total de 5 caracteres.
##3. Verifica mediante un método booleano si esa nueva cadena generada termina con el número "2".

## Tomar el texto numérico "42"
numero = "42"
print(numero)

## Rellenar con ceros a la izquierda hasta longitud de 5
numero_relleno = numero.zfill(5)
print(numero_relleno)

## Verificar si termina con el número "2"
termina_en_dos = numero_relleno.endswith("2")
print(termina_en_dos)
