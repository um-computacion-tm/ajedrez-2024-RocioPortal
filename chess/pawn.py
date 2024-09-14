from chess.pieces import Piece

class Pawn(Piece):

    def __str__(self):  #devuelve el simbolo de la torre segun el color de la pieza
      if self.__color__ == "WHITE":
          return "♟"
      else:
         return "♙" 
    

    def get_possible_positions(self, from_row, from_col):
        possibles = self.get_possible_positions_move(
            from_row,
            from_col,
        )
        possibles.extend(
            self.get_possible_positions_eat(from_row, from_col)
        )
        return possibles

    def get_possible_positions_eat(self, from_row, from_col):
        if self.__color__ == "BLACK":
            other_piece = self.__board__.get_piece(from_row + 1, from_col + 1)
            if other_piece and other_piece.__color__ == "WHITE":
                return [(from_row + 1, from_col + 1)]

        return []

    def get_possible_positions_move(self, from_row, from_col):
        if self.__color__ == "BLACK":
            if self.__board__.get_piece(from_row + 1, from_col) is None:
                if (
                    from_row == 1 and
                    self.__board__.get_piece(from_row + 2, from_col) is None
                ):
                    return [
                        (from_row + 1, from_col),
                        (from_row + 2, from_col)
                    ]
                else:
                    return [
                        (from_row + 1, from_col),
                    ]
        else:
            if from_row == 6:
                return [
                    (from_row - 1, from_col),
                    (from_row - 2, from_col)
                ]
            else:
                if self.__board__.get_piece(from_row - 1, from_col) is None:
                    return [
                        (from_row - 1, from_col),
                    ]
                else:
                    return []
        return []


    '''
    def is_valid_move(self, board, from_row, from_col, to_row, to_col):
        # Movimiento vertical básico
        direction = 1 if self.color == "WHITE" else -1
        start_row = 6 if self.color == "WHITE" else 1

        # Movimiento de un solo paso hacia adelante
        if from_col == to_col:
            if (to_row - from_row) == direction and board.get_piece(to_row, to_col) is None:
                return True
            # Movimiento de dos pasos desde la posición inicial
            if (from_row == start_row and (to_row - from_row) == 2 * direction and
                    board.get_piece(to_row, to_col) is None and
                    board.get_piece(from_row + direction, to_col) is None):
                return True
            
        # Movimiento en diagonal
        if abs(from_col - to_col) == 1 and (to_row - from_row) == direction:
            target_piece = board.get_piece(to_row, to_col)
            if target_piece is not None and target_piece.color != self.color:
                return True
        
        return False

    '''