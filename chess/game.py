from chess.board import Board
from chess.exceptions import InvalidMove, InvalidTurn, EmptyPosition, SelfCaptureException

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
        if len(self.__board__.pieces_from_black_piece) == 16:
            return "WHITE WINS"
        elif len(self.__board__.pieces_from_white_piece) == 16:
            return "BLACK WINS"
        else:
            return False
        

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

