# simular un juego
# ingresar una cantidad par de numeros
# debo emparejarlas con un texto
# debo dar un numero de intentos definido para el usuario
# prepara el buble y el select case

import random
from unittest import case  # esto es para generar numeros aleatorios

# Salvar el numero random en una variable
numero = random.randint(1, 10)
# print(numero)


def definirTargetas(numero):
    if numero % 2 == 0 and numero > 4:
        return numero
    else:
        return numero + 1


def asignarValoresAlasTargetas(numeroValidad):
    i = 0
    llenarTargetas = []
    temporal = ""
    while i <= numeroValidad:
        temporal = input("Ingrese un texto para la targeta " + str(i) + ": ")
        llenarTargetas.append(temporal)
    return llenarTargetas


def validarTargetas(numeroEscogen, rangoNumeros, llenarTargetas):
    # definir el numero de targetas

    for i in rangoNumeros:
        match numeroEscogen:
            case 1:
                if llenarTargetas[1] == llenarTargetas[1]:
                    print("Ganaste")
            case 2:
                if llenarTargetas[2] == llenarTargetas[2]:
                    print("Ganaste")
            case 3:
                if llenarTargetas[3] == llenarTargetas[3]:
                    print("Ganaste")
            case 4:
                if llenarTargetas[4] == llenarTargetas[4]:
                    print("Ganaste")
            case 5:
                if llenarTargetas[5] == llenarTargetas[5]:
                    print("Ganaste")
            case 6:
                if llenarTargetas[6] == llenarTargetas[6]:
                    print("Ganaste")
            case 7:
                if llenarTargetas[7] == llenarTargetas[7]:
                    print("Ganaste")
            case 8:
                if llenarTargetas[8] == llenarTargetas[8]:
                    print("Ganaste")
            case 9:
                if llenarTargetas[9] == llenarTargetas[9]:
                    print("Ganaste")
            case 10:
                if llenarTargetas[10] == llenarTargetas[10]:
                    print("Ganaste")
            case _:
                print("Perdiste")
