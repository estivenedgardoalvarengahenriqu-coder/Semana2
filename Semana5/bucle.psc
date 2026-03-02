Algoritmo bucle
	// bucle es algo que se repite hasta que
	// una condicion logica la rompe 
	
	Definir  contador Como Entero
	Escribir " numero del 0 al 100"
	leer numeroEntrada
	contador = 0
	resultado = 0
	anterior = 0
	sumar = 0
	
	Mientras  contador < numeroEntrada // falso  //null 77 unfined //nome
		anterior = resultado
		contador = contador + 1
		resultado = contador + anterior
		Escribir  "resultado es ", contador , " + ", anterior, "= ", resultado
	FinMientras
	
	Escribir  "password "
	leer pass
	
	Mientras pass <> "nombre de ella + fecha especial"   // ! = <> < >
		Escribir  "romper bucle infinito 1 si 2 no "
		leer respuesta
		si respuesta == "no"
		FinSi
		si respuesta == "si"
			pass = "nombre de ella + fecha especial"
		FinSi
	FinMientras
	
	Escribir  "final" 
	
	// exponentes
	// radicales 
	// parentesis
	// di y mul
	// suma yesta
	
	// contador  i  i++ i--   contador =+  contador = contador + contador
	
FinAlgoritmo
