from chess.pieces import Piece

class Pawn(Piece):
    
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