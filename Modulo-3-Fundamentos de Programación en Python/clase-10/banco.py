class CuentaBancaria:
    def __init__(self, titular, numero, saldo_inicial=0.0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo_inicial
        self.movimientos = []

    def abonar(self, monto, fecha):
        self.saldo += monto
        self.movimientos.append(('Abono', fecha, monto, self.saldo))

    def retirar(self, monto, fecha):
        if monto > self.saldo:
            print('Error: Saldo insuficiente')
        else:
            self.saldo -= monto
            self.movimientos.append(('Retiro', fecha, monto, self.saldo))

    def imprimir_estado_cuenta(self):
        print(f'Estado de cuenta de la cuenta {self.numero} a nombre de {self.titular}:')
        print(f'Movimiento  Tipo Movimiento  Fecha Movimiento  Monto Movimiento  Saldo')
        for movimiento in self.movimientos:
            print(f'{self.movimientos.index(movimiento)+1:<11} {movimiento[0]:<15} {movimiento[1]:<17} {movimiento[2]:<17} {movimiento[3]}')

# Pedimos al usuario que ingrese los datos de la cuenta
titular = input('Ingrese el nombre del titular de la cuenta: ')
numero = input('Ingrese el número de la cuenta: ')
saldo_inicial = float(input('Ingrese el saldo inicial de la cuenta: '))

# Creamos la cuenta bancaria
cuenta1 = CuentaBancaria(titular, numero, saldo_inicial)

# Pedimos al usuario que ingrese los movimientos de la cuenta
while True:
    print('Ingrese un movimiento de la cuenta:')
    tipo_movimiento = input('Abono o Retiro? ')
    if tipo_movimiento.lower() == 'abono':
        monto = float(input('Ingrese el monto del abono: '))
        fecha = input('Ingrese la fecha del abono (en formato dd/mm/yyyy): ')
        cuenta1.abonar(monto, fecha)
    elif tipo_movimiento.lower() == 'retiro':
        monto = float(input('Ingrese el monto del retiro: '))
        fecha = input('Ingrese la fecha del retiro (en formato dd/mm/yyyy): ')
        cuenta1.retirar(monto, fecha)
    else:
        print('Error: Tipo de movimiento inválido')
    
    # Preguntamos al usuario si desea agregar otro movimiento
    respuesta = input('Desea agregar otro movimiento? (S/N) ')
    if respuesta.lower() == 'n':
        break

# Imprimimos el estado de cuenta final
cuenta1.imprimir_estado_cuenta()


