nombres = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']

magos = ['Harry Houdini', 'David Blaine', 'Teller']
cientificos = ['Newton', 'Hawking', 'Einstein']
otros = [nombre for nombre in nombres if nombre not in magos and nombre not in cientificos]

def hacer_grandioso():
    for i in range(len(magos)):
        magos[i] = 'El gran ' + magos[i]

def imprimir_nombres():
    for nombre in nombres:
        print(nombre)

print("-----------------Inicio-----------------------")

print('Lista completa de nombres:')
imprimir_nombres()
print()

hacer_grandioso()

print("----------------------------------------------")

print('Magos grandiosos:')
for mago in magos:
    print(mago)
print()

print("----------------------------------------------")

print('Científicos:')
for cientifico in cientificos:
    print(cientifico)
print()

print("----------------------------------------------")

print('Otros:')
for otro in otros:
    print(otro)

print("-----------------Fin-----------------------")
