# Para tributar un derminadado impuesto se debe ser mayor de 
# 16 años y tener unos ingresos iguales o superiores a 1000$ mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales 
# y muestre por pantalla si el usuario tiene que tributar o no.

edad_minima = 16
ingresos_tope = [1000, "Euros"]

anios = int(input("Cuántos años tienes? "))
ingreso = float(input("Cuál es tu ingreso mensual? "))

if anios > edad_minima and ingreso >= ingresos_tope:
    print("Pagas impuestos")
else:
    print("No cumple requisitos")