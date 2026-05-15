#   Sistema de Gestión de Estudiantes

nombres = []  # Array de nombres
notas = []  # Array de notas (índice corresponde a cada nombre)


def clasificar_nota(nota):
    """Clasifica el estado del estudiante según su nota usando if/elif."""
    if nota >= 9:
        return "Excelente"
    elif nota >= 7:
        return "Aprobado"
    elif nota >= 6:
        return "Regular"
    else:
        return "Reprobado"


def agregar_estudiante():
    nombre = input("Nombre del estudiante: ").strip()
    if not nombre:
        print("⚠  El nombre no puede estar vacío.\n")
        return

    try:
        nota = float(input("Nota (0 – 10): "))
    except ValueError:
        print("⚠  Ingresa un número válido.\n")
        return

    if not (0 <= nota <= 10):
        print("⚠  La nota debe estar entre 0 y 10.\n")
        return

    nombres.append(nombre)
    notas.append(nota)
    estado = clasificar_nota(nota)
    print(f"✓  {nombre} agregado | Nota: {nota:.1f} | Estado: {estado}\n")


def mostrar_lista():
    if not nombres:
        print("No hay estudiantes registrados.\n")
        return

    print(f"\n{'N°':<4} {'Nombre':<25} {'Nota':>6}  {'Estado'}")
    print("-" * 50)

    # Bucle for para recorrer y mostrar los datos
    for i in range(len(nombres)):
        estado = clasificar_nota(notas[i])
        print(f"{i+1:<4} {nombres[i]:<25} {notas[i]:>6.1f}  {estado}")

    print()


def buscar_estudiante():
    criterio = input("Nombre a buscar: ").strip().lower()
    encontrados = 0

    # Bucle for para recorrer la lista de nombres
    for i in range(len(nombres)):
        if criterio in nombres[i].lower():
            estado = clasificar_nota(notas[i])
            print(f"  → {nombres[i]} | Nota: {notas[i]:.1f} | Estado: {estado}")
            encontrados += 1

    if encontrados == 0:
        print("No se encontró ningún estudiante con ese nombre.")
    print()


def mostrar_promedio():
    if not notas:
        print("No hay notas registradas aún.\n")
        return

    # Bucle for para calcular la suma
    total = 0
    for nota in notas:
        total += nota

    promedio = total / len(notas)
    estado = clasificar_nota(promedio)

    print(f"\n  Total de estudiantes : {len(nombres)}")
    print(f"  Suma de notas        : {total:.1f}")
    print(f"  Promedio general     : {promedio:.2f}")
    print(f"  Estado del grupo     : {estado}\n")


def mostrar_menu():
    print("=" * 40)
    print("  SISTEMA DE GESTIÓN DE ESTUDIANTES")
    print("=" * 40)
    print("  1. Agregar estudiante")
    print("  2. Mostrar lista de estudiantes")
    print("  3. Buscar estudiante por nombre")
    print("  4. Ver promedio general")
    print("  5. Salir")
    print("=" * 40)


# ── Bucle while: mantiene el menú activo hasta que el usuario elija salir ──
while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-5): ").strip()

    # ── match-case: controla las opciones del menú principal ──
    match opcion:
        case "1":
            print("\n── Agregar estudiante ──")
            agregar_estudiante()
        case "2":
            print("\n── Lista de estudiantes ──")
            mostrar_lista()
        case "3":
            print("\n── Buscar estudiante ──")
            buscar_estudiante()
        case "4":
            print("\n── Promedio general ──")
            mostrar_promedio()
        case "5":
            print("\nHasta luego. ¡Buena suerte con las notas!\n")
            break
        case _:
            print("⚠  Opción no válida. Ingresa un número del 1 al 5.\n")
