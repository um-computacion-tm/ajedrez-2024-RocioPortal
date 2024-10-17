import unittest
from chess.bishop import Bishop
from chess.board import Board

class TestBishop(unittest.TestCase):
    """
    Clase de prueba para la pieza Bishop en el juego de ajedrez.
    """

    def test_str(self):
        """
        Prueba que la representación en cadena (str) de un alfil blanco sea correcta.
        Funcionalidad:
        - Verifica que el símbolo del alfil blanco sea "♝".
        """
        board = Board()
        bishop = Bishop("WHITE", board)
        self.assertEqual(
            str(bishop),
            "♝",
        )

    def setUp(self):
        """
        Configuración inicial para cada prueba.
        Funcionalidad:
        - Crea un tablero vacío de prueba antes de ejecutar cada test.
        """
        self.board = Board(for_test=True)

    def test_bishop_move_diagonal(self):
        """
        Prueba que el alfil se pueda mover correctamente en diagonal.
        Funcionalidad:
        - Verifica que un movimiento diagonal válido sea permitido.
        """
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        is_valid = bishop.valid_positions(4, 4, 7, 7)
        self.assertTrue(is_valid)

    def test_bishop_blocked_by_own_piece(self):
        """
        Prueba que el alfil no pueda moverse si hay una pieza propia bloqueando.
        Funcionalidad:
        - Verifica que el alfil no pueda pasar a través de una pieza del mismo color.
        """
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        self.board.set_piece(5, 5, Bishop("WHITE", self.board))
        is_valid = bishop.valid_positions(4, 4, 7, 7)
        self.assertFalse(is_valid)

    def test_bishop_capture_enemy(self):
        """
        Prueba que el alfil pueda capturar una pieza enemiga en su camino.
        Funcionalidad:
        - Verifica que el alfil pueda capturar una pieza enemiga en su ruta diagonal.
        """
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        self.board.set_piece(5, 5, Bishop("BLACK", self.board))
        is_valid = bishop.valid_positions(4, 4, 5, 5)
        self.assertTrue(is_valid)

    def test_bishop_blocked_by_own_piece(self):
        """
        Prueba que el alfil no pueda moverse si está bloqueado por una pieza propia en su camino.
        Funcionalidad:
        - Verifica que el alfil no pueda pasar por encima de una pieza del mismo color.
        """
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        self.board.set_piece(5, 5, Bishop("WHITE", self.board))  # Bloqueo por pieza propia
        is_valid = bishop.valid_positions(4, 4, 6, 6)
        self.assertFalse(is_valid)

    def test_bishop_capture_enemy_diagonal(self):
        """
        Prueba que el alfil pueda capturar una pieza enemiga en su camino diagonal.
        Funcionalidad:
        - Verifica que el alfil pueda capturar correctamente una pieza enemiga en su ruta diagonal.
        """
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        self.board.set_piece(6, 6, Bishop("BLACK", self.board))  # Pieza enemiga
        is_valid = bishop.valid_positions(4, 4, 6, 6)
        self.assertTrue(is_valid)  # La captura debería ser válida

    def test_bishop_move_out_of_bounds(self):
        """
        Prueba que el alfil no pueda moverse fuera de los límites del tablero.
        Funcionalidad:
        - Verifica que un intento de movimiento fuera del tablero sea inválido.
        """
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(0, 0, bishop)
        is_valid = bishop.valid_positions(0, 0, -1, -1)  # Movimiento fuera del tablero
        self.assertFalse(is_valid)

    def test_bishop_move_orthogonal(self):
        """
        Prueba que el alfil no pueda moverse de manera ortogonal (horizontal o vertical).
        Funcionalidad:
        - Verifica que el alfil no pueda hacer movimientos no diagonales.
        """
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        is_valid = bishop.valid_positions(4, 4, 4, 6)  # Intento de movimiento horizontal
        self.assertFalse(is_valid)

    def test_bishop_long_move_diagonal(self):
        """
        Prueba que el alfil pueda realizar un movimiento diagonal largo sin ningún bloqueo.
        Funcionalidad:
        - Verifica que el alfil pueda moverse en una larga diagonal sin obstáculos.
        """
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(1, 1, bishop)
        is_valid = bishop.valid_positions(1, 1, 7, 7)  # Movimiento diagonal largo sin bloqueo
        self.assertTrue(is_valid)


if __name__ == '__main__':
    unittest.main()