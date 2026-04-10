##Ejercicio 4
## 1. Toma la palabra "CANTANDO".
##2. Convierte toda la cadena a letras minusculas.
##3. Elimina el sufijo "ando" de la palabra resultante y encuentra en que indice (posicion) quedo la letra "t".


palabra = "CANTANDO"
minusculas = palabra.lower
sin_sufijo = minusculas.removesuffix("ando")
posicion_t = sin_sufijo.find("t")

print("En minusculas;", minusculas)
print("sin_sufijo;", sin_sufijo)
print("posicion de `t`:", posicion_t)
