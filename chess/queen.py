from chess.pieces import Piece

class Queen(Piece):

    white_str = "♛"  
    black_str = "♕"
    
    def valid_positions(self, from_row, from_col, to_row, to_col):
        # Movimientos ortogonales y diagonales
        
        possible_positions = self.possible_moves_general(from_row, from_col, self.__king_queen_directions__, single_step=False)
        return (to_row, to_col) in possible_positions