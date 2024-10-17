import unittest
from chess.rook import Rook
from chess.board import Board
from chess.pawn import Pawn


class TestRook(unittest.TestCase):
    """
    Clase de pruebas para la pieza `Rook`en el juego de ajedrez.
    """

    def test_str(self):
        """
        Prueba que la representación en cadena (str) de la torre sea correcta.
        Funcionalidad:
        - Verifica que el símbolo de la torre blanca sea "♜".
        """
        board = Board()
        rook = Rook("WHITE", board)
        self.assertEqual(
            str(rook),
            "♜",
        )

    def setUp(self):
        """
        Configuración inicial para cada prueba.
        Funcionalidad:
        - Crea un nuevo tablero de prueba antes de ejecutar cada test.
        """
        self.board = Board(for_test=True)

    def test_rook_move_vertical(self):
        """
        Prueba que la torre pueda moverse verticalmente.
        Funcionalidad:
        - Verifica que la torre blanca pueda moverse verticalmente en el tablero.
        """
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 4, rook)
        is_valid = rook.valid_positions(4, 4, 7, 4)
        self.assertTrue(is_valid)  

    def test_rook_move_horizontal(self):
        """
        Prueba que la torre pueda moverse horizontalmente.
        Funcionalidad:
        - Verifica que la torre blanca pueda moverse horizontalmente en el tablero.
        """
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 4, rook)
        is_valid = rook.valid_positions(4, 4, 4, 7)
        self.assertTrue(is_valid)  

    def test_rook_blocked_by_own_piece(self):
        """
        Prueba que la torre no pueda moverse si una pieza propia bloquea su camino.
        Funcionalidad:
        - Coloca una pieza propia delante de la torre y verifica que la torre no pueda avanzar.
        """
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 4, rook)
        self.board.set_piece(5, 4, Rook("WHITE", self.board))  
        is_valid = rook.valid_positions(4, 4, 7, 4)
        self.assertFalse(is_valid) 

    def test_rook_capture_enemy(self):
        """
        Prueba que la torre pueda capturar una pieza enemiga.
        Funcionalidad:
        - Coloca una pieza enemiga en una casilla válida y verifica que la torre pueda capturarla.
        """
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 4, rook)
        self.board.set_piece(5, 4, Rook("BLACK", self.board))  
        is_valid = rook.valid_positions(4, 4, 5, 4)
        self.assertTrue(is_valid)  

    def test_rook_blocked_by_enemy_in_path(self):
        """
        Prueba que la torre no pueda moverse más allá de una pieza enemiga en su camino.
        Funcionalidad:
        - Verifica que la torre no pueda avanzar más allá de una pieza enemiga en su trayectoria.
        """
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 4, rook)
        self.board.set_piece(5, 4, Rook("BLACK", self.board)) 
        is_valid = rook.valid_positions(4, 4, 6, 4)
        self.assertFalse(is_valid)  

    def test_rook_invalid_diagonal_move(self):
        """
        Prueba que la torre no pueda moverse en diagonal.
        Funcionalidad:
        - Verifica que la torre no pueda moverse en diagonal, ya que solo se mueve ortogonalmente.
        """
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 4, rook)
        is_valid = rook.valid_positions(4, 4, 5, 5)  
        self.assertFalse(is_valid) 

    def test_rook_move_out_of_bounds(self):
        """
        Prueba que la torre no pueda moverse fuera de los límites del tablero.
        Funcionalidad:
        - Verifica que la torre no pueda moverse fuera del tablero.
        """
        rook = Rook("WHITE", self.board)
        self.board.set_piece(0, 0, rook)
        is_valid = rook.valid_positions(0, 0, -1, 0) 
        self.assertFalse(is_valid)  

    def test_rook_blocked_by_pawn(self):
        """
        Prueba que la torre no pueda moverse si está bloqueada por un peón.
        Funcionalidad:
        - Coloca un peón propio frente a la torre y verifica que la torre no pueda moverse a través de él.
        """
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 4, rook)
        self.board.set_piece(5, 4, Pawn("WHITE", self.board))
        is_valid = rook.valid_positions(4, 4, 7, 4)
        self.assertFalse(is_valid)  

    def test_rook_can_capture_enemy_pawn(self):
        """
        Prueba que la torre pueda capturar un peón enemigo.
        Funcionalidad:
        - Verifica que la torre pueda capturar una pieza enemiga en su trayectoria.
        """
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 4, rook)
        self.board.set_piece(5, 4, Pawn("BLACK", self.board))  
        is_valid = rook.valid_positions(4, 4, 5, 4)
        self.assertTrue(is_valid) 


if __name__ == '__main__':
    unittest.main()