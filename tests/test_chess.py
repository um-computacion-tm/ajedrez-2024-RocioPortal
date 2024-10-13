import unittest
from chess.game import Chess
from chess.exceptions import InvalidMove, InvalidTurn, EmptyPosition, SelfCaptureException
from chess.board import Board
from chess.rook import Rook


class TestChess(unittest.TestCase):

    def setUp(self):
        # Crear una instancia del juego de ajedrez para cada prueba
        self.game = Chess()

    def test_initial_turn(self):
        # Verificar que las blancas comienzan el juego
        self.assertEqual(self.game.turn, "WHITE")

    def test_invalid_move_empty_position(self):
        # Intentar mover desde una posición vacía (debería lanzar EmptyPosition)
        with self.assertRaises(EmptyPosition):
            self.game.move(4, 4, 5, 4)  # No hay ninguna pieza en (4, 4)


    def test_show_board(self):
        chess = Chess()
        expected_str = (
            "  0 1 2 3 4 5 6 7\n"
            "0 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n"
            "1 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ \n"
            "2 . . . . . . . . \n"
            "3 . . . . . . . . \n"
            "4 . . . . . . . . \n"
            "5 . . . . . . . . \n"
            "6 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n"
            "7 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n"
        )
        self.assertEqual(chess.show_board(), expected_str)

    def test_change_turn(self):
        # Verificar que el turno cambie después de un movimiento
        self.game.move(6, 4, 5, 4)  # Mover el peón blanco
        self.assertEqual(self.game.turn, "BLACK")  # Ahora debe ser el turno de las negras

        self.game.move(1, 4, 2, 4)  # Mover el peón negro
        self.assertEqual(self.game.turn, "WHITE")  # Ahora debe ser el turno de las blancas

    def test_invalid_turn(self):
        # Intentar mover una pieza negra en el turno de las blancas
        with self.assertRaises(InvalidTurn):
            self.game.move(1, 4, 2, 4)  # Mover un peón negro cuando es turno de las blancas

    def test_invalid_move(self):
        # Intentar mover un peón blanco dos casillas adelante cuando ya no es el primer movimiento
        self.game.move(6, 4, 5, 4)  # Primer movimiento válido
        with self.assertRaises(InvalidMove):
            self.game.move(5, 4, 3, 4)  # Este movimiento debería ser inválido

    def test_get_board(self):
        # Verificar que el tablero se obtiene correctamente a través de get_board()
        board = self.game.get_board()
        self.assertIsInstance(board, Board)  # Asegura que es una instancia de la clase Board

        #verificar que el tablero contiene piezas en posiciones iniciales
        self.assertIsNotNone(board.get_piece(0, 0))  # Debería haber una torre negra en la posición (0, 0)
        self.assertIsNotNone(board.get_piece(7, 0))  # Debería haber una torre blanca en la posición (7, 0)


    def test_self_capture(self):
        # Coloca una pieza blanca en (6, 0) (Peón) y otra blanca en (5, 0)
        rook = Rook("WHITE", self.game.get_board())
        self.game.get_board().set_piece(6, 0, rook)  # Colocar torre blanca en (6, 0)
        self.game.get_board().set_piece(5, 0, rook)  # Colocar otra torre blanca en (5, 0)

        # Intentar capturar la pieza propia
        with self.assertRaises(SelfCaptureException):
            self.game.move(6, 0, 5, 0)  # Mover la torre desde (6, 0) a (5, 0) (captura inválida)

    def test_white_wins(self):
        # Simular un escenario donde solo las piezas blancas permanecen
        for row in range(8):
            for col in range(8):
                self.game.__board__.set_piece(row, col, None)  # Vaciar el tablero

        self.game.__board__.set_piece(7, 0, Rook("WHITE", self.game.__board__))  # Dejar una torre blanca

        result = self.game.check_winner()  # Verifica si el juego ha terminado
        self.assertEqual(result, "WHITE WINS")  # El jugador blanco debe ganar

    def test_black_wins(self):
        # Simular un escenario donde solo las piezas negras permanecen
        for row in range(8):
            for col in range(8):
                self.game.__board__.set_piece(row, col, None)  # Vaciar el tablero

        self.game.__board__.set_piece(0, 0, Rook("BLACK", self.game.__board__))  # Dejar una torre negra

        result = self.game.check_winner()  # Verifica si el juego ha terminado
        self.assertEqual(result, "BLACK WINS")  # El jugador negro debe ganar

    def test_game_in_progress(self):
        # Simular un escenario donde el juego sigue en progreso (ambos jugadores tienen piezas)
        for row in range(8):
            for col in range(8):
                self.game.__board__.set_piece(row, col, None)  # Vaciar el tablero

        # Agregar una pieza blanca y una negra
        self.game.__board__.set_piece(7, 0, Rook("WHITE", self.game.__board__))
        self.game.__board__.set_piece(0, 0, Rook("BLACK", self.game.__board__))

        result = self.game.check_winner()  # Verifica si el juego sigue en progreso
        self.assertFalse(result)  # El juego debe seguir en progreso (no hay ganador todavía)


if __name__ == '__main__':
    unittest.main()