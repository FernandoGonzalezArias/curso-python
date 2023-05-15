## Autos y Motos, Bicicletas
## Autos [color, tipo_motor, ruedas, cantidad_puertas, ruedas, tipo_encendido, tipo_freno]
## Motos [color, tipo_motor, ruedas, tipo_freno, tipo_encendido, tipo_cadena]
## Bicicletas [color, ruedas, tipo_freno, tipo_manubrio]

## un metodo del padre que lo hereden todos
## un metdo diferente para cada clase hija

class Vehiculo:
    def __init__(self, _color, _ruedas, _tipo_freno):
        self.color = _color
        self.ruedas = _ruedas
        self.tipo_freno = _tipo_freno

    def frenar(self):
        print("este vehiculo esta frenando")

class VehiculoMotorizado:
    def __init__(self,  _tipo_motor, _tipo_encendido):
        self.tipo_motor = _tipo_motor
        self.tipo_encendido = _tipo_encendido

class Auto(Vehiculo, VehiculoMotorizado):
    def __init__(self, _color, _ruedas, _tipo_freno, _tipo_motor, _tipo_encendido ):
        Vehiculo.__init__(self, _color, _ruedas, _tipo_freno)
        VehiculoMotorizado.__init__(self, _tipo_motor, _tipo_encendido)

    def abrir_puerta(self, _puerta):
        print(f'abriendo la puerta {_puerta}')

class Moto(Vehiculo, VehiculoMotorizado):
    def __init__(self, _color, _ruedas, _tipo_freno, _tipo_motor, _tipo_encendido, _tipo_cadena):
        Vehiculo.__init__(_color, _ruedas, _tipo_freno)
        VehiculoMotorizado.__init__(self, _tipo_motor, _tipo_encendido)
        self.tipo_cadena = _tipo_cadena


class Bicicleta(Vehiculo):
    def __init__(self, _color, _ruedas, _tipo_freno, _tipo_manubrio):
        super().__init__(_color, _ruedas, _tipo_freno)
        self.tipo_manubrio = _tipo_manubrio

    def pedalear(self, sentido):
        print(f'la bicleta est apedaleando hacia {sentido}')