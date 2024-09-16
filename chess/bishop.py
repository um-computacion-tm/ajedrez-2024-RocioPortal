from chess.pieces import Piece

class Bishop(Piece):
    white_str = "♝"  
    black_str = "♗"

    def valid_positions(self, from_row, from_col, to_col, to_row):
      
      possible_diagonal_positions = (
         self.possible_positions_dai(from_row, from_col)+ #Diagonal ascendente izquierda
         self.possible_positions_dad(from_row, from_col)+ #Diagonal ascendente derecha
         self.possible_positions_ddi(from_row, from_col)+ #Diagonal descendente izquierda
         self.possible_positions_ddd(from_row, from_col)  #Diagonal desscendente derecha
      )
      return (to_row, to_col) in possible_diagonal_positions
   

















