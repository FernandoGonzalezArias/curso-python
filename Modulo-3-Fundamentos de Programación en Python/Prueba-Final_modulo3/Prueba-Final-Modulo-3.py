nombres = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']

# Separar nombres en grupos de magos, científicos y otros
magos = ['Harry Houdini', 'David Blaine', 'Teller']
cientificos = ['Newton', 'Hawking', 'Einstein']
otros = [nombre for nombre in nombres if nombre not in magos and nombre not in cientificos]

def hacer_grandioso():
    # Modificar lista de magos añadiendo 'El gran' antes del nombre de cada mago
    for i in range(len(magos)):
        magos[i] = 'El gran ' + magos[i]

def imprimir_nombres():
    # Imprimir nombre de cada persona de la lista
    for nombre in nombres:
        print(nombre)

# Imprimir la lista completa de nombres antes de ser modificados
print('Lista completa de nombres:')
imprimir_nombres()
print()

# Modificar lista de magos añadiendo 'El gran' antes del nombre de cada mago
hacer_grandioso()

# Imprimir nombres de los magos grandiosos, los nombres de los científicos y los restantes
print('Magos grandiosos:')
for mago in magos:
    print(mago)
print()

print('Científicos:')
for cientifico in cientificos:
    print(cientifico)
print()

print('Otros:')
for otro in otros:
    print(otro)
