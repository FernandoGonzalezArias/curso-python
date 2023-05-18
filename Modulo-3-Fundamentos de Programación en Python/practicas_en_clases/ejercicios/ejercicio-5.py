# escribir un programa que pregunte al usuario
# una cantidad a invertir, el interes anual y
# el numero de años, y muestre por pantalla
# el capital obtenido en la inversion

cantidad_invertida = float(input("Introduce la cantidad a invertir: "))
interes_anual = float(input("Introduce el interés anual (%): "))
num_anios = int(input("Introduce el número de años: "))

capital_obtenido = cantidad_invertida * (1 + (interes_anual/100))**num_anios

print("El capital obtenido es de:", round(capital_obtenido, 2), "Pesos")
