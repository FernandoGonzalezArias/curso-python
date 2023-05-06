# Escribir un programa que pregunte al usuario su edad y muestre por pantalla
# sie es mayor de edad o no.

edad_maxima = 18
edad_usuario = int(input("Cuál es tu edad? "))

if edad_usuario >= edad_maxima:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")