class Padre:
    def __init__(self, _name_padre, _rut_padre):
        self.name = _name_padre
        self.rut = _rut_padre
        self.sueldo = 0
    
    def pintar(self, _color):
        print(f"{self.name} esta pintando con el color {_color}")

class Hijo(Padre):
    def __init__(self, _name_hijo, _rut_hijo, _color_ojos):
        Padre.__init__(self, _name_hijo, _rut_hijo)
        self.color_ojos = _color_ojos
    
    def lijar(self):
        print(f"{self.name} esta lijando")

richar = Padre("Richar Lujano", "1")

richard = Hijo("Richard Lujano", "2", 'Marron')


print(richar.name, richar.sueldo)
print(richard.name, richard.sueldo)

richar.pintar("Rojo")
richard.pintar("verde")
richard.lijar()