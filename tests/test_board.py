import unittest
from chess.board import Board
from chess.rook import Rook
from chess.pawn import Pawn
from chess.exceptions import OutOfBoard


class TestBoard(unittest.TestCase):

    def test_str_board(self):
        board = Board()
        expected_str = (
            "    0    1    2    3    4    5    6    7 \n"
            "0   ♖    ♘    ♗    ♕    ♔    ♗    ♘    ♖  \n\n"
            "1   ♙    ♙    ♙    ♙    ♙    ♙    ♙    ♙  \n\n"
            "2   .    .    .    .    .    .    .    .  \n\n"
            "3   .    .    .    .    .    .    .    .  \n\n"
            "4   .    .    .    .    .    .    .    .  \n\n"
            "5   .    .    .    .    .    .    .    .  \n\n"
            "6   ♟    ♟    ♟    ♟    ♟    ♟    ♟    ♟  \n\n"
            "7   ♜    ♞    ♝    ♛    ♚    ♝    ♞    ♜  \n\n"
        )
        self.assertEqual(str(board), expected_str)

    def setUp(self):
        self.board = Board()

    def test_initial_positions(self):
        # Verificar que las piezas están en las posiciones correctas
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertEqual(self.board.get_piece(0, 0).get_color, "BLACK")
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertEqual(self.board.get_piece(7, 0).get_color, "WHITE")
        self.assertIsInstance(self.board.get_piece(1, 0), Pawn)
        self.assertEqual(self.board.get_piece(1, 0).get_color, "BLACK")
        self.assertIsInstance(self.board.get_piece(6, 0), Pawn)
        self.assertEqual(self.board.get_piece(6, 0).get_color, "WHITE")

    def test_get_piece(self):
        # Verificar que get_piece devuelve la pieza correcta
        rook = self.board.get_piece(0, 0)
        self.assertIsInstance(rook, Rook)
        self.assertEqual(rook.get_color, "BLACK")

        pawn = self.board.get_piece(6, 0)
        self.assertIsInstance(pawn, Pawn)
        self.assertEqual(pawn.get_color, "WHITE")

        pawn = self.board.get_piece(1, 0)
        self.assertIsInstance(pawn, Pawn)
        self.assertEqual(pawn.get_color, "BLACK")

    def test_set_piece(self):
        # Verificar que se puede colocar una pieza en una posición específica
        new_pawn = Pawn("BLACK", self.board)
        self.board.set_piece(4, 4, new_pawn)
        piece = self.board.get_piece(4, 4)
        self.assertIsInstance(piece, Pawn)
        self.assertEqual(piece.get_color, "BLACK")

    def test_move(self):
        board = Board(for_test=True)
        rook = Rook(color='BLACK', board=board)
        board.set_piece(0, 0, rook)

        board.move(
            from_row=0,
            from_col=0,
            to_row=2,
            to_col=0,
        )
        
        self.assertIsInstance(
            board.get_piece(2, 0),
            Rook,
        )
        self.assertEqual(
            str(board),
            (
                "    0    1    2    3    4    5    6    7 \n"  
                "0   .    .    .    .    .    .    .    .  \n\n"
                "1   .    .    .    .    .    .    .    .  \n\n"
                "2   ♖    .    .    .    .    .    .    .  \n\n"
                "3   .    .    .    .    .    .    .    .  \n\n"
                "4   .    .    .    .    .    .    .    .  \n\n"
                "5   .    .    .    .    .    .    .    .  \n\n"
                "6   .    .    .    .    .    .    .    .  \n\n"
                "7   .    .    .    .    .    .    .    .  \n\n"
            )
        )

    def test_get_piece_out_of_range(self):
        board = Board(for_test=True)

        with self.assertRaises(OutOfBoard) as exc:
            board.get_piece(10, 10)

        self.assertEqual(
            exc.exception.message,
            "La posicion indicada se encuentra fuera del tablero"
        )

if __name__ == '__main__':
    unittest.main()