from chess.pieces import Piece

class Queen(Piece):

    
    def __str__(self):  #devuelve el simbolo de la torre segun el color de la pieza
      if self.__color__ == "WHITE":
          return "♛"
      else:
         return "♕"    
      

    def valid_positions(self, from_row, from_col, to_row, to_col):
        # Movimientos ortogonales y diagonales
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),   # Ortogonales
                      (1, 1), (-1, -1), (1, -1), (-1, 1)] # Diagonales
        possible_positions = self.possible_moves_general(from_row, from_col, directions, single_step = False)
        return (to_row, to_col) in possible_positions