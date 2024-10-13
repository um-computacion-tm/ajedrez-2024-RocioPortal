from chess.pieces import Piece

class Rook(Piece):
    
    white_str = "♜"
    black_str = "♖"

    def valid_positions(self, from_row, from_col, to_row, to_col):
        '''
        La función verifica si una pieza torre puede moverse a una posición dada.
        Funcionalidad:
        Obtiene las direcciones válidas de movimiento de la torre (movimientos ortogonales).
        Calcula las posibles posiciones a las que la torre puede moverse.
        Verifica si la posición destino está dentro de las posiciones válidas de movimiento.
        Parámetros:
        from_row: Recibe la fila de la posición de origen.
        from_col: Recibe la columna de la posición de origen.
        to_row: Recibe la fila de la posición destino.
        to_col: Recibe la columna de la posición destino.
        Retorna:
        True si el movimiento es válido, False en caso contrario.
        '''
        # Movimientos ortogonales: arriba, abajo, izquierda, derecha
        directions = self.get_rook_directions()
        possible_positions = self.possible_moves_general(from_row, from_col, directions)
        return (to_row, to_col) in possible_positions

    def get_rook_directions(self):
        '''
        La función retorna las direcciones en las que una torre puede moverse.
        Funcionalidad:
        Devuelve una lista de tuplas que representan los movimientos ortogonales permitidos para la torre:
        arriba, abajo, izquierda y derecha.
        Retorna:
        Una lista de tuplas con las direcciones permitidas.
        '''
        # Movimientos ortogonales: arriba, abajo, izquierda, derecha
        return [(1, 0), (-1, 0), (0, -1), (0, 1)]

