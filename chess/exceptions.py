#Aca lanzamos las excepciones y las atrapamos en el cli 

class InvalidMove(Exception):
    """
    La clase `InvalidMove` es una excepción general que se lanza cuando un movimiento de pieza es inválido.
    Funcionalidad:
    - Muestra un mensaje de error predeterminado indicando que el movimiento es inválido.
    """
    message = "Movimieto de pieza invalido"
    def __str__(self):
        return self.message

class InvalidTurn(InvalidMove):
    """
    La clase `InvalidTurn` es una excepción que se lanza cuando un jugador intenta mover una pieza del oponente.
    Funcionalidad:
    - Hereda de `InvalidMove`.
    - Muestra un mensaje indicando que no se puede mover una pieza del otro jugador.
    """
    message = "No puedes mover pieza de otro jugador"

class EmptyPosition(InvalidMove):
    """
    La clase `EmptyPosition` es una excepción que se lanza cuando se intenta mover desde una casilla vacía.
    Funcionalidad:
    - Hereda de `InvalidMove`.
    - Muestra un mensaje indicando que la posición está vacía.
    """
    message = "La posicion esta vacia"

class OutOfBoard(InvalidMove):
    """
    La clase `OutOfBoard` es una excepción que se lanza cuando se intenta mover a una casilla fuera de los límites del tablero.
    Funcionalidad:
    - Hereda de `InvalidMove`.
    - Muestra un mensaje indicando que la posición está fuera del tablero.
    """
    message = "La posicion indicada se encuentra fuera del tablero"

class SelfCaptureException(InvalidMove):
    """
    La clase `SelfCaptureException` es una excepción que se lanza cuando un jugador intenta capturar su propia pieza.
    Funcionalidad:
    - Hereda de `InvalidMove`.
    - Muestra un mensaje indicando que no se pueden capturar las propias piezas.
    """
    message = "No puedes capturar tus propias piezas."

class InvalidCoordinateInputError(InvalidMove):
    """
    La clase `InvalidCoordinateInputError` es una excepción que se lanza cuando las coordenadas ingresadas no son válidas.
    Funcionalidad:
    - Hereda de `InvalidMove`.
    - Muestra un mensaje indicando que las coordenadas deben ser números.
    """
    message = "Las coordenadas deben ser números."

class GameOverException(Exception):
    """
    La clase `GameOverException` es una excepción que se lanza cuando el juego ha finalizado.
    Funcionalidad:
    - Permite la personalización del mensaje de error al finalizar el juego.
    - Muestra un mensaje predeterminado o personalizado cuando se termina la partida.
    """
    def __init__(self, message="El juego ha finalizado"):
        super().__init__(message)