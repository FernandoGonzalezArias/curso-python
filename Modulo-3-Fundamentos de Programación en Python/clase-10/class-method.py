class Empleado:
    sueldo_base = 100.000

    def __init__(self, _name):
        self.__name = _name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, _name):
        self.__name = _name

    @classmethod
    def obtener_sueldo_base(cls):
        return cls.sueldo_base
    
    @classmethod
    def modificar_sueldo_base(cls, _sueldo):
        cls.sueldo_base = _sueldo