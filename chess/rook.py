from chess.pieces import Piece

class Rook(Piece):
    
    white_str = "♜"
    black_str = "♖"

    def valid_positions(self, from_row, from_col, to_row, to_col):
        # Movimientos ortogonales: arriba, abajo, izquierda, derecha
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        possible_positions = self.possible_moves_general(from_row, from_col, directions)
        return (to_row, to_col) in possible_positions























    '''
    def is_valid_move(self, from_row, from_col, to_row, to_col, board):
        # Verifica si el movimiento es válido para una torre ya que si ambos son verdaderos significa que la fila y la columna 
        #estan cambiando, lo que indica un movimiento diagonal
        if from_row != to_row and from_col != to_col:
            return False
        
        if from_row == to_row:  # Movimiento horizontal
            step = 1 if to_col > from_col else -1
            for col in range(from_col + step, to_col, step):
                if board.get_piece(from_row, col) is not None:
                    return False  #si hay una pieza bloqueando el camino devuelve false 


        if from_col == to_col:  # Movimiento vertical
            step = 1 if to_row > from_row else -1
            for row in range(from_row + step, to_row, step):
                if board.get_piece(row, from_col) is not None:
                    return False

        return True
        '''