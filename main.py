# from Juego import Juego
# Tarea: Diagrama de Secuencia
# Funcionalidad: El Disparo

# Objetivo
# Como queremos entender la interacción dinámica de nuestro sistema, debemos modelar el flujo de un ataque. El objetivo es visualizar cómo el mensaje "disparar" viaja desde el jugador hasta la nave afectada.
# Escenario de la Tarea
# Debemos representar el siguiente flujo lógico:
# El Usuario introduce unas coordenadas (X, Y) en la interfaz.
# El objeto :Juego recibe estas coordenadas y le pide al :Tablero que procese el disparo.
# El :Tablero busca la correspondiente a esa posición.
# El :Tablero le ordena a la :Casilla que reciba el impacto.
# La :Casilla verifica si tiene una :Nave asignada.
# Si hay una nave,llama al método recibir_disparo() de la :Nave.
# La :Nave calcula su vida restante y responde si ha sido hundida.
# La respuesta (Agua, Tocado o Hundido) vuelve hacia atrás hasta llegar al Usuario.
# Elementos que debemos utilizar
# Actor: Usuario (Jugador).
# Líneas de Vida: :Juego, :Tablero, :Nave.
# Mensajes Principales:
# lanzar_ataque(x, y)
# gestionar_disparo(x, y)
# recibir_impacto()
# restar_vida()


from Tablero import Tablero
from Nave import Nave
from Juego import Juego

if __name__ == '__main__':
    n1 = Nave("nave1", 3)

    t1 = Tablero()
    t1.colocar_nave(n1)
    print(t1)
