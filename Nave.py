class Nave:
    """
    Clase que crea una nave con sus parametros, ademas tiene metodos "recibir_disparo" y "restar_vida" 
    """

    def __init__(self, nombre, tipo, tamano):
        self.nombre = nombre
        self.vida = tamano
        self.tipo = tipo
        self.estado = "Escondida"

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            self.__nombre = ""
            raise TypeError(f"{nombre} no tiene el tipo correcto")

    @property
    def vida(self):
        return self.__tamano

    @vida.setter
    def vida(self, tamano):
        if isinstance(tamano, int):
            self.__tamano = tamano
        else:
            self.__tamano = 0
            raise TypeError(f"{tamano} no tiene el tipo correcto")

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        if not isinstance(tipo, str):
            raise TypeError("Tipo debe ser una cadena de texto")
        self.__tipo = tipo

    def restar_vida(self):
        self.vida -= 1
        return self.vida

    def recibir_disparo(self):
        self.restar_vida()
        if self.vida > 0:
            self.estado = "Tocado"
        else:
            self.estado = "Hundido"
        return self.estado

    def __repr__(self):

        return f"{self.nombre}-{self.tipo}-{self.vida}"
