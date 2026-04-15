##Ejercicio 9:
##Solicita un año y determina si es bisiesto.

anio = int(input("Ingresa un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print(f"{anio} ES bisiesto")
else:
    print(f"{anio} NO es bisiesto")
