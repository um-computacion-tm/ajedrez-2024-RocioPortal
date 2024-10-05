from chess.pieces import Piece
from chess.queen import Queen

class Pawn(Piece):
    
    white_str = "♟"  
    black_str = "♙"

    def valid_positions(self, from_row, from_col, to_row, to_col):
        # Obtener posibles movimientos y capturas
        possible_positions = self.get_possible_moves(from_row, from_col)
        return (to_row, to_col) in possible_positions

    def get_possible_moves(self, from_row, from_col):
        moves = []
        direction = self.get_move_direction()  # Obtener dirección según el color
        start_row = self.get_start_row()       # Obtener fila inicial según el color

        # Movimientos hacia adelante
        self.add_forward_moves(from_row, from_col, direction, start_row, moves)

        # Capturas diagonales
        self.add_capture_moves(from_row, from_col, direction, moves)

        return moves

    def add_forward_moves(self, from_row, from_col, direction, start_row, moves):
        # Movimiento hacia adelante si está vacío
        if self.is_empty(from_row + direction, from_col):
            moves.append((from_row + direction, from_col))

            # Si está en la fila inicial, puede avanzar dos casillas
            if from_row == start_row and self.is_empty(from_row + 2 * direction, from_col):
                moves.append((from_row + 2 * direction, from_col))

    def add_capture_moves(self, from_row, from_col, direction, moves):
        capture_moves = [(direction, -1), (direction, 1)]
        for move in capture_moves:
            next_row, next_col = from_row + move[0], from_col + move[1]
            if self.is_in_bounds(next_row, next_col) and self.can_capture(next_row, next_col):
                moves.append((next_row, next_col))

    def get_move_direction(self):
        # Retorna la dirección de movimiento según el color
        return -1 if self.__color__ == 'WHITE' else 1

    def get_start_row(self):
        # Retorna la fila inicial según el color
        return 6 if self.__color__ == 'WHITE' else 1

    def is_in_bounds(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def is_empty(self, row, col):
        return self.is_in_bounds(row, col) and self.__board__.get_piece(row, col) is None

    def can_capture(self, row, col):
        piece = self.__board__.get_piece(row, col)
        return piece is not None and piece.get_color != self.__color__   


    def verify_promote(self, row, col):
        if (self.__color__ == "WHITE" and row == 0) or (self.__color__ == "BLACK" and row == 7):
            self.promote(row, col)
     
    def promote(self, row, col): 
        self.__board__.set_piece(row, col, Queen(self.__color__, self.__board__))
        return True #ocurrio el cambio









"""
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

"""