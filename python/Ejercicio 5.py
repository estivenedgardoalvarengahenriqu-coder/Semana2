frase = input("Escribe una frase: ")

if frase:  # verificamos que no esté vacía
    primera = frase[0]
    ultima = frase[-1]
    print("Primera letra:", primera)
    print("Última letra :", ultima)
else:
    print("No ingresaste ninguna frase.")
