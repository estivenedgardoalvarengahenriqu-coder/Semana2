Algoritmo CalificacionEstudiante
	Definir nota Como Entero
	
	Escribir "Ingrese la nota del estudiante (0 a 10): "
	Leer nota
	
	Si nota >= 6 Entonces
		Escribir "Aprobado"
		
	SiNo
		Si nota = 5 Entonces
			Escribir "Recuperacion"
		SiNo
			Escribir "Reprobado"
		FinSi
	FinSi
	
FinAlgoritmo