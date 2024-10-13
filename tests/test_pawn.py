
import unittest
from chess.pawn import Pawn
from chess.board import Board
from chess.rook import Rook

class TestPawn(unittest.TestCase):

    def test_str(self):
        board = Board()
        pawn = Pawn("WHITE", board)
        self.assertEqual(
            str(pawn),
            "♟",
        )

    def setUp(self):
        self.board = Board(for_test=True)

    def test_pawn_move_forward(self):
        # Peón blanco en (6, 4) debería poder moverse una casilla adelante
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(6, 4, pawn)
        moves = pawn.get_possible_moves(6, 4)
        self.assertIn((5, 4), moves)
        self.assertNotIn((6, 4), moves)

    def test_pawn_double_move_initial_position(self):
        # Peón blanco en la fila inicial (6, 4) debería poder moverse dos casillas adelante
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(6, 4, pawn)
        moves = pawn.get_possible_moves(6, 4)
        self.assertIn((4, 4), moves)  # Movimiento de dos casillas

        # Peón negro en la fila inicial (1, 4) debería poder moverse dos casillas adelante
        pawn_black = Pawn("BLACK", self.board)
        self.board.set_piece(1, 4, pawn_black)
        moves = pawn_black.get_possible_moves(1, 4)
        self.assertIn((3, 4), moves)  # Movimiento de dos casillas

    def test_pawn_blocked_by_piece(self):
        # Peón blanco no debería poder moverse si hay una pieza en frente
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(6, 4, pawn)
        blocking_piece = Pawn("BLACK", self.board)
        self.board.set_piece(5, 4, blocking_piece)
        moves = pawn.get_possible_moves(6, 4)
        self.assertNotIn((5, 4), moves)  # No puede moverse si está bloqueado

    def test_pawn_capture_diagonal(self):
        # Peón blanco debería poder capturar en diagonal
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(4, 4, pawn)

        # Colocar una pieza negra en diagonal
        enemy_piece = Pawn("BLACK", self.board)
        self.board.set_piece(3, 5, enemy_piece)

        # Usar el método que maneja tanto movimientos como capturas
        captures = pawn.get_possible_moves(4, 4)  # Asumiendo que el método ahora maneja capturas también
        self.assertIn((3, 5), captures)  # Puede capturar en (3, 5)

    def test_pawn_cannot_capture_forward(self):
        # Peón blanco no debería poder capturar hacia adelante
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(4, 4, pawn)

        # Colocar una pieza negra en frente
        enemy_piece = Pawn("BLACK", self.board)
        self.board.set_piece(3, 4, enemy_piece)

        moves = pawn.get_possible_moves(4, 4)
        self.assertNotIn((3, 4), moves)  # No puede capturar hacia adelante

    def test_pawn_out_of_bounds(self):
        # Verificar que los movimientos fuera de los límites del tablero no sean válidos
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(0, 4, pawn)  # Peón en la primera fila

        moves = pawn.get_possible_moves(0, 4)
        self.assertNotIn((-1, 4), moves)  # No puede moverse fuera del tablero

if __name__ == '__main__':
    unittest.main()