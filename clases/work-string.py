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
