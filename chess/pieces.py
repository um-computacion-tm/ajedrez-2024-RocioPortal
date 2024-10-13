class Piece:
    def __init__(self, color, board):
        '''
        El constructor inicializa la pieza con un color y la asocia a un tablero.
        Funcionalidad:
        Crea el atributo privado __color__ que almacena el color de la pieza.
        Crea el atributo privado __board__ que referencia el tablero en el que está la pieza.
        Define las direcciones posibles de movimiento para piezas como el rey y la reina.
        Parámetros:
        color: Color de la pieza, puede ser "WHITE" o "BLACK".
        board: Referencia al tablero en el que se encuentra la pieza.
        '''
        self.__color__ = color
        self.__board__ = board
        self.__king_queen_directions__ = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]

    def __str__(self):
        '''
        La función devuelve la representación en cadena de la pieza.
        Funcionalidad:
        Devuelve el símbolo Unicode correspondiente a la pieza dependiendo de su color.
        Retorna:
        La representación en cadena de la pieza: `white_str` si es blanca, `black_str` si es negra.
        '''
        if self.__color__ == "WHITE":
            return self.white_str
        else:
            return self.black_str
        
    @property
    def get_color (self):
        '''
        La función devuelve el color de la pieza.
        Funcionalidad:
        Devuelve el valor del atributo privado __color__.
        Retorna:
        El color de la pieza.
        '''
        return self.__color__


    def possible_moves_general(self, row, col, directions, single_step=False):
        '''
        La función genera las posiciones posibles a las que una pieza puede moverse.
        Funcionalidad:
        Recorre todas las direcciones permitidas para la pieza.
        Si encuentra otra pieza en la trayectoria, verifica si es una pieza enemiga para capturarla o detiene el avance.
        Si el parámetro `single_step` es True, la pieza solo avanzará una casilla en la dirección dada.
        Parámetros:
        row: Fila de la posición actual de la pieza.
        col: Columna de la posición actual de la pieza.
        directions: Lista de direcciones posibles para moverse, como tuplas de desplazamiento de fila y columna.
        single_step: Si es True, la pieza solo se moverá una casilla en cada dirección.
        Retorna:
        Una lista de tuplas con las posiciones posibles a las que la pieza puede moverse.
        '''
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