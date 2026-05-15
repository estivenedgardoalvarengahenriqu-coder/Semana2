# Ejercicio 4: Auditoría de Registros del Sistema
# Revisamos 50 registros, pero algunos están corruptos y uno es una amenaza seria

for registro in range(1, 51):

    # Los múltiplos de 3 están corruptos, los saltamos sin hacer ruido
    if registro % 3 == 0:
        continue

    # Si llegamos al registro 42 hay una brecha de seguridad, paramos todo inmediatamente
    if registro == 42:
        print(
            "¡Alerta! Brecha de seguridad detectada en registro 42. Proceso detenido."
        )
        break

    # Si el registro está bien, lo procesamos normalmente
    print(f"Procesando registro ID: {registro}")
