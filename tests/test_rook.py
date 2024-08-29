import unittest
from chess.rook import Rook
from chess.board import Board

class TestRook(unittest.TestCase):
    
    def test_rook_white_str(self):
        board = Board()
        rook = Rook("WHITE", board)  # Instancia de torre blanca
        self.assertEqual(str(rook), "♖")  # Prueba que el método __str__ devuelva el símbolo correcto para una torre blanca.

    def test_rook_black_str(self):
        board = Board()
        rook = Rook("BLACK", board)  # Instancia de torre negra
        self.assertEqual(str(rook), "♜")  # Prueba que el método __str__ devuelva el símbolo correcto para una torre negra.


if __name__ == '__main__':
    unittest.main()