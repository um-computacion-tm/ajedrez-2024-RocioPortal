import unittest
from chess.bishop import Bishop
from chess.board import Board

class TestBishop(unittest.TestCase):

    def test_str(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        self.assertEqual(
            str(bishop),
            "♝",
        )
    def setUp(self):
        self.board = Board(for_test=True)

    def test_bishop_move_diagonal(self):
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        is_valid = bishop.valid_positions(4, 4, 7, 7)
        self.assertTrue(is_valid)

    def test_bishop_blocked_by_own_piece(self):
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        self.board.set_piece(5, 5, Bishop("WHITE", self.board))
        is_valid = bishop.valid_positions(4, 4, 7, 7)
        self.assertFalse(is_valid)

    def test_bishop_capture_enemy(self):
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        self.board.set_piece(5, 5, Bishop("BLACK", self.board))
        is_valid = bishop.valid_positions(4, 4, 5, 5)
        self.assertTrue(is_valid)

    def test_bishop_blocked_by_own_piece(self):
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        self.board.set_piece(5, 5, Bishop("WHITE", self.board))  # Bloqueo por pieza propia
        is_valid = bishop.valid_positions(4, 4, 6, 6)
        self.assertFalse(is_valid)

    def test_bishop_capture_enemy_diagonal(self):
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        self.board.set_piece(6, 6, Bishop("BLACK", self.board))  # Pieza enemiga
        is_valid = bishop.valid_positions(4, 4, 6, 6)
        self.assertTrue(is_valid)  # La captura debería ser válida

    def test_bishop_move_out_of_bounds(self):
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(0, 0, bishop)
        is_valid = bishop.valid_positions(0, 0, -1, -1)  # Movimiento fuera del tablero
        self.assertFalse(is_valid)

    def test_bishop_move_orthogonal(self):
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, bishop)
        is_valid = bishop.valid_positions(4, 4, 4, 6)  # Intento de movimiento horizontal
        self.assertFalse(is_valid)

    def test_bishop_long_move_diagonal(self):
        bishop = Bishop("WHITE", self.board)
        self.board.set_piece(1, 1, bishop)
        is_valid = bishop.valid_positions(1, 1, 7, 7)  # Movimiento diagonal largo sin bloqueo
        self.assertTrue(is_valid)


if __name__ == '__main__':
    unittest.main()