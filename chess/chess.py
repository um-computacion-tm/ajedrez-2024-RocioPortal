from chess.board import Board
from chess.exceptions import InvalidMove, InvalidTurn, EmptyPosition
import sys

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
        if not piece.valid_positions(from_row, from_col, to_row, to_col):
            raise InvalidMove()
        self.__board__.move(from_row, from_col, to_row, to_col)
        self.change_turn()


    # Usuario elige terminan o no la partida (ofrece empate)

    def offer_draw(self):
        import sys
        print("¿Quiere terminar la partida? (si/no)")
        user_input = input().strip().lower()
        if user_input == "si":
            print("Su partida ha sido terminada, gracias por jugar!")
            return self.finish()
        else:
            print("Su partida continúa.")
            return True
        
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
