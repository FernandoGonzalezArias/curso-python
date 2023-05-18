# Escribir un programa que pida al usuario dos números y muestre por pantalla 
# su división. Si el divisor es cero el programa debe mostrar un error.

numerador = float(input("Ingresa el numerador: "))
denominador = float(input("Ingresa el denominador: "))

if denominador == 0:
    print("No se puede dividir por 0")
else:
    resultado = numerador % denominador
    print(f'El resultado es {resultado}')