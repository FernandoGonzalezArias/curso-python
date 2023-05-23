class Comuna:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculos = []
        self.duenos = []
        self.policias = []
        self.multas = []

    def registrar_vehiculo(self):
        print("Registro de Vehículo:")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        anio_fabricacion = int(input("Año de fabricación: "))
        motor = float(input("Motor (volumen en litros del cilindraje): "))
        combustible = input("Tipo de combustible: ")
        tipo = input("Tipo de automóvil: ")
        valor = float(input("Valor: "))
        num_puertas = int(input("Número de puertas: "))
        num_asientos = int(input("Cantidad de asientos: "))
        velocidad_maxima = int(input("Velocidad máxima: "))
        color = input("Color: ")
        tipo_carga = input("Tipo de carga: ")
        volumen_carga = float(input("Volumen de carga: "))
        tipo_licencia = input("Tipo de licencia: ")
        fecha_expedicion_licencia = input("Fecha de expedición de la licencia: ")
        fecha_vencimiento_licencia = input("Fecha de vencimiento de la licencia: ")
        rut_dueno = input("RUT del dueño: ")

        dueno = self.buscar_dueno(rut_dueno)
        if dueno is None:
            print("Dueño no encontrado. Registre el dueño antes de registrar el vehículo.")
            return

        vehiculo = Vehiculo(marca, modelo, anio_fabricacion, motor, combustible, tipo, valor, num_puertas,
                            num_asientos, velocidad_maxima, color, tipo_carga, volumen_carga, tipo_licencia,
                            fecha_expedicion_licencia, fecha_vencimiento_licencia, dueno)
        self.vehiculos.append(vehiculo)
        print("Vehículo registrado exitosamente.")

    def buscar_dueno(self, rut):
        for dueno in self.duenos:
            if dueno.rut == rut:
                return dueno
        return None

    def registrar_dueno(self):
        print("Registro de Dueño:")
        nombre = input("Nombre: ")
        rut = input("RUT: ")
        dueno = Dueno(nombre, rut)
        self.duenos.append(dueno)
        print("Dueño registrado exitosamente.")

    def registrar_policia(self):
        print("Registro de Policía:")
        nombre = input("Nombre: ")
        placa = input("Placa: ")
        policia = Policia(nombre, placa)
        self.policias.append(policia)
        print("Policía registrado exitosamente.")

    def poner_multa(self):
        print("Registro de Multa:")
        fecha = input("Fecha de la multa (DD/MM/AAAA): ")
        monto = float(input("Monto de la multa: "))

        print("Seleccione el tipo de multa:")
        print("1. Falta de documento del vehículo")
        print("2. Falta de documento del conductor")
        print("3. Exceso de velocidad")
        print("4. Conducir en estado de ebriedad")
        opcion = int(input("Opción: "))

        if opcion == 1:
            tipo_multa = "Falta de documento del vehículo"
        elif opcion == 2:
            tipo_multa = "Falta de documento del conductor"
        elif opcion == 3:
            tipo_multa = "Exceso de velocidad"
        elif opcion == 4:
            tipo_multa = "Conducir en estado de ebriedad"
        else:
            print("Opción inválida.")
            return

        print("Seleccione el vehículo al que se le impone la multa:")
        for i, vehiculo in enumerate(self.vehiculos):
            print(f"{i + 1}. {vehiculo.marca} {vehiculo.modelo} ({vehiculo.dueno.nombre})")
        opcion = int(input("Opción: "))

        if opcion < 1 or opcion > len(self.vehiculos):
            print("Opción inválida.")
            return

        vehiculo = self.vehiculos[opcion - 1]
        policia = self.seleccionar_policia()

        multa = Multa(fecha, monto, tipo_multa, vehiculo, policia)
        self.multas.append(multa)
        print("Multa registrada exitosamente.")

    def seleccionar_policia(self):
        print("Seleccione el policía que impone la multa:")
        for i, policia in enumerate(self.policias):
            print(f"{i + 1}. {policia.nombre}")
        opcion = int(input("Opción: "))

        if opcion < 1 or opcion > len(self.policias):
            print("Opción inválida.")
            return None

        return self.policias[opcion - 1]

    def consultar_multas_por_fecha(self):
        fecha = input("Ingrese la fecha para consultar las multas (DD/MM/AAAA): ")
        print("Multas registradas en la fecha", fecha + ":")

        multas_fecha = [multa for multa in self.multas if multa.fecha == fecha]
        if len(multas_fecha) == 0:
            print("No se encontraron multas en la fecha especificada.")
            return

        for multa in multas_fecha:
            print("Tipo de multa:", multa.tipo)
            print("Vehículo:", multa.vehiculo.marca, multa.vehiculo.modelo)
            print("Dueño:", multa.vehiculo.dueno.nombre)
            print("Monto:", multa.monto)
            print()

    def consultar_multas_por_vehiculo_o_dueno(self):
        print("Seleccione una opción:")
        print("1. Consultar multas por vehículo")
        print("2. Consultar multas por dueño")
        opcion = int(input("Opción: "))

        if opcion == 1:
            vehiculo = self.seleccionar_vehiculo()
            if vehiculo is not None:
                multas_vehiculo = [multa for multa in self.multas if multa.vehiculo == vehiculo]
                if len(multas_vehiculo) == 0:
                    print("No se encontraron multas para el vehículo especificado.")
                else:
                    print("Multas para el vehículo", vehiculo.marca, vehiculo.modelo + ":")
                    for multa in multas_vehiculo:
                        print("Fecha:", multa.fecha)
                        print("Tipo de multa:", multa.tipo)
                        print("Monto:", multa.monto)
                        print()
        elif opcion == 2:
            dueno = self.seleccionar_dueno()
            if dueno is not None:
                multas_dueno = [multa for multa in self.multas if multa.vehiculo.dueno == dueno]
                if len(multas_dueno) == 0:
                    print("No se encontraron multas para el dueño especificado.")
                else:
                    print("Multas para el dueño", dueno.nombre + ":")
                    for multa in multas_dueno:
                        print("Fecha:", multa.fecha)
                        print("Tipo de multa:", multa.tipo)
                        print("Vehículo:", multa.vehiculo.marca, multa.vehiculo.modelo)
                        print("Monto:", multa.monto)
                        print()
        else:
            print("Opción inválida.")

    def seleccionar_vehiculo(self):
        print("Seleccione el vehículo:")
        for i, vehiculo in enumerate(self.vehiculos):
            print(f"{i + 1}. {vehiculo.marca} {vehiculo.modelo} ({vehiculo.dueno.nombre})")
        opcion = int(input("Opción: "))

        if opcion < 1 or opcion > len(self.vehiculos):
            print("Opción inválida.")
            return None

        return self.vehiculos[opcion - 1]

    def seleccionar_dueno(self):
        print("Seleccione el dueño:")
        for i, dueno in enumerate(self.duenos):
            print(f"{i + 1}. {dueno.nombre}")
        opcion = int(input("Opción: "))

        if opcion < 1 or opcion > len(self.duenos):
            print("Opción inválida.")
            return None

        return self.duenos[opcion - 1]

    def mostrar_menu(self):
        while True:
            print("\n----- Parque Automotor de la Comuna", self.nombre, "-----")
            print("1. Registrar dueño")
            print("2. Registrar vehículo")
            print("3. Registrar policía")
            print("4. Poner multa")
            print("5. Consultar multas por fecha")
            print("6. Consultar multas por vehículo o dueño")
            print("0. Salir")
            opcion = int(input("Ingrese una opción: "))

            if opcion == 1:
                self.registrar_dueno()
            elif opcion == 2:
                self.registrar_vehiculo()
            elif opcion == 3:
                self.registrar_policia()
            elif opcion == 4:
                self.poner_multa()
            elif opcion == 5:
                self.consultar_multas_por_fecha()
            elif opcion == 6:
                self.consultar_multas_por_vehiculo_o_dueno()
            elif opcion == 0:
                break
            else:
                print("Opción inválida.")

class Vehiculo:
    def __init__(self, marca, modelo, anio_fabricacion, motor, combustible, tipo, valor, num_puertas,
                 num_asientos, velocidad_maxima, color, tipo_carga, volumen_carga, tipo_licencia,
                 fecha_expedicion_licencia, fecha_vencimiento_licencia, dueno):
        self.marca = marca
        self.modelo = modelo
        self.anio_fabricacion = anio_fabricacion
        self.motor = motor
        self.combustible = combustible
        self.tipo = tipo
        self.valor = valor
        self.num_puertas = num_puertas
        self.num_asientos = num_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.tipo_carga = tipo_carga
        self.volumen_carga = volumen_carga
        self.tipo_licencia = tipo_licencia
        self.fecha_expedicion_licencia = fecha_expedicion_licencia
        self.fecha_vencimiento_licencia = fecha_vencimiento_licencia
        self.dueno = dueno

class Dueno:
    def __init__(self, nombre, rut):
        self.nombre = nombre
        self.rut = rut

class Policia:
    def __init__(self, nombre, placa):
        self.nombre = nombre
        self.placa = placa

class Multa:
    def __init__(self, fecha, monto, tipo, vehiculo, policia):
        self.fecha = fecha
        self.monto = monto
        self.tipo = tipo
        self.vehiculo = vehiculo
        self.policia = policia


nombre_comuna = input("Ingrese el nombre de la comuna: ")
comuna = Comuna(nombre_comuna)


comuna.mostrar_menu()



       
