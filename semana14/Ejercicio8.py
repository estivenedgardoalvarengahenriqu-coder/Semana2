def buscar_producto(productos, busqueda):
    for producto in productos:
        if producto.lower() == busqueda.lower():
            return True
    return False


productos = ["Arroz", "Leche", "Pan", "Huevos", "Aceite"]
busqueda = input("Ingrese el producto a buscar: ")

if buscar_producto(productos, busqueda):
    print(f"'{busqueda}' fue encontrado.")
else:
    print(f"'{busqueda}' no está en la lista.")
