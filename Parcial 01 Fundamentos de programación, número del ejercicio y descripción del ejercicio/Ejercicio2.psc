Algoritmo SumaNumerosPositivos
	Definir num, suma Como Entero
	
	suma <- 0
	num <- 0
	
	Mientras num >= 0 Hacer
		
		Escribir "Ingrese un numero: "
		Leer num
		
		Si num >= 0 Entonces
			suma <- suma + num
		FinSi
		
	FinMientras
	
	Escribir "La suma de los numeros positivos es: ", suma
FinAlgoritmo