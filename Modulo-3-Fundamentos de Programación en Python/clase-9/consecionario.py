class Motocicleta():
    estado = "nueva"
    motor = False

    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, peso, combustible_maximo):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        self.combustible_maximo = combustible_maximo

    def arrancar(self):
        if self.motor:
            print("Se escucha un molesto sonido al girar la llave. El motor ya estaba arrancado.")
        else:
            print("Se ha arrancado el motor. Ruge como un león.")
    
    def detener(self):
        if self.motor:
            print("Se detiene el motor.")
        else:
            print("No puedes parar el motor, porque ya está apagado. ¿No lo oyes?")

    def consulta_precio(self):
        print(f"El precio de la motocicleta {self.marca} {self.modelo} es de {self.precio} $.")

    def comprobar_deposito(self):
        print(f" Deposito de {self.marca} {self.modelo}")
        print(f"El depósito contiene {self.combustible_litros} litros.")
        print(f"La capacidad máxima es de {self.combustible_maximo}.")
        print(f"Faltan {self.combustible_maximo - self.combustible_litros} litros para llenar.")
        print("\n")
    
    def repostar(self):
        while True:
            self.repostar_litros = float(input("Introduzca la cantidad de litros a repostar:\n"))
            
            if self.combustible_litros + self.repostar_litros <= self.combustible_maximo:
                print("Repostaje exitoso.")
                print(f"Se han repostado {self.repostar_litros} litros.")
                self.combustible_litros += self.repostar_litros 
                print(f"El depósito tiene {self.combustible_litros} litros.")
                break
            else:
                print("Excede el maximo de litros")

moto_1 = Motocicleta("Roja y blanca", "45663-FHDY", 10, 2, "Yamaha", "YZF-R1", "20/02/2020", 288, 199, 17)

moto_2 = Motocicleta(
    matricula="48659-FHEZ", 
    combustible_litros=0, 
    color="Negra", 
    marca="Harley Davidson", 
    modelo="Fat Boy",  
    numero_ruedas=2, 
    peso=304, 
    fecha_fabricacion="29/09/2020", 
    velocidad_punta=160,
    combustible_maximo=20
    )

moto_1.arrancar()
moto_1.detener()

print("----consultar desde fuera de class-----")
moto_1.precio = 27000
print(f'El precio de la motocicleta {moto_1.marca}{moto_1.modelo} es de {moto_1.precio}$')

print("----consultar desde dentro de class-----")
moto_1.consulta_precio()

print("-----------------------------------------------------------------------------")

moto_1.comprobar_deposito()
moto_2.comprobar_deposito()

moto_1.repostar()
print("moto_1 cargada con exito")
moto_2.repostar()
print("moto_2 cargada con exito")