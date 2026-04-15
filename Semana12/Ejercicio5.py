##Ejercicio 5:
##Solicita dos números y una operación (+, -, *, /) y realiza el cálculo usando if, elif y else.

a = float(input("Primer número: "))
b = float(input("Segundo número: "))
op = input("Operación (+, -, *, /): ")

if op == "+":
    print(f"Resultado: {a + b}")
elif op == "-":
    print(f"Resultado: {a - b}")
elif op == "*":
    print(f"Resultado: {a * b}")
elif op == "/" and b != 0:
    print(f"Resultado: {a / b}")
elif op == "/" and b == 0:
    print("Error: división entre cero")
else:
    print("Operación no válida")
