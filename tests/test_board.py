import unittest
from chess.board import Board


class TestBoard(unittest.TestCase):
    def test_str_board(self):
        board = Board()
        self.assertEqual(
            str(board),
            (
                "♖♘♗♕♔♗♘♖\n"
                "♙♙♙♙♙♙♙♙\n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "♟♟♟♟♟♟♟♟\n"
                "♜♞♝♛♚♝♞♜\n"
            )
        )