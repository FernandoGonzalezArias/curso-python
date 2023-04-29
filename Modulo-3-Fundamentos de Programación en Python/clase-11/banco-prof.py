class Banco:
    

    def __init__(self):
        self.cuentas = [] # guardar las cuentas y correlativos
        self.movimientos = [] #gurdar los movimientos

    def agregar_cuenta(self, _cuenta, _rut):
        self.cuentas.append({
            'numero_cuenta': _cuenta,
            'rut': _rut,
            'correlativo_movimiento': 1,
            'saldo': 0
        })

    def agregar_movimiento_for(self, _cuenta, _fecha, _tipo, _monto):
        for elemento in self.cuentas:
            if elemento['numero_cuenta'] == _cuenta:
                if _tipo == 'Retiro':
                    if elemento['saldo'] - _monto < 0:
                        print("saldo insuficiente")
                    else:
                        self.movimientos.append({
                            'numero_cuenta': _cuenta,
                            'correlativo_movimiento': elemento['correlativo_movimiento'],
                            'fecha': _fecha,
                            'tipo': _tipo,
                            'monto': _monto,
                            'saldo': elemento['saldo'] - _monto
                        })
                        elemento['saldo'] = elemento['saldo'] - _monto
                        elemento['correlativo_movimiento'] = elemento['correlativo_movimiento'] + 1
                else:
                    self.movimientos.append({
                        'numero_cuenta': _cuenta,
                        'correlativo_movimiento': elemento['correlativo_movimiento'],
                        'fecha': _fecha,
                        'tipo': _tipo,
                        'monto': _monto,
                        'saldo': elemento['saldo'] + _monto
                    })
                    elemento['saldo'] = elemento['saldo'] + _monto
                    elemento['correlativo_movimiento'] = elemento['correlativo_movimiento'] + 1
                break
    
    def estado_cuenta(self, _cuenta):
        movimientos_cuenta = list(filter(lambda elementos: elementos['numero_cuenta'] == _cuenta, self.movimientos))
        print("{:<20}".format(" Nº Mvto."),  "{:<20}".format("Fecha"),   "{:<20}".format("Tipo"),   "{:<20}".format("Monto"),  "{:<20}".format("Saldo"))
        for elemento in movimientos_cuenta:
            print("{:<20}".format(elemento['correlativo_movimiento']),  "{:<20}".format(elemento['fecha']),   "{:<20}".format(elemento['tipo']),   "{:<20}".format(elemento['monto']),  "{:<20}".format(elemento['saldo']))

    


    

banco_bci = Banco()

banco_bci.agregar_cuenta("7360001", "14.999.000-1")
banco_bci.agregar_cuenta("7360002", "14.999.000-2")
banco_bci.agregar_cuenta("7360003", "14.999.000-3")
banco_bci.agregar_cuenta("7360004", "15.999.000-4")

banco_bci.agregar_movimiento_for("7360001", "17/04/2023", "Abono", 1000)
banco_bci.agregar_movimiento_for("7360001", "17/04/2023", "Abono", 500)
banco_bci.agregar_movimiento_for("7360001", "17/04/2023", "Retiro", 100)
banco_bci.agregar_movimiento_for("7360001", "17/04/2023", "Abono", 1000)
banco_bci.agregar_movimiento_for("7360001", "17/04/2023", "Retiro", 500)

banco_bci.agregar_movimiento_for("7360002", "17/04/2023", "Abono", 3000)
banco_bci.agregar_movimiento_for("7360002", "17/04/2023", "Abono", 100)
banco_bci.agregar_movimiento_for("7360002", "17/04/2023", "Retiro", 750)

banco_bci.agregar_movimiento_for("7360003", "17/04/2023", "Abono", 5000)


banco_bci.estado_cuenta("7360001")