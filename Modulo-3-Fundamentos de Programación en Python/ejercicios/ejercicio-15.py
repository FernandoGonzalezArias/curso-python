# En una determinada empresa, sus empleados son evaluados al final de cada año.
# Los puntos que pueden obtener en la evaluación comienzan en 0.0 
# y pueden ir aumentando, traduciéndose en mejores beneficios. 
# Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más,
# pero no valores intermedios entre las cifras mencionadas. 
# A continuación se muestra una tabla con los niveles correspondientes a cada puntuación.
# La cantidad de dinero conseguida en cada nivel es de 2.400€ 
# multiplicada por la puntuación del nivel.

# Nivel    Puntuación
# Inaceptable    0.0
# Aceptable    0.4
# Meritorio    0.6 o más
# Escribir un programa que lea la puntuación del usuario e indique su nivel
# de rendimiento, así como la cantidad de dinero que recibirá el usuario

puntuacion = float(input("Introduce tu puntuación: "))

if puntuacion == 0.0:
    nivel = "inaceptable"
    dinero = 0
elif puntuacion == 0.4:
    nivel = "Aceptable"
    dinero = 2400 * puntuacion
elif puntuacion >= 0.6:
    nivel = "Meritorio"
    dinero = 2400 * puntuacion
else:
    nivel = "puntuación incorrecta"
    dinero = "puntuación incorrecta"
    print("Puntuación no válida")

print("Tu nivel es", nivel)
print("Tu bono es", dinero)