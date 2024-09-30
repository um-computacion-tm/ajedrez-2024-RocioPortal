class Piece:
    def __init__(self, color, board):
        self.__color__ = color
        self.__board__ = board
        self.__king_queen_directions__ = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]

    def __str__(self):
        if self.__color__ == "WHITE":
            return self.white_str
        else:
            return self.black_str
        
    @property
    def get_color (self):
        return self.__color__


    def possible_moves_general(self, row, col, directions, single_step=False):
        possibles = []
        for row_dir, col_dir in directions:
            next_row, next_col = row + row_dir, col + col_dir
            while 0 <= next_row < 8 and 0 <= next_col < 8:
                other_piece = self.__board__.get_piece(next_row, next_col)
                if other_piece is not None:
                    if other_piece.get_color != self.get_color:
                        possibles.append((next_row, next_col))  # Puede capturar
                    break  # Detener si hay una pieza
                possibles.append((next_row, next_col))

                # Si `single_step` es True, solo avanzamos una casilla
                if single_step:
                    break

                # Continuar en la misma dirección
                next_row += row_dir
                next_col += col_dir
        return possibles