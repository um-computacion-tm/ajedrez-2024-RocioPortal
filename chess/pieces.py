class Piece:
    def __init__(self, color, board):
        self.__color__ = color
        self.__board__ = board

    def __str__(self):
        if self.__color__ == "WHITE":
            return self.white_str
        else:
            return self.black_str
        
    @property
    def get_color (self):
        return self.__color__
    

#movimientos verticales y horizontales

    def possible_positions_vd(self, row, col):  #movimiento vertical descendente
        possibles = []
        for next_row in range(row + 1, 8):
            # que la celda que sigue no este ocupada..
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))
                break
            possibles.append((next_row, col))
        return possibles

    def possible_positions_va(self, row, col): #movimiento vertical ascendente
        possibles = []
        for next_row in range(row - 1, -1, -1):
            possibles.append((next_row, col))
        return possibles
    
   
    def possible_positions_hl(self, row, col):  #movimiento horizontal hacia la izquierda 
        possibles = []
        for next_col in range(col - 1, -1, -1):
            other_piece = self.__board__.get_piece(row, next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((row, next_col))
                break
            possibles.append((row, next_col))
        return possibles
    
    
    def possible_positions_hr(self, row, col): # Movimiento horizontal hacia la derecha
        possibles = []
        for next_col in range(col + 1, 8):
            other_piece = self.__board__.get_piece(row, next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((row, next_col))
                break
            possibles.append((row, next_col))
        return possibles
    
# Movimientos diagonales (usados por el alfil y reina)

    def possible_positions_dad(self, row, col):  # Diagonal ascendente derecha
        possibles = []
        next_row, next_col = row - 1, col + 1
        while next_row >= 0 and next_col < 8:
            other_piece = self.__board__.get_piece(next_row, next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, next_col))
                break
            possibles.append((next_row, next_col))
            next_row -= 1
            next_col += 1
        return possibles
    
    def possible_positions_dai(self, row, col):  # Diagonal ascendente izquierda
        possibles = []
        next_row, next_col = row - 1, col - 1
        while next_row >= 0 and next_col >= 0:
            other_piece = self.__board__.get_piece(next_row, next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, next_col))
                break
            possibles.append((next_row, next_col))
            next_row -= 1
            next_col -= 1
        return possibles