Algoritmo PrimerosNParesConMOD
	
	Definir N, i, contador Como Entero
	
	Escribir "Ingrese cuantos numeros pares desea ver:"
	Leer N
	
	contador <- 0
	
	Para i <- 1 Hasta N*2 Hacer
		Si i MOD 2 = 0 Entonces
			
			Escribir i
			contador <- contador + 1
		FinSi
		
		Si contador = N Entonces
			i <- N*2
			.
		FinSi
	FinPara
	
FinAlgoritmo
