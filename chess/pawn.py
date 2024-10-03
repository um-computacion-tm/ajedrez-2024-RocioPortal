from chess.pieces import Piece
from chess.queen import Queen

class Pawn(Piece):
    
    white_str = "♟"  
    black_str = "♙"

    def valid_positions(self, from_row, from_col, to_row, to_col):
        # Obtener posibles movimientos y capturas
        possible_positions = self.get_possible_moves(from_row, from_col)
        possible_positions += self.get_possible_captures(from_row, from_col)
        return (to_row, to_col) in possible_positions

    # Movimientos normales del peón
    def get_possible_moves(self, from_row, from_col):
        directions = self.get_move_directions(from_row)
        possible_positions = []

        for direction in directions:
            next_row, next_col = from_row + direction[0], from_col + direction[1]
            if self.is_in_bounds(next_row, next_col) and self.is_empty(next_row, next_col):
                possible_positions.append((next_row, next_col))
            else:
                break  # Detenerse si hay una pieza en el camino

        return possible_positions

    # Capturas en diagonal del peón
    def get_possible_captures(self, from_row, from_col):
        capture_directions = [(1, 1), (1, -1)] if self.__color__ == "BLACK" else [(-1, 1), (-1, -1)]
        possible_captures = []

        for direction in capture_directions:
            next_row, next_col = from_row + direction[0], from_col + direction[1]
            if self.is_in_bounds(next_row, next_col):
                other_piece = self.__board__.get_piece(next_row, next_col)
                if other_piece and other_piece.get_color != self.__color__:
                    possible_captures.append((next_row, next_col))  # Solo captura si hay una pieza enemiga

        return possible_captures

    # Obtener direcciones de movimiento del peón (incluye avanzar dos casillas si está en la fila inicial)
    def get_move_directions(self, from_row):
        directions = [(1, 0)] if self.__color__ == "BLACK" else [(-1, 0)]

        # Si está en la fila inicial, puede avanzar dos casillas
        if self.__color__ == "BLACK" and from_row == 1:
            directions.append((2, 0))
        elif self.__color__ == "WHITE" and from_row == 6:
            directions.append((-2, 0))

        return directions
  
    # Verificar si las coordenadas están dentro del tablero
    def is_in_bounds(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    # Verificar si la posición está vacía
    def is_empty(self, row, col):
        return self.__board__.get_piece(row, col) is None
    
    def verify_promote(self, row, col):
        if (self.__color__ == "WHITE" and row == 0) or (self.__color__ == "BLACK" and row == 7):
            self.promote(row, col)
     
    def promote(self, row, col): 
        self.__board__.set_piece(row, col, Queen(self.__color__, self.__board__))
        return True #ocurrio el cambio

    
