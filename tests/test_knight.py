import unittest
from chess.knight import Knight
from chess.board import Board

class TestKnight(unittest.TestCase):
    """
    Clase de pruebas para la pieza `Knight` en el juego de ajedrez.
    """

    def test_str(self):
        """
        Prueba que la representación en cadena (str) del caballo sea correcta.
        Funcionalidad:
        - Verifica que el símbolo del caballo blanco sea "♞".
        """
        board = Board()
        knight = Knight("WHITE", board)
        self.assertEqual(
            str(knight),
            "♞",
        )       

    def setUp(self):
        """
        Configuración inicial para cada prueba.
        Funcionalidad:
        - Crea un nuevo tablero de prueba antes de ejecutar cada test.
        """
        self.board = Board(for_test=True)

    def test_knight_move(self):
        """
        Prueba que el caballo pueda moverse en "L" a una posición válida.
        Funcionalidad:
        - Coloca el caballo en una posición y verifica que pueda moverse en "L" a una nueva posición.
        """
        knight = Knight("WHITE", self.board)
        self.board.set_piece(4, 4, knight)
        is_valid = knight.valid_positions(4, 4, 6, 5)
        self.assertTrue(is_valid)

    def test_knight_blocked_by_own_piece(self):
        """
        Prueba que el caballo no pueda moverse a una casilla ocupada por una pieza propia.
        Funcionalidad:
        - Coloca una pieza propia en la casilla destino y verifica que el caballo no pueda moverse a esa posición.
        """
        knight = Knight("WHITE", self.board)
        self.board.set_piece(4, 4, knight)
        self.board.set_piece(6, 5, Knight("WHITE", self.board))
        is_valid = knight.valid_positions(4, 4, 6, 5)
        self.assertFalse(is_valid)

    def test_knight_invalid_move(self):
        """
        Prueba que un movimiento no válido del caballo sea rechazado.
        Funcionalidad:
        - Verifica que el caballo no pueda moverse a una posición que no sea en forma de "L".
        """
        knight = Knight("WHITE", self.board)
        self.board.set_piece(4, 4, knight)
        is_valid = knight.valid_positions(4, 4, 5, 5) 
        self.assertFalse(is_valid)

    def test_knight_capture_enemy(self):
        """
        Prueba que el caballo pueda capturar una pieza enemiga.
        Funcionalidad:
        - Coloca una pieza enemiga en la casilla destino y verifica que el caballo pueda capturarla.
        """
        knight = Knight("WHITE", self.board)
        self.board.set_piece(4, 4, knight)
        self.board.set_piece(6, 5, Knight("BLACK", self.board)) 
        is_valid = knight.valid_positions(4, 4, 6, 5)
        self.assertTrue(is_valid)

    def test_knight_move_out_of_bounds(self):
        """
        Prueba que el caballo no pueda moverse fuera de los límites del tablero.
        Funcionalidad:
        - Verifica que un intento de movimiento fuera de los límites del tablero sea inválido.
        """
        knight = Knight("WHITE", self.board)
        self.board.set_piece(0, 1, knight) 
        is_valid = knight.valid_positions(0, 1, -1, 0) 
        self.assertFalse(is_valid)

    def test_knight_valid_move(self):
        """
        Prueba que el caballo pueda realizar un movimiento válido en "L".
        Funcionalidad:
        - Coloca el caballo en una posición y verifica que pueda moverse en "L" a una nueva posición válida.
        """
        knight = Knight("WHITE", self.board)
        self.board.set_piece(2, 3, knight) 
        is_valid = knight.valid_positions(2, 3, 4, 2) 
        self.assertTrue(is_valid)

    def test_knight_cannot_capture_own_piece(self):
        """
        Prueba que el caballo no pueda capturar una pieza propia.
        Funcionalidad:
        - Verifica que el caballo no pueda moverse a una casilla ocupada por una pieza propia y capturarla.
        """
        knight = Knight("WHITE", self.board)
        self.board.set_piece(4, 4, knight)
        self.board.set_piece(6, 5, Knight("WHITE", self.board)) 
        is_valid = knight.valid_positions(4, 4, 6, 5)
        self.assertFalse(is_valid)  


if __name__ == '__main__':
    unittest.main()