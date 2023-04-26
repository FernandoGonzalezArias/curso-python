print("=============== DICIONARIO =================")

empy_dict = {}

fullfield_dict = {
    "id": 1,
    "name": "valeria"
}

print(empy_dict)
print(fullfield_dict)

#conversion dict(variable_iterable)
lista_1 = ['a1', 'b2']
dict_converted = dict(lista_1)
print(lista_1, dict_converted)

#obtener un elemento Por ejemplo
mi_diccionario = {"nombre": "Juan", "edad": 30}
edad = mi_diccionario["edad"]
print(edad)

#añadir un elemento : En Python, puedes añadir un nuevo par clave-valor a un diccionario
#  utilizando la sintaxis diccionario[nueva_clave] = nuevo_valor.
#  Por ejemplo, si tienes un diccionario llamado "mi_diccionario" 
# que contiene los pares clave-valor "nombre": "Juan" y "edad": 30, y
#  quieres añadir el par clave-valor "profesión": "programador",
#  puedes hacerlo de la siguiente manera:
mi_diccionario = {"nombre": "Juan", "edad": 30}
mi_diccionario["profesion"] = "programador"
print(mi_diccionario)

#También puedes insertar un elemento en una posición específica de la lista
#  utilizando el método insert(). Este método toma dos argumentos: 
# el índice en el que deseas insertar el elemento y el valor del elemento.
#Por ejemplo, si deseas insertar el elemento "x" en la posición 2 
# de la lista "mi_lista", puedes hacerlo de la siguiente manera:
mi_lista = ["a", "b", "c"]
mi_lista.insert(2, "x")
print(mi_lista)

#Para modificar un elemento en un diccionario en Python,
#  puedes utilizar la sintaxis diccionario[clave] = nuevo_valor,
#  donde clave es la clave del elemento que deseas modificar y nuevo_valor es
#  el nuevo valor que deseas asignarle. Por ejemplo,
#  si tienes un diccionario llamado "mi_diccionario" que contiene 
# los pares clave-valor "nombre": "Juan" y "edad": 30, 
# y quieres cambiar el valor de la clave "edad" a 35, puedes hacerlo 
# de la siguiente manera:
mi_diccionario = {"nombre": "Juan", "edad": 30}
mi_diccionario["edad"] = 35
print(mi_diccionario)

#Para eliminar un elemento en un diccionario en Python, 
# puedes utilizar la sintaxis del diccionario[clave],
#  donde clave es la clave del elemento que deseas eliminar. Por ejemplo,
#  si tienes un diccionario llamado "mi_diccionario" que contiene los pares
#  clave-valor "nombre": "Juan" y "edad": 30, y quieres eliminar el elemento
#  con la clave "edad", puedes hacerlo de la siguiente manera:
mi_diccionario = {"nombre": "Juan", "edad": 30}
del mi_diccionario["edad"]
print(mi_diccionario)

emty_dict_2 = dict()    #diccionario vacio
print(emty_dict_2)

full_dict = dict(
    genero = "M",
    nacionalidad = "Chilena"
)
print(full_dict)

#recorrer elementos por variable:
empleado ={
    "name": "Fernando",
    "apellido": "Gonzalez",
    "edad": 28,
    "rut": "18.750.211-k"
}
print(empleado)
for variablex in empleado.values():
    print(variablex)

    #recorrer elementos x clave:
for a, b in empleado.items():
    print(a, b)

print("=============== CONDICIONALES =================")

#if condicion :
#bloque de codigo

edad = 60
if edad >50:
    print("hola don")

#-------------------------------

temperatura = 38
if temperatura >= 37:
    print("tempeatura alta")
else:
    print("temperatura normal")
#---------------------------------
temperatura = 15
pais = 'Chile'

if temperatura < 10:
    if pais == 'Chile':
        print('sii')
    else:
        print('noo')
else:
    if pais == 'Chile':
        print('111')
    else:
        print('222')
#------------------------------------
if temperatura <10:
    print("es altamente posible que nieve")
elif temperatura >= 10 and temperatura <= 20:
    print("es medianamente probable que nieve")
else:
    print("no hay posibilidades de nieve")
#------------------------------------------


print("=============== CICLOS =================")
#WHILE
print("While 1")
want_exit = 'n'
while want_exit == 'n':
    print("Hola como estas")
    want_exit = input("¿quieres salir S/N?")

print("fuera del while")

#----------------------------------------
print("While 2")
want_exit = 'n'
num_questions = 0
while want_exit == 'n':
    print("Hola como estas")
    want_exit = input("¿quieres salir S/N?")
    num_questions += 1
    if num_questions == 3:
        print("alcanzaste el maximo permitido")
        break
print("se acabo el while")
