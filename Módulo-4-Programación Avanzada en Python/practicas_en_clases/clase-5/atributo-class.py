class Student:
    escuela_nombre = 'USACH'

    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

    @classmethod
    def cambiar_escuela(cls, _new_name):
         cls.escuela_nombre = _new_name

    def ver_nombre_escuela(self):
        print(Student.escuela_nombre)


student1 = Student("Juan", 20)

student1.ver_nombre_escuela()
student1.cambiar_escuela('Andres Bello')
student1.ver_nombre_escuela()