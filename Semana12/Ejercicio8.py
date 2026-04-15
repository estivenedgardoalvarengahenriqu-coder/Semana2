##Ejercicio 8:
##Pide tres lados de un triángulo y determina si es equilátero, isósceles o escaleno.

a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))

if a == b == c:
    print("Triángulo equilátero")
elif a == b or b == c or a == c:
    print("Triángulo isósceles")
else:
    print("Triángulo escaleno")
