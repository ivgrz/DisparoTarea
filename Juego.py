from Nave import Nave
from Tablero import Tablero


class Juego:
    def __init__(self):
        self.tablero = Tablero()
        self.inicializar_naves()

    def inicializar_naves(self):
        """
        Crea e inicializa todas las naves del juego.
        Coloca las naves en el tablero en posiciones predefinidas.
        """
        por1 = Nave("Enterprise", "portaaviones", 5)

        fra1 = Nave("Bismarck", "fragata", 3)
        fra2 = Nave("Prince of Wales", "fragata", 3)
        fra3 = Nave("Graf Spee", "fragata", 3)

        sub1 = Nave("U-47", "submarino", 1)
        sub2 = Nave("U-96", "submarino", 1)
        sub3 = Nave("U-505", "submarino", 1)
        sub4 = Nave("U-534", "submarino", 1)

        self.tablero.colocar_nave(por1, 1, 1, "H")   # Enterprise: (1,1) a (1,5)
        self.tablero.colocar_nave(fra1, 3, 3, "V")   # Bismarck: (3,3) a (5,3)
        self.tablero.colocar_nave(fra2, 7, 1, "H")   # Prince of Wales: (7,1) a (7,3)
        self.tablero.colocar_nave(fra3, 9, 1, "H")   # Graf Spee: (9,1) a (9,3)
        self.tablero.colocar_nave(sub1, 4, 6, "H")   # U-47: (4,6)
        self.tablero.colocar_nave(sub2, 9, 9, "H")   # U-96: (9,9)
        self.tablero.colocar_nave(sub3, 7, 6, "H")   # U-505: (7,6)
        self.tablero.colocar_nave(sub4, 9, 5, "H")   # U-534: (9,5)

    def mostrar_resultado(self, resultado: int):
        """
        Muestra por pantalla el resultado de un disparo.

        Args:
            resultado (int): Resultado del disparo (AGUA=0, TOCADO=1, HUNDIDO=2)
        """
        if resultado == self.tablero.AGUA:
            print("Agua")
        elif resultado == self.tablero.TOCADO:
            print("Tocado")
        elif resultado == self.tablero.HUNDIDO:
            print("Hundido")

    def lanzar_ataque(self, x, y):
        """
        Ejecuta un disparo en las coordenadas indicadas.

        Args:
            x (int): Coordenada X del disparo
            y (int): Coordenada Y del disparo
        """
        print(f"Atacando a ({x}, {y})")
        resultado = self.tablero.comprobar_impacto(x, y)
        self.mostrar_resultado(resultado)


if __name__ == "__main__":

    juego = Juego()

    while True:
        print("---BIENVENIDO AL JUEGO---\n")
        print("1. Lanzar ataque\n")
        print("2. Salir")
        opcion = input("Elige una opcion: ")

        match opcion:
            case "1":
                x = int(input("Elige una fila (0-9): "))
                y = int(input("Elige una columna (0-9): "))
                juego.lanzar_ataque(x, y)
            case "2":
                print("Saliendo...")
                break
