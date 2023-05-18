class Figura:
    
    ## Inicializador
    def __init__(self, x, y, color):
        ## Asignacion de variables
        self.x = x
        self.y = y
        self.color = color
        
    def dibujar(self):
        print("Figura dibujada en coordenadas:\n  X:" , self.x, "\n  Y:", self.y)
        print("  Color:", self.color)   

class Cuadrado(Figura):
    
    ## Redifinimos algunos metodos
    def definir_lado(self, lado):
        self.lado = lado
        
    def dibujar(self):
        print("\nCuadrado dibujado en coordenadas:\n  X:" , self.x, "\n  Y:", self.y)
        print("  Color:", self.color)    
        print("  Longitud del costado:", self.lado)
        
class Circulo(Figura):
    
    ## Redifinimos algunos metodos    
    def definir_radio(self, radio):
        self.radio = radio
        
    def dibujar(self):
        print("\nCirculo dibujado en coordenadas:\n  X:" , self.x, "\n  Y:", self.y)
        print("  Color:", self.color)    
        print("  Longitud del radio:", self.radio)
        
        
## Creamos una figura (cuadrado) en una posicion y con un color
c = Cuadrado(2,5, "verde")
# Definimos la longitud del lado
c.definir_lado(5)
c.dibujar()

## Creamos una figura (cuadrado) en una posicion y con un color
r = Circulo(2,5, "rojo")
# Creamos una figura (cuadrado) en una posicion y con un color
r.definir_radio(3)
r.dibujar()