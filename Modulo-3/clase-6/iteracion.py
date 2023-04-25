#recorre palabra por palabra por la funcion split
words = "esto es una cadena de texto"
letter = words.split()
for letter in letter:
    print(letter)
print("-----------------------------------")
#recorre letra por letra
words = "esto es una cadena de texto"
for letter in words:
    print(letter)
print("-----------------------------------")

#romper la iteracion con break
words = "esto es una cadena de texto"
for letter in words:
    if letter !=' ':
        print(letter)
    else:
        break
print("-----------------------------------")

# iterar string
animals_list = ['gato', 'perro', 'pajaro']
for animal in animals_list:
    print(animal)
print("-----------------------------------")

#iterar rangos con range()
list1 = range(2,3)
print(list1)
for number_in in range(1,10):
    print(number_in)
#iterar rangos con range() de 2 en 2
list1 = range(2,3)
print(list1)
for number_in in range(1,10,2): # el tercer valos es para q vaya de 2 en 2 como ej
    print(number_in)

print("----------TABLA DE MULTIPLICAR------------------")
for num_tabla in range(1,10):
    for num_mul in range(1,10):
        result = num_tabla * num_mul
        print(f'{num_tabla} x {num_mul} = {result}')
    print("------------------------")
print("-----------------------------------")

