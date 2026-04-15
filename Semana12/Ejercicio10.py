##Ejercicio 10:
##Pide usuario y contraseña. Si ambos coinciden con valores predefinidos, muestra "Acceso permitido", de lo contrario "Acceso denegado".

USUARIO_CORRECTO = "admin"
CLAVE_CORRECTA = "1234"

usuario = input("Usuario: ")
clave = input("Contraseña: ")

if usuario == USUARIO_CORRECTO and clave == CLAVE_CORRECTA:
    print("✓ Acceso permitido")
else:
    print("✗ Acceso denegado")
