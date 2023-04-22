# 3. Escriba un programa que calcule el máximo común divisor entre dos números enteros.

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

a = numero1
b = numero2
while b != 0:
    resto = a % b
    a = b
    b = resto

print("El máximo común divisor de", numero1, "y", numero2, "es", a)

