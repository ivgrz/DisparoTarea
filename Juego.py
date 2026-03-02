from Nave import Nave
from Tablero import Tablero


class Juego:
    def __init__(self):
        self.tablero = Tablero()
        self.naves = []
        self.inicializar_naves()

    def inicializar_naves(self):
        datos = [("Submarino", 1), ("Buque", 2), ("Portaaviones", 4)]
        for nombre, tamano in datos:
            for _ in range(2):
                nave = Nave(nombre, tamano)
                self.naves.append(nave)
                self.tablero.colocar_nave(nave)

    def lanzar_ataque(self, x, y):
        return self.tablero.gestionar_disparo(x, y)


if __name__ == "__main__":

    juego = Juego()

    while True:
        print("---BIENVENIDO AL JUEGO---\n")
        print("1. Ver Tablero\n")
        print("2. Lanzar ataque\n")
        print("3. Salir")
        opcion = input("Elige una opcion: ")

        match opcion:
            case "1":
                print(juego.tablero)
            case "2":
                x = int(input("Elige una fila: "))
                y = int(input("Elige una columna: "))
                print(juego.lanzar_ataque(x, y))
            case "3":
                print("Saliendo...")
                break
