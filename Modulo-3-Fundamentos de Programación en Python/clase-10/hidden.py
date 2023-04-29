class Droid:
    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

arturo = Droid("Arturo")


print(arturo.name)

## Cree una clase llamada Artefacto, agreguele tres atributos y
## utilice los getter and setter para acceder a lleos