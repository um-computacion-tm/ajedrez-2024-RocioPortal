from chess.pieces import Piece

class Bishop(Piece):
    
    def is_valid_move(self, board, from_row, from_col, to_row, to_col):
        # El movimiento del alfil debe ser diagonal: la diferencia entre las filas y las columnas debe ser igual
        if abs(to_row - from_row) == abs(to_col - from_col):
            # Determina la dirección del movimiento
            row_step = 1 if to_row > from_row else -1
            col_step = 1 if to_col > from_col else -1
            
            # Recorre cada posición en la diagonal hasta la posición de destino
            row, col = from_row + row_step, from_col + col_step
            while row != to_row and col != to_col:
                # Si hay alguna pieza en el camino, el movimiento no es válido
                if board.get_piece(row, col) is not None:
                    return False
                row += row_step
                col += col_step

            # Si la casilla de destino está ocupada por una pieza del mismo color, el movimiento no es válido
            target_piece = board.get_piece(to_row, to_col)
            if target_piece is not None and target_piece.color == self.color:
                return False
            
            # Si no hay piezas en el camino y la casilla de destino no está ocupada por una pieza del mismo color, el movimiento es válido
            return True
        
        # Si el movimiento no es diagonal, no es válido
        return False
    