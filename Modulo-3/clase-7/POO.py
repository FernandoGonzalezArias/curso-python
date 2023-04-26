#crando una clase
class transporte:
    pass

#instanciar la clase y crear un objeto
transporte1 = transporte()
transporte2 = transporte()

class BuzzeLigthYear:
    pass
bozz1 = BuzzeLigthYear()
bozz2 = BuzzeLigthYear()

print(type(transporte1))
print(type(bozz1))

print("---------------------------------------")

class Droid:                        # clase droid
    def __init__(self):
        self.power_on = False
    def switch_on(self):            #metodo switch_on
        print("Hola soy un droid")  
        self.power_on = True
    def switch_off(self):             # metodo switch_off
        print("Adios enciendeme")
        self.power_on = False


k8_arthur = Droid()
k8_citripio = Droid()

k8_arthur.switch_on()
print("arthur: ", k8_arthur.power_on)
print("citripio: ", k8_citripio.power_on)
k8_arthur.switch_off()
print(k8_arthur.power_on)

print("---------------------------------------")

class Vehicle:
    def __init__(self, type, model):
      self.type_vehicle = type
      self.model_vehicle = model

sedan = Vehicle('Sedan', 'Aveo')
print(sedan.type_vehicle, sedan.model_vehicle)
pickup = Vehicle('Pickup', 'Ranger')
print(pickup.type_vehicle, pickup.model_vehicle)

