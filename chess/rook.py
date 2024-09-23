from chess.pieces import Piece

class Rook(Piece):
    
    white_str = "♜"
    black_str = "♖"

    def valid_positions(self, from_row, from_col, to_row, to_col):
        # Movimientos ortogonales: arriba, abajo, izquierda, derecha
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        possible_positions = self.possible_moves_general(from_row, from_col, directions)
        return (to_row, to_col) in possible_positions


