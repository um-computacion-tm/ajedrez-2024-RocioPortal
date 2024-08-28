import unittest
from chess.board import Board


class TestBoard(unittest.TestCase):

    def test_str_board(self):                #Inicializa el tablero y compara la salida esperada con la real utilizando simbolos
        board = Board()
        self.assertEqual(
            str(board),
            (
                "♜♞♝♛♚♝♞♜\n"
                "♟♟♟♟♟♟♟♟\n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "♙♙♙♙♙♙♙♙\n"
                "♖♘♗♕♔♗♘♖\n"
            )
        )

    def setUp(self):
        self.board = Board()