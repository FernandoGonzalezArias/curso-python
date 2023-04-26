# Escriba una clase MobilePhone que represente un telefono movil.
# Atributos
# manufacturer ( cadena de texto)
# screen_size (flotante)
# num_cores     (entero)
# apps (lista de cadenas de texto)
# status (false: apagado, True: encendido)
# Metodos
# __init__(self, manufacturer, screen_size, num:cores)
#power_on(self)
#power_off(self)
# install_app(self, app)
#uninstall_app(dels, app)

class MobilePhone:
    def __init__(self, manufacturer, screen_size, num_cores):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = []
        self.status = False
        
    def power_on(self):
        self.status = True
        print("Celular prendido")
    def power_off(self):
        self.status = False
        print("Celular apagado")
    def install_app(self, app):
        self.apps.append(app)
    
    def uninstall_app(self, app):
        if app in self.apps:
            self.apps.remove(app)


cel = MobilePhone('Hecho en China', [7.5, 'pulgadas']  , [8, 'Nucleos'])
print("Caracteristicas: ", cel.manufacturer, cel.screen_size, cel.num_cores)

cel.power_on()

cel.install_app('WhatsApp')
cel.install_app('Facebook')
print("Apps instaladas: ", cel.apps)

cel.uninstall_app('Facebook')
print("Apps instaladas despues de desinstalar Facebook: ", cel.apps)

cel.power_off()









