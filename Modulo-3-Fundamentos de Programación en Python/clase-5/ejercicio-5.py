# 5. Escriba un programa que eliminar un signo de exclamación del final de una cadena. 
#     puede suponer que los datos de entrada son siempre una cadena, no es necesario verificarlos.

cadena = input("Ingrese una cadena: ")

if cadena.endswith("!"):
    nueva_cadena = cadena[:-1]
    print("La nueva cadena es:", nueva_cadena)
else:
    print("La cadena ingresada no termina en un signo de exclamación")
