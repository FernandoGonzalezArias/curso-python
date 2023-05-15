class Empleado:
    sueldo = 0 ## variable de clase

    def __init__(self, _name) -> None:
        self.name = _name

persona = Empleado("Juan Perez")
print(persona.name)


## Redifiniendo la clase para hacer el atributo publico name, privado
class EmpleadoProtected:
    sueldo = 0

    def __init__(self, _name) -> None:
        self.__name = _name

    @property                   ## getter
    def name(self):
        return self.__name
    
    @name.setter                ## setter
    def name(self, _name):
        self.__name = _name



persona2 = EmpleadoProtected("maria")
print(persona2.name)

persona2.name = "Juan"
print(persona2.name)