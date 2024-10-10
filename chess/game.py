from chess.board import Board
from chess.exceptions import InvalidMove, InvalidTurn, EmptyPosition, GameOverException, SelfCaptureException

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"  #inician las blancas


    def is_playing(self):
        return True

    def move(
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
       # validate coords
        piece = self.__board__.get_piece(from_row, from_col)
        if not piece:
            raise EmptyPosition()
        if not piece.get_color == self.__turn__:  
            raise InvalidTurn()
        if self.__board__.get_piece(to_row, to_col) and self.__board__.get_piece(to_row, to_col).get_color == self.__turn__:
            raise SelfCaptureException()  # Nueva excepción para evitar capturar tus propias piezas
        if not piece.valid_positions(from_row, from_col, to_row, to_col):
            raise InvalidMove()
        self.__board__.move(from_row, from_col, to_row, to_col)
        self.change_turn()


    def check_end_game(self):
        if not self.has_pieces("WHITE"):
            raise GameOverException("Las piezas blancas han perdido. El juego ha terminado.")
        elif not self.has_pieces("BLACK"):
            raise GameOverException("Las piezas negras han perdido. El juego ha terminado.")
        
    @property
    def turn(self):
        return self.__turn__
    
    def show_board(self):
        return str(self.__board__)

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"

    def get_board(self):
        return self.__board__

