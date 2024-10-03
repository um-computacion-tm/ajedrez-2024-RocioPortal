import unittest
from chess.board import Board
from chess.king import King

class TestKing(unittest.TestCase):

    def test_str(self):
        board = Board()
        king = King("WHITE", board)
        self.assertEqual(
            str(king),
            "♚",
        )

    def setUp(self):
        self.board = Board(for_test=True)

    def test_king_move_one_square(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)

        # Verifica si el rey puede moverse una casilla en diagonal
        is_valid = king.valid_positions(4, 4, 5, 5)
        self.assertTrue(is_valid)

    def test_king_blocked_by_own_piece(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        self.board.set_piece(5, 5, King("WHITE", self.board))  # Pieza blanca bloqueando

        # Verifica que el rey no pueda moverse si hay una pieza propia bloqueando
        is_valid = king.valid_positions(4, 4, 5, 5)
        self.assertFalse(is_valid)

    def test_king_move_two_squares_invalid(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)

        # El rey no debería poder moverse dos casillas (movimiento inválido)
        is_valid = king.valid_positions(4, 4, 6, 4)
        self.assertFalse(is_valid)

    def test_king_move_too_far(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        is_valid = king.valid_positions(4, 4, 6, 6)  # Más de un paso
        self.assertFalse(is_valid)

    def test_king_blocked_by_own_piece(self):
        king = King("WHITE", self.board)
        self.board.set_piece(4, 4, king)
        self.board.set_piece(5, 5, King("WHITE", self.board))  # Pieza propia
        is_valid = king.valid_positions(4, 4, 5, 5)
        self.assertFalse(is_valid)

if __name__ == '__main__':
    unittest.main()