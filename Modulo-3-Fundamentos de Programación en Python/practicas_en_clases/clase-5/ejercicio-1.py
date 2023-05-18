# 1. Cree un programa que encuentre el promedio de los tres puntajes dados y devuelva el valor de la letra 
# asociada con esa calificación. con al siguiente tabla
#     0   - 2     D
#     2.1 - 5     C
#     5.1 - 6     B
#     6.1 - 7     A

# Pedimos al usuario que ingrese los tres puntajes
puntaje1 = float(input("Ingrese el puntaje 1 (entre 0 y 7): "))
puntaje2 = float(input("Ingrese el puntaje 2 (entre 0 y 7): "))
puntaje3 = float(input("Ingrese el puntaje 3 (entre 0 y 7): "))

# puntajes dentro del rango 
if puntaje1 < 0 or puntaje1 > 7 or puntaje2 < 0 or puntaje2 > 7 or puntaje3 < 0 or puntaje3 > 7:
    print("Error: los puntajes ingresados deben estar entre 0 y 7")
else:
 # Calculamos el promedio 
    promedio = (puntaje1 + puntaje2 + puntaje3) / 3
# Asignamos la letra 
    if promedio >= 0 and promedio <= 2:
        letra = "D"
    elif promedio > 2 and promedio <= 5:
        letra = "C"
    elif promedio > 5 and promedio <= 6:
        letra = "B"
    else:
        letra = "A"
# Mostramos  el promedio y la letra
    print("El promedio de los puntajes es:", promedio)
    print("La letra correspondiente es:", letra)
