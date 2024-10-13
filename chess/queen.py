from chess.pieces import Piece

class Queen(Piece):

    white_str = "♛"  
    black_str = "♕"
    
    def valid_positions(self, from_row, from_col, to_row, to_col, directions=None):
        '''
        La función verifica si una pieza reina puede moverse a una posición dada.
        Funcionalidad:
        - Verifica si se han proporcionado direcciones de movimiento. Si no se proporcionan, usa las direcciones estándar para la reina (movimientos ortogonales y diagonales).
        - Calcula las posiciones posibles a las que la reina puede moverse desde la posición de origen.
        - Determina si la posición destino está dentro de las posiciones válidas.
        Parámetros:
        from_row: Recibe la fila de la posición de origen.
        from_col: Recibe la columna de la posición de origen.
        to_row: Recibe la fila de la posición destino.
        to_col: Recibe la columna de la posición destino.
        directions (opcional): Direcciones posibles de movimiento. Si no se pasa, usa las direcciones predeterminadas de la reina.
        Retorna:
        True si el movimiento es válido, False en caso contrario.
        '''
        if directions is None:
            directions = self.__king_queen_directions__
        possible_positions = self.possible_moves_general(from_row, from_col, directions, single_step=False)
        return (to_row, to_col) in possible_positions