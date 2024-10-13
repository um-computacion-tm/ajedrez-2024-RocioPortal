from chess.board import Board
from chess.exceptions import InvalidMove, InvalidTurn, EmptyPosition, SelfCaptureException

class Chess:
    def __init__(self):
        """
        La función crea una instancia de la clase Chess (ajedrez).
        Funcionalidad:
        Inicializa el tablero de juego y establece el turno inicial como "WHITE" (blancas).
        """
        self.__board__ = Board()
        self.__turn__ = "WHITE"  #inician las blancas


    def is_playing(self):
        '''
        La función indica si el juego está en curso.
        Funcionalidad:
        Devuelve `True` para indicar que el juego sigue activo.
        '''
        return True

    def move(
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
        '''
        La función mueve una pieza en el tablero si el movimiento es válido.
        Funcionalidad:
        Verifica que haya una pieza en la posición de origen y que pertenezca al jugador que tiene el turno.
        Verifica que el movimiento sea válido y que no se capture una pieza del mismo color.
        Si todo es correcto, mueve la pieza y cambia el turno.
        Parámetros:
        from_row: Fila de origen.
        from_col: Columna de origen.
        to_row: Fila de destino.
        to_col: Columna de destino.
        '''
       # validate coords
        piece = self.__board__.get_piece(from_row, from_col)
        if not piece:
            raise EmptyPosition() 
        if not piece.get_color == self.__turn__:  
            raise InvalidTurn()
        if self.__board__.get_piece(to_row, to_col) and self.__board__.get_piece(to_row, to_col).get_color == self.__turn__:
            raise SelfCaptureException()  # Nueva excepción para evitar capturar tus propias piezas
        if not piece.valid_positions(from_row, from_col, to_row, to_col):
            raise InvalidMove()
        self.__board__.move(from_row, from_col, to_row, to_col)
        self.change_turn()


    def check_winner(self):
        '''
        La función verifica si algún jugador ha ganado.
        Funcionalidad:
        Recorre el tablero contando las piezas de cada color.
        Si alguno de los jugadores se queda sin piezas, se declara al otro como ganador.
        Retorna el ganador o False si aún no hay ganador.
        '''
        white_pieces = 0
        black_pieces = 0
        
        # Recorre el tablero y cuenta las piezas de cada color
        for row in self.__board__.__positions__:
            for piece in row:
                if piece is not None:
                    if piece.get_color == "WHITE":
                        white_pieces += 1
                    elif piece.get_color == "BLACK":
                        black_pieces += 1

        # Verifica si alguno de los jugadores se ha quedado sin piezas
        if white_pieces == 0:
            return "BLACK WINS"
        elif black_pieces == 0:
            return "WHITE WINS"
        else:
            return False
        

    @property
    def turn(self):
        '''
        La función devuelve el turno actual.
        Funcionalidad:
        Retorna el valor del atributo `__turn__`, que indica de quién es el turno ("WHITE" o "BLACK").
        '''
        return self.__turn__
    
    def show_board(self):
        '''
        La función muestra el estado actual del tablero.
        Funcionalidad:
        Devuelve el tablero como una cadena de texto con la posición actual de las piezas.
        '''
        return str(self.__board__)

    def change_turn(self):
        '''
        La función cambia el turno del jugador.
        Funcionalidad:
        Cambia el turno del jugador actual. Si es el turno de las blancas, lo cambia a negras y viceversa.
        '''
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"

    def get_board(self):
        '''
        La función devuelve el tablero de juego.
        Funcionalidad:
        Retorna el tablero actual de la partida.
        '''
        return self.__board__

