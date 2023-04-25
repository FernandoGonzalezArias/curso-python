def saludar(name):
    print(f'Hola {name} !!!')
saludar('Fernando')

print("---------------------------------------")

def saludar_dos(first_name, last_name):
    print(f'Hola {first_name}, {last_name} !!!!')
saludar_dos(first_name = 'Fernando', last_name = 'Gonzalez')

print("---------------------------------------")

def multiplicar_texto(texto, multiplier):
    print(texto * multiplier)
multiplicar_texto("V", 5)

print("---------------------------------------")

def varietal(param1, param2, *others): #con 1 * transforma en tupla
    print(param1)
    print(param2)
    print(others)
varietal("1A", "2B", 0)

print("---------------------------------------")

def varietal_dos(param1, **others): # si en con 2 ** se transforma en diccionario
    print(param1)
    print(others)
varietal_dos("1A", id = 0) # su key + valor