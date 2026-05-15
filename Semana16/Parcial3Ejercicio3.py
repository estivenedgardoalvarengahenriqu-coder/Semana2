# Ejercicio 3: Sistema de Alertas para Sensor Industrial
# El sensor manda 5 lecturas y nosotros decidimos qué alerta disparar según el valor

lecturas = []

# Recolectamos las 5 temperaturas que el sensor envía
for i in range(1, 6):
    temperatura = int(input(f"Ingrese la lectura {i} de temperatura: "))
    lecturas.append(temperatura)

print("\n--- Procesando lecturas del sensor ---")

# Revisamos cada temperatura y evaluamos qué está pasando
for temp in lecturas:
    match temp:
        case 0:
            print("Alerta: Punto de Congelación")
        case 100:
            print("Alerta: Punto de Ebullición")
        case _:
            # Si no es ninguno de los casos especiales, vemos si está en rango normal o no
            estado = "Estado: Estable" if 10 <= temp <= 30 else "Estado: Crítico"
            print(estado)
