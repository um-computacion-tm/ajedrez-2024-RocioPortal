import unittest
from chess.knight import Knight
from chess.board import Board

class TestKnight(unittest.TestCase):
    def test_str(self):
        board = Board()
        knight = Knight("WHITE", board)
        self.assertEqual(
            str(knight),
            "♞",
        )       

    def setUp(self):
        self.board = Board(for_test=True)

    def test_knight_move(self):
        knight = Knight("WHITE", self.board)
        self.board.set_piece(4, 4, knight)
        is_valid = knight.valid_positions(4, 4, 6, 5)
        self.assertTrue(is_valid)

    def test_knight_blocked_by_own_piece(self):
        knight = Knight("WHITE", self.board)
        self.board.set_piece(4, 4, knight)
        self.board.set_piece(6, 5, Knight("WHITE", self.board))
        is_valid = knight.valid_positions(4, 4, 6, 5)
        self.assertFalse(is_valid)

    def test_knight_invalid_move(self):
        knight = Knight("WHITE", self.board)
        self.board.set_piece(4, 4, knight)
        is_valid = knight.valid_positions(4, 4, 5, 5)  # No es un movimiento en "L"
        self.assertFalse(is_valid)

    def test_knight_capture_enemy(self):
        knight = Knight("WHITE", self.board)
        self.board.set_piece(4, 4, knight)
        self.board.set_piece(6, 5, Knight("BLACK", self.board))  # Pieza enemiga
        is_valid = knight.valid_positions(4, 4, 6, 5)
        self.assertTrue(is_valid)



if __name__ == '__main__':
    unittest.main()