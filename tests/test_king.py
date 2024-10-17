import unittest
from chess.board import Board
from chess.king import King
from chess.rook import Rook
from chess.pawn import Pawn

class TestKing(unittest.TestCase):
    """
    Clase de pruebas para la pieza `King` en el juego de ajedrez.
    """

    def test_str(self):
        """
        Prueba que la representación en cadena (str) del rey sea correcta.
        Funcionalidad:
        - Verifica que el símbolo del rey blanco sea "♚".
        """
        board = Board()
        king = King("WHITE", board)
        self.assertEqual(
            str(king),
            "♚",
        )

    def setUp(self):
        """
        Configuración inicial para cada prueba.
        Funcionalidad:
        - Crea un nuevo tablero de prueba antes de ejecutar cada test.
        """
        self.board = Board(for_test=True)

    def test_king_move_one_square(self):
        """
        Prueba que el rey pueda moverse una casilla en cualquier dirección.
        Funcionalidad:
        - Coloca un rey en el tablero y verifica que pueda moverse una casilla en diagonal.
        """
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)

        is_valid = king.valid_positions(4, 4, 5, 5)
        self.assertTrue(is_valid)

    def test_king_blocked_by_own_piece(self):
        """
        Prueba que el rey no pueda moverse si hay una pieza propia bloqueando.
        Funcionalidad:
        - Coloca una pieza propia en la casilla destino y verifica que el rey no pueda moverse a esa posición.
        """
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        self.board.set_piece(5, 5, King("WHITE", self.board))  # Pieza blanca bloqueando

        is_valid = king.valid_positions(4, 4, 5, 5)
        self.assertFalse(is_valid)

    def test_king_move_two_squares_invalid(self):
        """
        Prueba que el rey no pueda moverse más de una casilla en cualquier dirección.
        Funcionalidad:
        - Verifica que el rey no pueda moverse dos casillas hacia adelante, lo cual es un movimiento inválido.
        """
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)

        is_valid = king.valid_positions(4, 4, 6, 4)
        self.assertFalse(is_valid)

    def test_king_move_too_far(self):
        """
        Prueba que el rey no pueda moverse más de una casilla en diagonal.
        Funcionalidad:
        - Verifica que el rey no pueda moverse dos casillas en diagonal.
        """
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        is_valid = king.valid_positions(4, 4, 6, 6)  # Más de un paso
        self.assertFalse(is_valid)

    def test_king_move_out_of_bounds(self):
        """
        Prueba que el rey no pueda moverse fuera de los límites del tablero.
        Funcionalidad:
        - Verifica que un intento de movimiento fuera de los límites del tablero sea inválido.
        """
        king = King("WHITE", self.board)
        self.board.set_piece(0, 0, king) 
        is_valid = king.valid_positions(0, 0, -1, -1)  
        self.assertFalse(is_valid)
    
    def test_king_cannot_capture_own_piece(self):
        """
        Prueba que el rey no pueda capturar su propia pieza.
        Funcionalidad:
        - Coloca una pieza propia en la casilla de destino y verifica que el rey no pueda capturarla.
        """
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        self.board.set_piece(5, 4, Pawn("WHITE", self.board)) 

        is_valid = king.valid_positions(4, 4, 5, 4)
        self.assertFalse(is_valid) 

    def test_king_capture_enemy(self):
        """
        Prueba que el rey pueda capturar una pieza enemiga.
        Funcionalidad:
        - Coloca una pieza enemiga en una casilla adyacente y verifica que el rey pueda capturarla.
        """
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        self.board.set_piece(5, 4, Pawn("BLACK", self.board))  

        is_valid = king.valid_positions(4, 4, 5, 4)
        self.assertTrue(is_valid) 

    def test_king_blocked_by_enemy_in_path(self):
        """
        Prueba que el rey no pueda moverse a una casilla bloqueada por una pieza enemiga en el camino.
        Funcionalidad:
        - Coloca una pieza enemiga en una casilla cercana y verifica que el rey no pueda moverse a través de ella.
        """
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        self.board.set_piece(5, 5, Rook("BLACK", self.board))  

        is_valid = king.valid_positions(4, 4, 6, 6)
        self.assertFalse(is_valid) 



   
if __name__ == '__main__':
    unittest.main()