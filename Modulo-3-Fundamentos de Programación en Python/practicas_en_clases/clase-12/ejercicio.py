# se necesita realizar un programa basado en clases que permita automatizar el torniquete (control de acceso)
# de una micro, de la siguiente manera

#     1 Las personas que aboradan la micro son, mujeres, hombres, niños y aduto mayor, de los cuales los niños no pagan y lso adultos mayores pagan la tarifa
#       el 50%
    
#     2 el cobro actual de la micro es de 730 pesos

#     3 por lo que necesitamos un reporte de operacion por dia donde, por micro (cada micro se reguistra por patente), se listen los tipos de usuario y la cantidad total recaudad por 
#       cada, anexar a este reporte el total por dia

#     4. seria interesante que apart6e del reporte anterior que estotal, tener uno filtrado por dia y otro filtrado por persona

class Usuario:
    def __init__(self, nombre, tipo, fecha):
        self.nombre = nombre
        self.tipo = tipo
        self.fecha = fecha

class Torniquete:
    def __init__(self, patente, precio):
        self.patente = patente
        self.precio = precio
        self.usuarios = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def reporte_por_micro(self):
        print(f"Reporte por micro {self.patente}:")
        tipos_usuarios = {"mujer": 0, "hombre": 0, "nino": 0, "adulto mayor": 0}
        total = 0
        for usuario in self.usuarios:
            tipos_usuarios[usuario.tipo] += 1
            if usuario.tipo == "nino":
                continue
            elif usuario.tipo == "adulto mayor":
                total += self.precio * 0.5
            else:
                total += self.precio
        for tipo, cantidad in tipos_usuarios.items():
            print(f"{tipo}: {cantidad}")
        print(f"Total recaudado: {total} pesos")

    def reporte_por_dia(self, fecha):
        print(f"Reporte por día {fecha} para la micro {self.patente}:")
        tipos_usuarios = {"mujer": 0, "hombre": 0, "nino": 0, "adulto mayor": 0}
        total = 0
        for usuario in self.usuarios:
            if usuario.fecha == fecha:
                tipos_usuarios[usuario.tipo] += 1
                if usuario.tipo == "nino":
                    continue
                elif usuario.tipo == "adulto mayor":
                    total += self.precio * 0.5
                else:
                    total += self.precio
        for tipo, cantidad in tipos_usuarios.items():
            print(f"{tipo}: {cantidad}")
        print(f"Total recaudado: {total} pesos")

    def reporte_por_persona(self, nombre):
        print(f"Reporte para la persona {nombre} en la micro {self.patente}:")
        total = 0
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                if usuario.tipo == "nino":
                    continue
                elif usuario.tipo == "adulto mayor":
                    total += self.precio * 0.5
                else:
                    total += self.precio
        print(f"Total recaudado por la persona {nombre}: {total} pesos")
        return total

print("--------------------------------------")
micro = Torniquete("ABC-123", 730)
print("--------------------------------------")
micro.agregar_usuario(Usuario("María", "mujer", "02-05-2023"))
micro.agregar_usuario(Usuario("Pedro", "hombre", "02-05-2023"))
micro.agregar_usuario(Usuario("Juan", "adulto mayor", "02-05-2023"))
micro.agregar_usuario(Usuario("Luisa", "nino", "02-05-2023"))
micro.agregar_usuario(Usuario("Ana", "mujer", "01-05-2023"))
micro.agregar_usuario(Usuario("Santiago", "hombre", "01-05-2023"))
micro.agregar_usuario(Usuario("José", "adulto mayor", "01-05-2023"))
micro.agregar_usuario(Usuario("María", "mujer", "01-05-2023"))
print("--------------------------------------")
micro.reporte_por_micro()
print("--------------------------------------")
micro.reporte_por_dia("01-05-2023")
print("--------------------------------------")
micro.reporte_por_persona("María")
print("--------------------------------------")

