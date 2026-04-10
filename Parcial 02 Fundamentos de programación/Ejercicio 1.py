##Ejercicio 1
## 1. Declara una variable con la cadena "  elefante  ".
## 2. Utiliza el método correspondiente para eliminar los espacios en blanco a ambos extremos de la palabra.
## 3. Cuenta y muestra cuántas veces se repite la letra "e" en el texto ya limpio.


## Declarar una variable con la cadena "  elefante  "
cadena = "  elefante  "
print(cadena)

## Eliminar los espacios en blanco a ambos extremos
cadena_limpia = cadena.strip()
print(cadena_limpia)

## Contar cuántas veces se repite la letra "e" en el texto ya limpio
conteo_e = cadena_limpia.count("e")
print(f"La letra 'e' aparece {conteo_e} veces")
