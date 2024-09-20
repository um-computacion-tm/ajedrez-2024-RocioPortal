import unittest
from chess.rook import Rook
from chess.board import Board
from chess.pawn import Pawn


class TestRook(unittest.TestCase):

    def test_str(self):
        board = Board()
        rook = Rook("WHITE", board)
        self.assertEqual(
            str(rook),
            "♜",
        )

    def setUp(self):
        self.board = Board(for_test=True)

    def test_rook_move_vertical(self):
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 4, rook)
        is_valid = rook.valid_positions(4, 4, 7, 4)
        self.assertTrue(is_valid)

    def test_rook_move_horizontal(self):
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 4, rook)
        is_valid = rook.valid_positions(4, 4, 4, 7)
        self.assertTrue(is_valid)

    def test_rook_blocked_by_own_piece(self):
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 4, rook)
        self.board.set_piece(5, 4, Rook("WHITE", self.board))
        is_valid = rook.valid_positions(4, 4, 7, 4)
        self.assertFalse(is_valid)

    def test_rook_capture_enemy(self):
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 4, rook)
        self.board.set_piece(5, 4, Rook("BLACK", self.board))
        is_valid = rook.valid_positions(4, 4, 5, 4)
        self.assertTrue(is_valid)

    def test_rook_blocked_by_enemy_in_path(self):
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 4, rook)
        self.board.set_piece(5, 4, Rook("BLACK", self.board))  # Pieza enemiga en el camino
        is_valid = rook.valid_positions(4, 4, 6, 4)
        self.assertFalse(is_valid)  # El movimiento debería ser inválido

    def test_rook_invalid_diagonal_move(self):
        rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 4, rook)
        is_valid = rook.valid_positions(4, 4, 5, 5)  # Intentar moverse en diagonal
        self.assertFalse(is_valid)  # El movimiento debería ser inválido


if __name__ == '__main__':
    unittest.main()