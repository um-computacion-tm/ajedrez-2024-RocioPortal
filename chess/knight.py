from chess.pieces import Piece

class Knight(Piece):
    ...

    def __str__(self):  #devuelve el simbolo de la torre segun el color de la pieza
      if self.__color__ == "WHITE":
          return "♞"
      else:
         return "♘" 


    def valid_positions(self, from_row, from_col, to_row, to_col):
        possible_positions = self.possible_positions_knight(from_row, from_col)
        return (to_row, to_col) in possible_positions

    def possible_positions_knight(self, row, col):
        possibles = []
        knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                        (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for move in knight_moves:
            next_row, next_col = row + move[0], col + move[1]
            if 0 <= next_row < 8 and 0 <= next_col < 8:
                other_piece = self.__board__.get_piece(next_row, next_col)
                if other_piece is None or other_piece.get_color != self.get_color:
                    possibles.append((next_row, next_col))
        return possibles