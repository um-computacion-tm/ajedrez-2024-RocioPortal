from chess.pieces import Piece

class King(Piece):
    
    white_str = "♚"  
    black_str = "♔"
      
    def valid_positions(self, from_row, from_col, to_row, to_col):
        # El rey puede moverse una casilla en cualquier dirección (ortogonal o diagonal)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),   # Movimientos ortogonales
                      (1, 1), (-1, -1), (1, -1), (-1, 1)] # Movimientos diagonales
                      
        # single_step=True porque el rey solo se mueve una casilla en cualquier dirección
        possible_positions = self.possible_moves_general(from_row, from_col, directions, single_step=True)
        return (to_row, to_col) in possible_positions