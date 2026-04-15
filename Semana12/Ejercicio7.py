##Ejercicio 7:
##Solicita el monto de una compra y aplica:
##Más de 100: 20% de descuento
##Entre 50 y 100: 10% de descuento
##Menos de 50: sin descuento

monto = float(input("Monto de la compra: $"))

if monto > 100:
    descuento = monto * 0.20
    print(f"Descuento 20%: ${descuento:.2f}")
    print(f"Total a pagar: ${monto - descuento:.2f}")
elif monto >= 50:
    descuento = monto * 0.10
    print(f"Descuento 10%: ${descuento:.2f}")
    print(f"Total a pagar: ${monto - descuento:.2f}")
else:
    print("Sin descuento")
    print(f"Total a pagar: ${monto:.2f}")
