# Clase que representa una casilla del tablero
from Nave import Nave


class Casilla:
    def __init__(self):
        """
        Constructor de la clase Casilla.

        Atributos:
            nave: Referencia a la nave que ocupa esta casilla (None si está vacía)
            visitada (bool): True si ya se ha disparado a esta casilla, False en caso contrario
        """
        self.nave: Nave = None
        self.visitada = False
