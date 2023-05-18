# 4. Dado un mes como un número entero del 1 al 12, devuelva a qué trimestre del año pertenece como un número entero.
#     Por ejemplo: el mes 2 (febrero), forma parte del primer trimestre; el mes 6 (junio), 
#     forma parte del segundo trimestre; y el mes 11 (noviembre), forma parte del cuarto trimestre.

mes = int(input("Ingrese el número de mes (1-12): "))

if mes >= 1 and mes <= 3:
    trimestre = 1
elif mes >= 4 and mes <= 6:
    trimestre = 2
elif mes >= 7 and mes <= 9:
    trimestre = 3
elif mes >= 10 and mes <= 12:
    trimestre = 4
else:
    print("El número de mes ingresado es inválido")

if mes >= 1 and mes <= 12:
    print("El mes", mes, "pertenece al trimestre", trimestre)
