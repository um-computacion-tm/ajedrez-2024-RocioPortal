import unittest
from chess.game import Chess
from chess.exceptions import InvalidMove, InvalidTurn, EmptyPosition, SelfCaptureException
from chess.board import Board
from chess.rook import Rook


class TestChess(unittest.TestCase):
    """
    Clase de pruebas para la lógica del juego de ajedrez (`Chess`).
    """

    def setUp(self):
        """
        Configuración inicial para cada prueba.
        Funcionalidad:
        - Crea una nueva instancia del juego de ajedrez antes de cada prueba.
        """
        self.game = Chess()

    def test_initial_turn(self):
        """
        Prueba que el turno inicial sea el de las blancas.
        Funcionalidad:
        - Verifica que el juego comience con el turno de las piezas blancas.
        """
        self.assertEqual(self.game.turn, "WHITE")

    def test_invalid_move_empty_position(self):
        """
        Prueba que se lance una excepción al intentar mover desde una posición vacía.
        Funcionalidad:
        - Verifica que se lance `EmptyPosition` al intentar mover una pieza desde una casilla vacía.
        """
        with self.assertRaises(EmptyPosition):
            self.game.move(4, 4, 5, 4)  

    def test_show_board(self):
        """
        Prueba que el tablero se muestre correctamente.
        Funcionalidad:
        - Compara la representación del tablero inicial con una cadena de texto esperada.
        """
        chess = Chess()
        expected_str = (
            "    0    1    2    3    4    5    6    7 \n"
            "0   ♖    ♘    ♗    ♕    ♔    ♗    ♘    ♖  \n\n"
            "1   ♙    ♙    ♙    ♙    ♙    ♙    ♙    ♙  \n\n"
            "2   .    .    .    .    .    .    .    .  \n\n"
            "3   .    .    .    .    .    .    .    .  \n\n"
            "4   .    .    .    .    .    .    .    .  \n\n"
            "5   .    .    .    .    .    .    .    .  \n\n"
            "6   ♟    ♟    ♟    ♟    ♟    ♟    ♟    ♟  \n\n"
            "7   ♜    ♞    ♝    ♛    ♚    ♝    ♞    ♜  \n\n"
        )
        self.assertEqual(chess.show_board(), expected_str)

    def test_change_turn(self):
        """
        Prueba que el turno cambie correctamente después de un movimiento.
        Funcionalidad:
        - Verifica que el turno cambie de blanco a negro y luego de negro a blanco tras cada movimiento.
        """
        self.game.move(6, 4, 5, 4) 
        self.assertEqual(self.game.turn, "BLACK") 

        self.game.move(1, 4, 2, 4) 
        self.assertEqual(self.game.turn, "WHITE")  

    def test_invalid_turn(self):
        """
        Prueba que se lance una excepción si un jugador intenta mover una pieza cuando no es su turno.
        Funcionalidad:
        - Verifica que se lance `InvalidTurn` al intentar mover una pieza negra cuando es el turno de las blancas.
        """
        with self.assertRaises(InvalidTurn):
            self.game.move(1, 4, 2, 4)  # Mover un peón negro cuando es turno de las blancas

    def test_invalid_move(self):
        """
        Prueba que se lance una excepción si un movimiento es inválido.
        Funcionalidad:
        - Verifica que se lance `InvalidMove` al intentar mover un peón blanco dos casillas después de su primer movimiento.
        """
        self.game.move(6, 4, 5, 4)  # Primer movimiento válido
        with self.assertRaises(InvalidMove):
            self.game.move(5, 4, 3, 4)  # Movimiento inválido

    def test_get_board(self):
        """
        Prueba que se pueda obtener el tablero del juego.
        Funcionalidad:
        - Verifica que `get_board()` devuelva una instancia del tablero y que las piezas estén en sus posiciones iniciales.
        """
        board = self.game.get_board()
        self.assertIsInstance(board, Board)  # Asegura que es una instancia de la clase Board

        # Verificar que el tablero contiene piezas en posiciones iniciales
        self.assertIsNotNone(board.get_piece(0, 0))  # Torre negra en (0, 0)
        self.assertIsNotNone(board.get_piece(7, 0))  # Torre blanca en (7, 0)

    def test_self_capture(self):
        """
        Prueba que no se pueda capturar una pieza propia.
        Funcionalidad:
        - Verifica que se lance `SelfCaptureException` al intentar capturar una pieza del mismo color.
        """
        rook = Rook("WHITE", self.game.get_board())
        self.game.get_board().set_piece(6, 0, rook)  # Colocar torre blanca en (6, 0)
        self.game.get_board().set_piece(5, 0, rook)  # Colocar otra torre blanca en (5, 0)

        # Intentar capturar la pieza propia
        with self.assertRaises(SelfCaptureException):
            self.game.move(6, 0, 5, 0)  # Mover la torre desde (6, 0) a (5, 0)

    def test_white_wins(self):
        """
        Prueba que el jugador blanco gane cuando solo quedan piezas blancas.
        Funcionalidad:
        - Simula un escenario donde solo quedan piezas blancas en el tablero y verifica que el jugador blanco gane.
        """
        for row in range(8):
            for col in range(8):
                self.game.__board__.set_piece(row, col, None)  # Vaciar el tablero

        self.game.__board__.set_piece(7, 0, Rook("WHITE", self.game.__board__))  # Dejar una torre blanca

        result = self.game.check_winner()  # Verifica si el juego ha terminado
        self.assertEqual(result, "WHITE WINS")  # El jugador blanco debe ganar

    def test_black_wins(self):
        """
        Prueba que el jugador negro gane cuando solo quedan piezas negras.
        Funcionalidad:
        - Simula un escenario donde solo quedan piezas negras en el tablero y verifica que el jugador negro gane.
        """
        for row in range(8):
            for col in range(8):
                self.game.__board__.set_piece(row, col, None)  

        self.game.__board__.set_piece(0, 0, Rook("BLACK", self.game.__board__)) 

        result = self.game.check_winner() 
        self.assertEqual(result, "BLACK WINS") 

    def test_game_in_progress(self):
        """
        Prueba que el juego siga en progreso cuando ambos jugadores tienen piezas en el tablero.
        Funcionalidad:
        - Simula un escenario donde tanto las piezas blancas como negras siguen en el tablero y verifica que el juego no haya terminado.
        """
        for row in range(8):
            for col in range(8):
                self.game.__board__.set_piece(row, col, None)  # Vaciar el tablero

        # Agregar una pieza blanca y una negra
        self.game.__board__.set_piece(7, 0, Rook("WHITE", self.game.__board__))
        self.game.__board__.set_piece(0, 0, Rook("BLACK", self.game.__board__))

        result = self.game.check_winner() 
        self.assertFalse(result)  


if __name__ == '__main__':
    unittest.main()