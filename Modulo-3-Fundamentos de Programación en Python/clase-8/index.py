class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

gato = Animal("Angora", "Persa") # Obtener su valor
print(gato.type) 

gato.type = "Grandanes" # Modificar el valor
print(gato.type)

print("----------------------------------------------------")
class Droid:
    def __init__(self, name):
        self.hidden_name = name

    @property
    def name(self) -> str: 
        return self.hidden_name
    
    @name.setter
    def name(self, name:  str) -> None:
        self.hidden_name = name

androide = Droid("Arthur")
print(androide.name)
androide.name = "citripio"
print(androide.name )

print("----------------------------------------------------")

class CalculatedValue:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    @property
    def get_calculate_value(self) -> float:
        return 0.35 * self.height
    
valuex = CalculatedValue("Ratio", 10)
print(f'El {valuex.name} es: {valuex.get_calculate_value}')

print("----------------------------------------------------")

class Dog:
    obeys_owner = True

    def __init__(self, name):
        self.name = name 

dog_one = Dog("Robin")
dog_two = Dog("Malta")
dog_three = Dog("Luz")

print(f'{dog_one.name} obedece a su dueño {dog_one.obeys_owner}')
print(f'{dog_two.name} obedece a su dueño {dog_two.obeys_owner}')
print(f'{dog_three.name} obedece a su dueño {dog_three.obeys_owner}')
print("-------separando perros----------")
dog_one.obeys_owner = False
print(f'{dog_one.name} obedece a su dueño {dog_one.obeys_owner}')
print(f'{dog_two.name} obedece a su dueño {dog_two.obeys_owner}')
print(f'{dog_three.name} obedece a su dueño {dog_three.obeys_owner}')
print("--------")
Dog.obeys_owner = True
print(f'{dog_one.name} obedece a su dueño {dog_one.obeys_owner}')
print(f'{dog_two.name} obedece a su dueño {dog_two.obeys_owner}')
print(f'{dog_three.name} obedece a su dueño {dog_three.obeys_owner}')


