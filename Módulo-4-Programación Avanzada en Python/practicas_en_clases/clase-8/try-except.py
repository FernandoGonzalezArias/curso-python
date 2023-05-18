print("--------------------------------------------------------")
class EjemploIndexError:
    def __init__(self, datos):
        self.datos = datos

    def acceder_elemento(self, indice):
        try:
            elemento = self.datos[indice]
            print("El elemento en el índice {} es: {}".format(indice, elemento))
        except IndexError:
            print("Error: ¡Índice fuera de rango!")

lista_datos = [1, 2, 3]
ejemplo = EjemploIndexError(lista_datos)

ejemplo.acceder_elemento(0)  
ejemplo.acceder_elemento(5)  

print("--------------------------------------------------------")
class EjemploKeyError:
    def __init__(self, diccionario):
        self.diccionario = diccionario

    def acceder_valor(self, clave):
        try:
            valor = self.diccionario[clave]
            print("El valor para la clave '{}' es: {}".format(clave, valor))
        except KeyError:
            print("Error: ¡Clave no encontrada!")


datos_dict = {"a": 1, "b": 2, "c": 3}
ejemplo = EjemploKeyError(datos_dict)

ejemplo.acceder_valor("a")  
ejemplo.acceder_valor("d") 

print("--------------------------------------------------------")

class EjemploTypeError:
    def __init__(self, valor):
        self.valor = valor

    def multiplicar(self, multiplicador):
        try:
            resultado = self.valor * multiplicador
            print("El resultado de la multiplicación es:", resultado)
        except TypeError:
            print("Error: ¡Tipo de operando no admitido!")

# Ejemplo de uso
ejemplo = EjemploTypeError(5)

ejemplo.multiplicar(2)        # Multiplicación exitosa entre un entero y otro entero
ejemplo.multiplicar("hola")   # Genera un TypeError al intentar multiplicar un entero con una cadena


print("--------------------------------------------------------")

