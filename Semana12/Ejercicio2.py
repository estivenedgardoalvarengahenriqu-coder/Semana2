##Ejercicio 2:
##Solicita la edad de una persona y muestra si es menor de edad, mayor de edad o adulto mayor (60 o más).

edad = int(input("Ingresa tu edad: "))

if edad < 18:
    print("Es menor de edad")
elif edad < 60:
    print("Es mayor de edad")
else:
    print("Es adulto mayor")
15
