class Persona():

	def __init__(self,dni,nombre,edad):
		self.dni=dni
		self.nombre=nombre
		self.edad=edad

	@property
	def dni(self):
		return self._dni

	@dni.setter
	def dni(self,dni):
		self._dni=dni

	@property
	def nombre(self):
		return self._nombre

	@nombre.setter
	def nombre(self,nombre):
		self._nombre=nombre	

	@property
	def edad(self):
		return self._edad

	@edad.setter
	def edad(self,edad):
		if edad>0:
			self._edad=edad	
		else:
			raise ValueError("Edad incorrecta")

	def __str__(self):
		return self.dni.__str__()+" "+self.nombre+" ("+str(self.edad)+")"

class Notas():

	def __init__(self):
		self._notas={}

	
	@property
	def notas(self):
		resultado=""
		for key,value in self._notas.items():
			resultado+=key+":"+str(value)+"\n"
		return resultado

	def addnotas(self,asig,nota):
		self._notas[asig]=nota

	def modnota(self,asig,nota):
		if asig in self._notas.keys():
			self._notas[asig]=nota
		else:
			raise ValueError("Asignatura incorrecta")

	def delnota(self,asig):
		if asig in self._notas.keys():
			del self._notas[asig]
		else:
			raise ValueError("Asignatura incorrecta")

	def media(self):
		return sum(self._notas.values())/len(self._notas.values())

	def __str__(self):
		resultado=""
		for key,value in self._notas.items():
			resultado+=key+":"+str(value)+"\n"
		return resultado

class Dni():

	def __init__(self,numero):
		self.numero=numero

	def __calcular_letra(self):
		letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
		return letras[int(self.numero)%23]

	@property
	def numero(self):
		return self._numero

	@numero.setter
	def numero(self,numero):
		if len(numero)==8 and numero.isdigit():
			self._numero = numero
			self._letra = self.__calcular_letra()
		else: 
			raise ValueError("DNI incorecto")


	@property
	def letra(self):
		return self._letra

	def __str__(self):
		return "{0}-{1}".format(self.numero,self.letra)
	
class Alumno(Persona,Notas):

	def __init__(self,dni,nombre,edad):
		Persona.__init__(self,dni,nombre,edad)
		Notas.__init__(self)

	def __str__(self):
		return Persona.__str__(self)+"\n"+Notas.__str__(self)