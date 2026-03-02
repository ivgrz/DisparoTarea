class Juego:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	@property
	def x(self):
		return self.__x
	@x.setter
	def x(self,x):
		if isinstance(x,int):
			self.__x = x
		else:
			self.__x = 0
	@property
	def y(self):
		return self._y
	@y.setter
	def y(self,y):
		if isinstance(y, int):
			self.__y = y
		else:
			self.__y = 0




	def lanzar_ataque(self):

