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


    def check_winner(self):
        white_pieces = 0
        black_pieces = 0
        
        # Recorre el tablero y cuenta las piezas de cada color
        for row in self.__board__.__positions__:
            for piece in row:
                if piece is not None:
                    if piece.get_color == "WHITE":
                        white_pieces += 1
                    elif piece.get_color == "BLACK":
                        black_pieces += 1

        # Verifica si alguno de los jugadores se ha quedado sin piezas
        if white_pieces == 0:
            return "BLACK WINS"
        elif black_pieces == 0:
            return "WHITE WINS"
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

