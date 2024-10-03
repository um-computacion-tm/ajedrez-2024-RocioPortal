from chess.pieces import Piece

class Knight(Piece):
    
    white_str = "♞"  
    black_str = "♘"

    def valid_positions(self, from_row, from_col, to_row, to_col):
        """
        Determina si un movimiento de caballo es válido.
        """
        directions = self.generate_knight_directions()
        possible_positions = self.possible_moves_general(from_row, from_col, directions, single_step=True)
        return (to_row, to_col) in possible_positions

    def generate_knight_directions(self):
        """
        Genera las direcciones de movimiento posibles del caballo.
        """
        moves = [2, 1, -1, -2]
        return [(i, j) for i in moves for j in moves if abs(i) != abs(j)]