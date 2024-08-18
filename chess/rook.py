from pieces import Piece

class Rook(Piece):
    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        # Verifica si el movimiento es válido para una torre ya que si ambos son verdaderos significa que la fila y la columna 
        #estan cambiando, lo que indica un movimiento diagonal
        if from_row != to_row and from_col != to_col:
            return False
