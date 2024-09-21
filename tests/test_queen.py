import unittest
from chess.queen import Queen
from chess.rook import Rook
from chess.board import Board

class TestQueen(unittest.TestCase):

    def test_str(self):
        board = Board()
        queen = Queen("WHITE", board)
        self.assertEqual(
            str(queen),
            "♛",
        )

    def setUp(self):
        # Se inicializa un tablero para los tests
        self.board = Board(for_test=True)

    def test_queen_move_orthogonal_vertical(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)  # Colocamos la reina en (4, 4)

        # Verifica si la reina puede moverse verticalmente hacia abajo (de (4, 4) a (7, 4))
        is_valid = queen.valid_positions(4, 4, 7, 4)
        self.assertTrue(is_valid)  # El movimiento debería ser válido

        # Verifica si la reina puede moverse horizontalmente hacia la derecha (de (4, 4) a (4, 7))
        is_valid = queen.valid_positions(4, 4, 4, 7)
        self.assertTrue(is_valid)  # El movimiento debería ser válido

    def test_queen_move_diagonal(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)  # Colocamos la reina en (4, 4)

        # Verifica si la reina puede moverse en diagonal hacia (7, 7)
        is_valid = queen.valid_positions(4, 4, 7, 7)
        self.assertTrue(is_valid)  # El movimiento debería ser válido

    def test_queen_blocked_by_own_piece(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)  # Colocamos la reina en (4, 4)
        self.board.set_piece(6, 4, Queen("WHITE", self.board))  # Colocamos una pieza blanca en (6, 4)

        # Verifica que la reina no pueda moverse a (7, 4) porque está bloqueada por su propia pieza
        is_valid = queen.valid_positions(4, 4, 7, 4)
        self.assertFalse(is_valid)  # El movimiento debería ser inválido

    def test_queen_capture_enemy(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)  # Colocamos la reina en (4, 4)
        self.board.set_piece(6, 4, Queen("BLACK", self.board))  # Colocamos una pieza enemiga en (6, 4)

        # Verifica si la reina puede capturar la pieza enemiga en (6, 4)
        is_valid = queen.valid_positions(4, 4, 6, 4)
        self.assertTrue(is_valid)  # El movimiento debería ser válido

    def test_queen_blocked_by_enemy(self):
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)  # Colocamos la reina en (4, 4)
        self.board.set_piece(6, 4, Queen("BLACK", self.board))  # Colocamos una pieza enemiga en (6, 4)

        # Verifica que la reina no pueda moverse más allá de la pieza enemiga en (7, 4)
        is_valid = queen.valid_positions(4, 4, 7, 4)
        self.assertFalse(is_valid)  # El movimiento debería ser inválido
if __name__ == '__main__':
    unittest.main()