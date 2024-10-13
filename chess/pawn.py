from chess.pieces import Piece
from chess.queen import Queen

class Pawn(Piece):
    
    white_str = "♟"  
    black_str = "♙"

    def valid_positions(self, from_row, from_col, to_row, to_col):
        '''
        La función verifica si un movimiento del peón es válido.
        Funcionalidad:
        - Obtiene las posiciones posibles a las que el peón puede moverse o capturar desde la posición de origen.
        - Verifica si la posición destino está dentro de las posiciones válidas calculadas.
        Parámetros:
        from_row: Recibe la fila de la posición de origen.
        from_col: Recibe la columna de la posición de origen.
        to_row: Recibe la fila de la posición destino.
        to_col: Recibe la columna de la posición destino.
        Retorna:
        True si el movimiento es válido, False en caso contrario.
        '''
        # Obtener posibles movimientos y capturas
        possible_positions = self.get_possible_moves(from_row, from_col)
        return (to_row, to_col) in possible_positions

    def get_possible_moves(self, from_row, from_col):
        '''
        La función calcula los posibles movimientos y capturas del peón.
        Funcionalidad:
        - Obtiene la dirección de movimiento del peón según su color.
        - Calcula los movimientos hacia adelante (incluyendo el doble movimiento desde la fila inicial).
        - Calcula las posibles capturas diagonales.
        Parámetros:
        from_row: Recibe la fila de la posición de origen.
        from_col: Recibe la columna de la posición de origen.
        Retorna:
        Una lista de tuplas con las posiciones posibles a las que el peón puede moverse o capturar.
        '''
        moves = []
        direction = self.get_move_direction()  # Obtener dirección según el color
        start_row = self.get_start_row()       # Obtener fila inicial según el color

        # Movimientos hacia adelante
        self.add_forward_moves(from_row, from_col, direction, start_row, moves)

        # Capturas diagonales
        self.add_capture_moves(from_row, from_col, direction, moves)

        return moves

    def add_forward_moves(self, from_row, from_col, direction, start_row, moves):
        '''
        La función añade los movimientos hacia adelante del peón.
        Funcionalidad:
        - Añade un movimiento hacia adelante si la casilla está vacía.
        - Si el peón está en su fila inicial, añade un movimiento de dos casillas si ambas están vacías.
        Parámetros:
        from_row: Fila de la posición de origen del peón.
        from_col: Columna de la posición de origen del peón.
        direction: Dirección de movimiento del peón (arriba o abajo).
        start_row: Fila inicial del peón según su color.
        moves: Lista donde se añaden los movimientos posibles.
        '''
        # Movimiento hacia adelante si está vacío
        if self.is_empty(from_row + direction, from_col):
            moves.append((from_row + direction, from_col))

            # Si está en la fila inicial, puede avanzar dos casillas
            if from_row == start_row and self.is_empty(from_row + 2 * direction, from_col):
                moves.append((from_row + 2 * direction, from_col))

    def add_capture_moves(self, from_row, from_col, direction, moves):
        '''
        La función añade los movimientos de captura en diagonal del peón.
        Funcionalidad:
        - Calcula las posibles capturas diagonales en las dos direcciones (izquierda y derecha).
        - Si la casilla está dentro del tablero y contiene una pieza del oponente, se añade como una captura válida.
        Parámetros:
        from_row: Fila de la posición de origen del peón.
        from_col: Columna de la posición de origen del peón.
        direction: Dirección de movimiento del peón (arriba o abajo).
        moves: Lista donde se añaden los movimientos de captura posibles.
        '''
        capture_moves = [(direction, -1), (direction, 1)]
        for move in capture_moves:
            next_row, next_col = from_row + move[0], from_col + move[1]
            if self.is_in_bounds(next_row, next_col) and self.can_capture(next_row, next_col):
                moves.append((next_row, next_col))

    def get_move_direction(self):
        '''
        La función obtiene la dirección de movimiento del peón.
        Funcionalidad:
        - Si el peón es blanco, su dirección es hacia arriba (-1).
        - Si el peón es negro, su dirección es hacia abajo (1).
        Retorna:
        La dirección de movimiento del peón como un entero (-1 o 1).
        '''
        # Retorna la dirección de movimiento según el color
        return -1 if self.__color__ == 'WHITE' else 1

    def get_start_row(self):
        '''
        La función obtiene la fila inicial del peón según su color.
        Funcionalidad:
        - Si el peón es blanco, su fila inicial es 6.
        - Si el peón es negro, su fila inicial es 1.
        Retorna:
        La fila inicial del peón como un entero (6 o 1).
        '''
        return 6 if self.__color__ == 'WHITE' else 1

    def is_in_bounds(self, row, col):
        '''
        La función verifica si una posición está dentro de los límites del tablero.
        Funcionalidad:
        - Verifica si la fila y la columna están dentro del rango válido (0 a 7).
        Parámetros:
        row: Fila a verificar.
        col: Columna a verificar.
        Retorna:
        True si la posición está dentro de los límites, False en caso contrario.
        '''
        return 0 <= row < 8 and 0 <= col < 8

    def is_empty(self, row, col):
        '''
        La función verifica si una casilla está vacía.
        Funcionalidad:
        - Verifica si la casilla en la posición dada está dentro de los límites del tablero y no contiene una pieza.
        Parámetros:
        row: Fila de la posición a verificar.
        col: Columna de la posición a verificar.
        Retorna:
        True si la casilla está vacía, False en caso contrario.
        '''
        return self.is_in_bounds(row, col) and self.__board__.get_piece(row, col) is None

    def can_capture(self, row, col):
        '''
        La función verifica si el peón puede capturar una pieza en una casilla dada.
        Funcionalidad:
        - Verifica si hay una pieza en la casilla y si pertenece al oponente.
        Parámetros:
        row: Fila de la posición a verificar.
        col: Columna de la posición a verificar.
        Retorna:
        True si el peón puede capturar la pieza, False en caso contrario.
        '''
        piece = self.__board__.get_piece(row, col)
        return piece is not None and piece.get_color != self.__color__   
