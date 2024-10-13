from chess.pieces import Piece

class Bishop(Piece):
    '''
    La clase Bishop representa el alfil en el juego de ajedrez.
    Hereda de la clase Piece.
    '''
    white_str = "♝"  
    black_str = "♗"

    def valid_positions(self, from_row, from_col, to_row, to_col):
        '''
        La función determina si una posición de destino es válida para el alfil.
        Funcionalidad:
        Los movimientos válidos del alfil son diagonales en todas las direcciones.
        Se generan las posiciones posibles a las que puede moverse el alfil desde la posición inicial.
        Parámetros:
        from_row: Fila de la posición inicial.
        from_col: Columna de la posición inicial.
        to_row: Fila de la posición de destino.
        to_col: Columna de la posición de destino.
        Retorna:
        `True` si la posición de destino está dentro de las posiciones válidas, de lo contrario, `False`.
        '''
        # Movimientos diagonales
        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        possible_positions = self.possible_moves_general(from_row, from_col, directions)
        return (to_row, to_col) in possible_positions

   

















