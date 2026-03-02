Algoritmo LaboratorioSumarHastaNegativo
    
	// segun yo entendi con el enunciado: debo de ingresar numeros 
	//que hagan una suma al momento de ingresar un numero le pedira
	//que ingrese mas numero y asi seguira poniendo, Hasta Que 
	//cuando ingrese un numero negativo la ejecucion finalizara y le dara
	//el resultado de las sumas que solo sean numero positivos 
	// y los negativos la ejecucion entiende que ahi debe detener las sumas
	//y dar el resultado con los numeros positivos
    Definir numero Como Entero
    Definir suma Como Entero
    Definir continuar Como Logico
    // intentare explicar lo que hice en la parte donde dice "definir suma como entero" me base en los archivos anteriores de psc
	//y a la palabra suma lo defini como entero por que sera lo que estaremos haciendo la palabra "Definir como entero"
	// es simplemente que estoy indicando que al ingresar una palabra en medio a este lo definire como la parte entera
	// de la ejecucion, o lo que estoy buscando hacer que en este caso busco hacer una suma con numeros
	// y "definir como logico"  es que al momento de estar ingresando numeros para sumar la ejecucion continuara
	// por que estoy por logicamente siguiendo haciendo las sumas es decir por ejemplo si no tuvieramos "5+5+  =15" la suma daria 10 y no 15
	// entonces le indico que quiero continuar o seguir continuando ingresando datos para lleguir como un bucle
    suma <- 0
    continuar <- Verdadero
    
    Mientras continuar Hacer
        
        Escribir "Ingrese un numero: "
        Leer numero
        
        Si numero < 0 Entonces
            continuar <- Falso
        Sino
            suma <- suma + numero
        FinSi
        // vaya aqui  en esta parte donde dice Escribir "ingrese un numero:" hasta Fin Escribir "la suma total es:" , hay una parte donde dice 
		// "si numero < 0 continuar falso" le estoy indicando que si ingreso un numero negativo a 0 la ejecucion reconocera que no es correcto 
		// las sumas que sean de 0 para arriba y la ejecucion se detendra osea llegara a su fin pero sin embargo en el apartado donde dice
		// "sino suma suma + numero" le estoy indicando que los numero que sean mayor que 0 o en otro contexto que si cumplo con los numero arriba que 
		// 0 la suma seguira continuando
    FinMientras
    
    Escribir "La suma total es: ", suma
    
FinAlgoritmo

// ahora bien como puedo hacer la ejecucion haga lo siguiente
// cuando la ejecucion inicie le pedira que indique un numero puede ingresar por ejemplo: 1
// y le pedira otra vez que indique un numero ponga por partes lo siguiente (si usted gusta) : 2,3,4
// y para detener la suma y le de el resultado, entonces en vez de colocar un numero positivo 
// la proxima vez que le salga ingrese un numero ponga un numero negativo por ejemplo: -1
// y la ejecucion finalizara y le dara como resultado los numeros que marco en los campos en 
// este caso en el ejemplo el resultado le dara : 10 
// y el numero negativo sera ignoraro por que indicamos que es falso y no cumple con lo que pedimos