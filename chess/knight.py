from chess.pieces import Piece

class Knight(Piece):
    
    white_str = "♞"  
    black_str = "♘"

    def valid_positions(self, from_row, from_col, to_row, to_col):
        """
        La función verifica si un movimiento del caballo es válido.
        Funcionalidad:
        - Genera las direcciones posibles del movimiento del caballo en forma de "L".
        - Calcula las posiciones posibles a las que el caballo puede moverse desde la posición de origen.
        - Verifica si la posición destino está dentro de las posiciones válidas.
        Parámetros:
        from_row: Recibe la fila de la posición de origen.
        from_col: Recibe la columna de la posición de origen.
        to_row: Recibe la fila de la posición destino.
        to_col: Recibe la columna de la posición destino.
        Retorna:
        True si el movimiento es válido, False en caso contrario.        
        """
        directions = self.generate_knight_directions()
        possible_positions = self.possible_moves_general(from_row, from_col, directions, single_step=True)
        return (to_row, to_col) in possible_positions

    def generate_knight_directions(self):
        """
        La función genera las direcciones posibles del movimiento del caballo.
        Funcionalidad:
        - Crea todas las combinaciones posibles de movimientos en "L" del caballo (2 casillas en una dirección y 1 en otra).
        Retorna:
        Una lista de tuplas que representan las direcciones válidas para el movimiento del caballo.
        """
        moves = [2, 1, -1, -2]
        return [(i, j) for i in moves for j in moves if abs(i) != abs(j)]