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

    def test_move_vertical_desc(self):
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

    def test_move_vertical_asc(self):
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions_va(4, 1)
        self.assertEqual(
            possibles,
            [(3, 1), (2, 1), (1, 1), (0, 1)]
        )

    def test_move_vertical_desc_with_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("WHITE", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

    def test_move_vertical_desc_with_not_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("BLACK", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1)]
        )

    def test_move_horizontal_left(self):
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions_hl(4, 4)
        self.assertEqual(
            possibles,
            [(4, 3), (4, 2), (4, 1), (4, 0)]
        )

    def test_move_horizontal_left_with_own_piece(self):
        board = Board()
        board.set_piece(4, 2, Pawn("WHITE", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 4, rook)
        possibles = rook.possible_positions_hl(4, 4)
        self.assertEqual(
            possibles,
            [(4, 3)]
        )

    def test_move_horizontal_left_with_not_own_piece(self):
        board = Board()
        board.set_piece(4, 2, Pawn("BLACK", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 4, rook)
        possibles = rook.possible_positions_hl(4, 4)
        self.assertEqual(
            possibles,
            [(4, 3), (4, 2)]
        )



'''
class TestRook(unittest.TestCase):
    
    def test_rook_white_str(self):
        board = Board()
        rook = Rook("WHITE", board)  # Instancia de torre blanca
        self.assertEqual(str(rook), "♖")  # Prueba que el método __str__ devuelva el símbolo correcto para una torre blanca.

    def test_rook_black_str(self):
        board = Board()
        rook = Rook("BLACK", board)  # Instancia de torre negra
        self.assertEqual(str(rook), "♜")  # Prueba que el método __str__ devuelva el símbolo correcto para una torre negra.

'''


if __name__ == '__main__':
    unittest.main()