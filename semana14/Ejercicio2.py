def filtrar_nombres(nombres):
    for nombre in nombres:
        if len(nombre) > 5:
            print(nombre)

nombres = []
for i in range(10):
    nombre = input(f"Ingrese nombre {i+1}: ")
    nombres.append(nombre)

print("\nNombres con más de 5 caracteres:")
filtrar_nombres(nombres)