from chess.pieces import Piece

class Knight(Piece):
    ...

    def __str__(self):  #devuelve el simbolo de la torre segun el color de la pieza
      if self.__color__ == "WHITE":
          return "♘"
      else:
         return "♞" 