Proceso SistemaEjemplo
	Definir edad, nota Como Entero
    Definir continuar Como Caracter
    Definir numero Como Entero
    
    // --- USO DE AND ---
    Escribir "Ingrese su edad:"
    Leer edad
    Escribir "Ingrese su nota:"
    Leer nota
    
    Si edad >= 18 Y nota >= 7 Entonces
        Escribir "Aprobado y mayor de edad"
    Sino
        Escribir "No cumple ambas condiciones"
    FinSi
    
    
    // --- USO DE OR ---
    Si edad < 18 O nota < 7 Entonces
        Escribir "No cumple al menos una condición"
    FinSi
    
    
    // --- USO DE DIFERENTE ---
    Si nota <> 10 Entonces
        Escribir "No obtuvo nota perfecta"
    FinSi
    
    
    // --- BUCLE MIENTRAS ---
    numero <- 1
    Mientras numero <= 3 Hacer
        Escribir "Mientras: ", numero
        numero <- numero + 1
    FinMientras
    
    
    // --- BUCLE PARA ---
    Para i <- 1 Hasta 3 Con Paso 1 Hacer
        Escribir "Para: ", i
    FinPara
    
    
    // --- BUCLE REPETIR ---
    Repetir
        Escribir "Desea continuar? (S/N)"
        Leer continuar
    Hasta Que continuar = "N"
    
    
    // --- USO DE SEGUN ---
    Escribir "Ingrese una opción (1-3):"
    Leer numero
    
    Segun numero Hacer
        1:
            Escribir "Opción 1 seleccionada"
        2:
            Escribir "Opción 2 seleccionada"
        3:
            Escribir "Opción 3 seleccionada"
        De Otro Modo:
            Escribir "Opción inválida"
    FinSegun
    
    
    // --- LLAMADO A FUNCION CON RETORNO ---
    Escribir "Ingrese un número para calcular cuadrado:"
    Leer numero
    Escribir"El cuadrado es:", Cuadrado (numero)
    
    
    // --- LLAMADO A SUBPROCESO (SIN RETORNO) ---
    Saludo("Eder")
FinProceso

Funcion resultado <- NombreFuncion(parametros)
    
    // proceso
    
FinFuncion

SubProceso Saludo(nombre)
    Escribir "Bienvenido ", nombre
FinSubProceso


