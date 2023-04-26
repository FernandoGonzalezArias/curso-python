class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

gato = Animal("Angora", "Persa") # obtener su valor
# print(gato.type) 

gato.type = "Grandanes" # Modificar el valor
print(gato.type)