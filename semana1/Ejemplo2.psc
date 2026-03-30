Algoritmo Ejemplo2
	Definir cajero, cuentaDeAhorro,numeroCuenta, cantidadSaliente, Saldo, preguntar Como Entero
	cuentaDeAhorro =1000
	numeroDeCuenta = 12345
	
	Escribir "bienvenido,"
	Escribir "Actividad que desea realizar"
	Escribir "1 para consultar"
	Escribir "2 para extraer dinero de la cuenta de ahorro"
	
	Escribir "Escriba el numero de cuenta a operar"
	Leer preguntar //yo no quiero ser un uno mejor busco otra chamba
	
	si preguntar == 1
		Escribir "Escriba el numero de cuenta a operar"
		Leer preguntar // es valor de numero de cuentas
		
		si preguntar ==numeroDeCuenta
			Escribir "Su saldo es"	cuentaDeAhorro
		FinSi
	FinSi
	
	si preguntar == 2
		Escribir "Escriba el numero de cuenta a operar"
		Leer preguntar // es valor de numero de cuentas
		
		si preguntar ==numeroDeCuenta
			Escribir "Escriba el monto a extraer"
			Leer preguntar //es la cantidad a extraer
			
			//< =
			si preguntar <= cuentaDeAhorro
				Saldo = cuentaDeAhorro - preguntar
				Escribir  "procesando"
				Escribir  "Su saldo actual es de " , Saldo
			FinSi
		FinSi
	FinSi
	
	
	
	//or o puedes llevar
	//panes con cafe o chocolate
	
	//and puedes llevar carne y jamon
	
	//not mejor no
	
		
	
	
	//no pueden comenzar con 
	//nummero
	
	//signos a menos que sea _
	
	//no teben llevar espacio
	
	//== si es igual
	//<> diferente
	
	
	//Si es una calse siempre inicia con Mayusculas
	// es evitar el codigo espagueti 
FinAlgoritmo
