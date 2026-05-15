# Ejercicio 2: Terminal de Cobro Seguro
# Usamos Decimal en lugar de float porque con float los centavos se descuadran
from decimal import Decimal

total = Decimal("0")

# El terminal se queda corriendo hasta que el cajero ingrese 0 para cerrar
while True:
    entrada = input("Ingrese el precio del producto (0 para finalizar): ")

    try:
        precio = Decimal(entrada)

        # Si el usuario mete 0, cerramos y mostramos el total
        if precio == 0:
            break

        total += precio
        print(f"Precio agregado: ${precio}  |  Total acumulado: ${total}")

    except ValueError:
        # Si escribieron letras o algo raro, avisamos pero no tronamos el programa
        print("Advertencia: eso no es un número válido, intente de nuevo.")

print(f"\nTotal final de la compra: ${total}")
