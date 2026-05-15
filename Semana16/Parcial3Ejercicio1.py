# Ejercicio 1: Clasificación de Paquetes
# Los códigos llegan en formato AÑO-CATEGORÍA-PAÍS, ejemplo: 2024-TECNOLOGIA-SV

# Le pedimos al usuario que escriba el código de rastreo
etiqueta = input("Ingrese el código de rastreo (formato AÑO-CATEGORÍA-PAÍS): ")

# Antes de hacer cualquier cosa, nos aseguramos que no nos mandaron algo vacío
if etiqueta == "" or etiqueta is None:
    print("Error: el código de rastreo está vacío. No hay nada que procesar.")
else:
    # Partimos el código por los guiones y agarramos la parte del medio, que es la categoría
    partes = etiqueta.split("-")
    categoria = partes[1]
    print(f"Categoría detectada: {categoria}")

    # Si el código termina en "SV" es local, de lo contrario va para afuera
    ruta = "Ruta Local" if etiqueta.endswith("SV") else "Ruta Internacional"
    print(f"Tipo de ruta: {ruta}")
