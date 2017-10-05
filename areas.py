class Areas(object):
	def __init__(self):
		self.area = 0
		self.pi = 3.1416

	def areaCuadrado(self, lado):
		self.area = lado * lado

	def areaRectangulo(self, base, altura):
		self.area = base * altura	

	def areaCirculo(self, radio):	
		self.area = self.pi*(radio**2)

	def areaTrapecio(self, a, b, h):
		self.area = (a+b)/2			

	def obtener_area(self):
		return self.area	