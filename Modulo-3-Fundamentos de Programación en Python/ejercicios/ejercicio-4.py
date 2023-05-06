# escribir un programa que pregunte al usuario por el numero 
#de horas trabajadas y el coste por hora,
# despues debe mostrar por pantalla el salario que le corresponde

horas_trabajadas = float(input("Introduce el número de horas trabajadas: "))
coste_hora = float(input("Introduce el coste por hora: "))

salario = horas_trabajadas * coste_hora
print("Tu salario es de:",salario, "Pesos")
