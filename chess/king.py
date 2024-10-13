from chess.pieces import Piece

class King(Piece):
    
    white_str = "♚"  
    black_str = "♔"
      
    def valid_positions(self, from_row, from_col, to_row, to_col):
        '''
        La función verifica si un movimiento del rey es válido.
        Funcionalidad:
        - Calcula las posiciones posibles a las que el rey puede moverse desde la posición de origen.
        - El rey solo puede moverse una casilla en cualquier dirección, por lo que se usa `single_step=True`.
        - Verifica si la posición destino está dentro de las posiciones válidas.
        Parámetros:
        from_row: Recibe la fila de la posición de origen.
        from_col: Recibe la columna de la posición de origen.
        to_row: Recibe la fila de la posición destino.
        to_col: Recibe la columna de la posición destino.
        Retorna:
        True si el movimiento es válido, False en caso contrario.
        '''
        # single_step=True porque el rey solo se mueve una casilla en cualquier dirección
        possible_positions = self.possible_moves_general(from_row, from_col, self.__king_queen_directions__, single_step=True)
        return (to_row, to_col) in possible_positions