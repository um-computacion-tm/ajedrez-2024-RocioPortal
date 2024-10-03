from chess.pieces import Piece

class Knight(Piece):
    
    white_str = "♞"  
    black_str = "♘"

    def valid_positions(self, from_row, from_col, to_row, to_col):
        # Movimientos en forma de "L"
        knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                        (1, 2), (1, -2), (-1, 2), (-1, -2)]
        possible_positions = self.possible_moves_general(from_row, from_col, knight_moves, single_step=True)
        return (to_row, to_col) in possible_positions