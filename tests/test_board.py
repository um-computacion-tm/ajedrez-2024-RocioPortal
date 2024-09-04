import unittest
from chess.board import Board
from chess.rook import Rook
from chess.pawn import Pawn


class TestBoard(unittest.TestCase):

    def test_str_board(self):                #Inicializa el tablero y compara la salida esperada con la real utilizando simbolos
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

    def test_set_piece(self):
        # Verificar que se puede colocar una pieza en una posición específica
        new_pawn = Pawn("BLACK")
        self.board.set_piece(4, 4, new_pawn)
        piece = self.board.get_piece(4, 4)
        self.assertIsInstance(piece, Pawn)
        self.assertEqual(piece.get_color, "BLACK")

if __name__ == '__main__':
    unittest.main()