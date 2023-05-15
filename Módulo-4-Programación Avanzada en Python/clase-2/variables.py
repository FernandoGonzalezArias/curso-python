class Alumno:
    #variable de clase
    semestre = 1,
    asignaturas = ["Python", "Javascript", "Base de Datos"]

    def __init__(self, _name):
        #variable instancia
        self.name = _name
        self.asignatura = ""
        self.notas = []

    def incribir_asignatura(self, _asignatura):
        self.asignatura = _asignatura

    def registrar_notas(self, _nota):
        self.notas.append(_nota) # [4, 5.6, 7, 9]

    def obtener_promedio(self):
        promedio = sum(self.notas)/len(self.notas)
        print(f'El promedio de notas de {self.name} es: {promedio}')
    


alumno1 = Alumno("Marysabel")
alumno2 = Alumno("Maria Jose")
alumno3 = Alumno("Maria Fernanda")

print(f'alumno1: {alumno1.name} --- alumno2: {alumno2.name} --- alumno3: {alumno3.name}')
print(f'semestre alumno1: {alumno1.semestre} --- semestre alumno2: {alumno2.semestre} --- semestre alumno3: {alumno3.semestre}')

alumno2.semestre = 2
print(f'semestre alumno1: {alumno1.semestre} --- semestre alumno2: {alumno2.semestre} --- semestre alumno3: {alumno3.semestre}')

Alumno.semestre = 3
print(f'semestre alumno1: {alumno1.semestre} --- semestre alumno2: {alumno2.semestre} --- semestre alumno3: {alumno3.semestre}')


alumno1.incribir_asignatura("Python")

