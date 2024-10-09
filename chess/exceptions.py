#Aca lanzamos las excepciones y las atrapamos en el cli 

class InvalidMove(Exception):
    message = "Movimieto de pieza invalido"
    def __str__(self):
        return self.message

class InvalidTurn(InvalidMove):
    message = "No puedes mover pieza de otro jugador"

class EmptyPosition(InvalidMove):
    message = "La posicion esta vacia"

class OutOfBoard(InvalidMove):
    message = "La posicion indicada se encuentra fuera del tablero"

class SelfCaptureException(InvalidMove):
    message = "No puedes capturar tus propias piezas."

class GameOverException(Exception):
    def __init__(self, message="El juego ha finalizado"):
        super().__init__(message)