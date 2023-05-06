# Imagina que acabas de abrir una nueva cuenta de ahorros que 
# te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se 
# cobran hasta finales de año se añaden al final de tu balance de tu cuenta de 
# ahorros. Escribir un programa que comience leyendo la cantidad de dinero 
# depositada en la cuenta de ahorros introducida por el usuario. Después el 
# programa debe calcular y mostrar por pantalla la cantidad ahorros del primer, 
# segundo y tercer año. Redondear cada cantidad a 2 decimales

interes = 0.04
monto_inicial = float(input("Cuál es el monto de ahorro inicial: "))

saldo_anio1 = monto_inicial + (monto_inicial * interes)
saldo_anio2 = saldo_anio1 + (saldo_anio1 * interes)
saldo_anio3 = saldo_anio2 + (saldo_anio2 * interes)


print('Estado de cuenta')
print(f'Cantidad de ahorros tras el primer año: {round(saldo_anio1, 2)}')
print(f'Cantidad de ahorros tras el segundo año: {round(saldo_anio2, 2)}')
print(f'Cantidad de ahorros tras el tercer año: {round(saldo_anio3, 2)}')