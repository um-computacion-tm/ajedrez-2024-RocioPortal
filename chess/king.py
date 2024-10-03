from chess.pieces import Piece

class King(Piece):
    
    white_str = "♚"  
    black_str = "♔"
      
    def valid_positions(self, from_row, from_col, to_row, to_col):

        # single_step=True porque el rey solo se mueve una casilla en cualquier dirección
        possible_positions = self.possible_moves_general(from_row, from_col, self.__king_queen_directions__, single_step=True)
        return (to_row, to_col) in possible_positions