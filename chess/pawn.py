from chess.pieces import Piece

class Pawn(Piece):
    
    white_str = "♟"  
    black_str = "♙"
    
    def valid_positions(self, from_row, from_col, to_row, to_col):
        # Movimientos de avance del peón
        directions = [(1, 0)] if self.__color__ == "BLACK" else [(-1, 0)]
        
        # Si está en la fila inicial, puede avanzar dos casillas
        if self.__color__ == "BLACK" and from_row == 1:
            directions.append((2, 0))
        elif self.__color__ == "WHITE" and from_row == 6:
            directions.append((-2, 0))

        # Movimientos hacia adelante (sin capturar)
        possible_positions = []
        for direction in directions:
            next_row = from_row + direction[0]
            next_col = from_col + direction[1]

            # Verificar si está dentro del tablero
            if 0 <= next_row < 8 and 0 <= next_col < 8:
                # Verificar si la casilla está vacía
                if self.__board__.get_piece(next_row, next_col) is None:
                    possible_positions.append((next_row, next_col))
                else:
                    break  # Si hay una pieza en el camino, no puede seguir avanzando

        # Capturas en diagonal
        capture_directions = [(1, 1), (1, -1)] if self.__color__ == "BLACK" else [(-1, 1), (-1, -1)]
        
        for direction in capture_directions:
            next_row, next_col = from_row + direction[0], from_col + direction[1]
            if 0 <= next_row < 8 and 0 <= next_col < 8:
                other_piece = self.__board__.get_piece(next_row, next_col)
                if other_piece and other_piece.get_color != self.__color__:
                    possible_positions.append((next_row, next_col))  # Solo captura si hay una pieza enemiga

        return (to_row, to_col) in possible_positions
