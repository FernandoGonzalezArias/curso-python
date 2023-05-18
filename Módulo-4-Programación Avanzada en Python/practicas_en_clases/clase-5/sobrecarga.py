class Persona:
    message_base = "Te Estoy llamando"
    def __init__(self, _name):
        self.name = _name

    def llamar(self):
        print(self.message_base)

    def llamar(self, _medio=''):
        message = self.message_base
        if (_medio != ''):
            message = f"{self.message_base} con {_medio}"
        print(message)

    def llamar(self, _medio='', _time= ''):
        message = self.message_base
        if (_medio != '' and _time == ''):
            message = f"{self.message_base} con {_medio}"
        if (_medio != '' and _time != ''):
            message = f"{self.message_base} con {_medio} a las {_time}"
        print(message)


juan = Persona("Juan")

juan.llamar("Telefono", '15:00 horas')