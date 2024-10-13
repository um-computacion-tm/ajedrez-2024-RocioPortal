from chess.rook import Rook
from chess.knight import Knight
from chess.bishop import Bishop
from chess.queen import Queen
from chess.king import King
from chess.pawn import Pawn
from chess.exceptions import OutOfBoard

class Board:    
    def __init__(self, for_test = False): #para que en los test de cada pieza no aparezcan las demas
        '''
        La función crea una instancia de la clase Board (tablero).
        Funcionalidad:
        Inicializa un tablero vacío de 8x8.
        Si `for_test` es `False`, se colocan las piezas en sus posiciones iniciales.
        Parámetros:
        for_test: Indica si el tablero se inicializa sin piezas para pruebas.
        '''
        self.__positions__ = []    
        for _ in range (8):
            col= []
            for _ in range (8):
                col.append(None)
            self.__positions__.append(col)
        if not for_test:
            #torres
                self.__positions__ [0] [0] = Rook("BLACK", self)    
                self.__positions__ [0] [7] = Rook("BLACK", self) 
                self.__positions__ [7] [7] = Rook("WHITE", self) 
                self.__positions__ [7] [0] = Rook("WHITE", self) 

            #Caballos
                self.__positions__[0][1] = Knight("BLACK", self)
                self.__positions__[0][6] = Knight("BLACK", self)
                self.__positions__[7][1] = Knight("WHITE", self)  
                self.__positions__[7][6] = Knight("WHITE", self)

            #Alfiles
                self.__positions__[0][2] = Bishop("BLACK",self)  
                self.__positions__[0][5] = Bishop("BLACK", self)
                self.__positions__[7][2] = Bishop("WHITE", self)
                self.__positions__[7][5] = Bishop("WHITE", self)

            #Reinas
                self.__positions__[0][3] = Queen("BLACK", self)
                self.__positions__[7][3] = Queen("WHITE", self)

            #Reyes
                self.__positions__[0][4] = King("BLACK", self)
                self.__positions__[7][4] = King("WHITE", self)

            #Peones
                for i in range(8):
                    self.__positions__[1][i] = Pawn("BLACK", self)
                    self.__positions__[6][i] = Pawn("WHITE", self)


    def __str__(self):
        '''
        La función convierte el tablero a una representación de texto.
        Funcionalidad:
        Devuelve el estado actual del tablero con índices de filas y columnas.
        Las celdas vacías se representan con un punto (.).
        Retorna:
        Una cadena de texto que representa el tablero actual.
        '''
        board_str = "  0 1 2 3 4 5 6 7\n"  # Índices de las columnas
        for i, row in enumerate(self.__positions__):
            board_str += str(i) + " "  # Índices de las filas
            for cell in row:
                if cell is not None:
                    board_str += str(cell) + " "
                else:
                    board_str += ". "  # Representación de las celdas vacías
            board_str += "\n"
        return board_str


    def get_piece(self, row, col):
        '''
        La función obtiene la pieza en una posición específica del tablero.
        Funcionalidad:
        Verifica si la posición está dentro del rango permitido (0 a 7).
        Si la posición es válida, devuelve la pieza en esa ubicación.
        Si no es válida, lanza una excepción `OutOfBoard`.
        Parámetros:
        row: Fila de la pieza.
        col: Columna de la pieza.
        Retorna:
        La pieza en la posición especificada o `None` si está vacía.
        '''
        if not (
            0 <= row < 8 or 0 <= col < 8
        ):
            raise OutOfBoard()
        return self.__positions__[row][col]

    def set_piece(self, row, col, piece):
        '''
        La función coloca una pieza en una posición específica del tablero.
        Funcionalidad:
        Coloca una pieza en la fila y columna indicadas.
        Parámetros:
        row: Fila en la que se colocará la pieza.
        col: Columna en la que se colocará la pieza.
        piece: La pieza que se va a colocar.
        '''
        self.__positions__[row][col] = piece

    def move(self, from_row, from_col, to_row, to_col):
        '''
        La función mueve una pieza de una posición a otra en el tablero.
        Funcionalidad:
        Obtiene la pieza de la posición inicial y la coloca en la posición de destino.
        Luego, deja vacía la posición de origen.
        Parámetros:
        from_row: Fila de la posición inicial.
        from_col: Columna de la posición inicial.
        to_row: Fila de la posición de destino.
        to_col: Columna de la posición de destino.
        '''
        origin = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)