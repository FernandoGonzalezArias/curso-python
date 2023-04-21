print("=============== STRING ==================")
# al concatenar se da el espacio con un " " vacio y con espacio al medio
first_name = "Fernando"
Last_name = "Gonzalez"
print(first_name + " " + Last_name)  

 # para dar espacio entre los 3 holas repeditos solo se le da y espacio al final de la palabra
mensaje1 = "Hola " *3       
print(mensaje1)

# añadir con +=
mensaje3 = "Bryan"         
print(mensaje3)
mensaje3 += ","           
print(mensaje3)
mensaje3 += " Arias"
print(mensaje3)

#len, lo que hace es obtener el total de caracteres
print(len(mensaje3))

# funcion propia como por ej find
# busca coicidencia dentro de un sting
cadena = "esto es una oracion por ucrania"
posicion = cadena.find("pelo")
print("pelo se encuentra en:", posicion)
posicion = cadena.find("ucrania")
print("ucrania se encuentra en:", posicion)

#funcion lower: para convertir una cadena de caracteres en minuscula
string = "EJEMPLO DE CADENA"
lower_string = string.lower()
print(lower_string)

# como reemplazar una cadena  utilizando replace()
cadena = "Me gusta Mac"
nueva_cadena = cadena.replace("Mac", "Window")
print(nueva_cadena)

print("=============== LISTAS ==================")

#variable[]
emty_List = []
print(emty_List)

full_list = [1, 3, 500, 1.4, [2, "a"], {"name": "Fernando"}, (1,3,5)]
print(full_list)

# Lista(), permite convertir a lista
second_list = list()
print(second_list)
# convertir cadenas de texto en listas
print(list("concurso"))
#Range(), un rango cconvertido en una lista de numeros
range_one = range(10)
print(list(range_one))

#agregar un item a la lista append()
numeros = [1, 4, 6]
print(numeros)
numeros.append(10)
print(numeros)
# como seleccionar o extraer un iten de la lista, con la posicion, lista[posicion]
print(numeros[2])
# como recorrer la lista con For y Range
for i in range(len(numeros)):
 print(numeros[i])
#como eliminar un elemento de la lista  con remove()
numeros.remove(4)
print(numeros)
#modificar la lista, a la variable se escribe al lado el indice del numero cual cambiar
numeros[0] = 5
print(numeros)

print("=============== TUPLAS ==================")

#TUPLAS: son inmutables, no se pueden cambiar y en ves de cerrar asi [] se cierra con (), es como constante
empy_tupla = ()
second = (1, "a", 90)
print(empy_tupla, second)

one_tuple = ('Fernando',)  # para que sea tuple y no string se tiene que terminar con una coma ,
print(type(one_tuple))

emty_tuple_2 = tuple()  # tuple vacia

# una lista la transdormo en tuple
list_to_convert = [2, 6, 8, 9]
print(list_to_convert)
tuple_converter = tuple(list_to_convert)
print(tuple_converter)

la_tupla = [1, 2, 3, 4 ]
revertir_la_tupla = reversed(la_tupla)
print(la_tupla)
print(list(revertir_la_tupla))
