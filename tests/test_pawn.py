
import unittest
from chess.pawn import Pawn
from chess.board import Board
from chess.rook import Rook
from chess.queen import Queen


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
        # Crear un peón blanco en (6, 4) y verificar su movimiento hacia adelante
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(6, 4, pawn)
        
        # Verificar que puede moverse a (5, 4)
        is_valid = pawn.valid_positions(6, 4, 5, 4)
        self.assertTrue(is_valid)

        # Verificar que no puede moverse a una casilla ocupada (directamente adelante)
        self.board.set_piece(5, 4, Pawn("WHITE", self.board))
        is_valid = pawn.valid_positions(6, 4, 5, 4)
        self.assertFalse(is_valid)

    def test_pawn_initial_two_step_move(self):
        # Crear un peón blanco en su posición inicial (6, 4)
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(6, 4, pawn)
        
        # Verificar que puede moverse dos casillas hacia adelante (a (4, 4))
        is_valid = pawn.valid_positions(6, 4, 4, 4)
        self.assertTrue(is_valid)

    def test_pawn_capture_enemy(self):
        # Crear un peón blanco en (6, 4) y un enemigo en (5, 3)
        pawn = Pawn("WHITE", self.board)
        enemy_rook = Rook("BLACK", self.board)
        self.board.set_piece(6, 4, pawn)
        self.board.set_piece(5, 3, enemy_rook)
        
        # Verificar que el peón puede capturar en diagonal a (5, 3)
        is_valid = pawn.valid_positions(6, 4, 5, 3)
        self.assertTrue(is_valid)

    def test_pawn_capture_own_piece(self):
        # Crear un peón blanco en (6, 4) y una torre blanca en (5, 3)
        pawn = Pawn("WHITE", self.board)
        own_rook = Rook("WHITE", self.board)
        self.board.set_piece(6, 4, pawn)
        self.board.set_piece(5, 3, own_rook)
        
        # Verificar que el peón NO puede capturar su propia pieza en diagonal
        is_valid = pawn.valid_positions(6, 4, 5, 3)
        self.assertFalse(is_valid)

    def test_pawn_blocked_move(self):
        # Crear un peón blanco en (6, 4) y una torre (bloqueo) en (5, 4)
        pawn = Pawn("WHITE", self.board)
        blocking_rook = Rook("BLACK", self.board)
        self.board.set_piece(6, 4, pawn)
        self.board.set_piece(5, 4, blocking_rook)
        
        # Verificar que el peón NO puede avanzar a (5, 4)
        is_valid = pawn.valid_positions(6, 4, 5, 4)
        self.assertFalse(is_valid)  # Este movimiento no debería ser válido

    def test_pawn_black_moves(self):
        # Crear un peón negro en su posición inicial (1, 4)
        pawn = Pawn("BLACK", self.board)
        self.board.set_piece(1, 4, pawn)
        
        # Verificar que puede avanzar dos casillas a (3, 4)
        is_valid = pawn.valid_positions(1, 4, 3, 4)
        self.assertTrue(is_valid)
        
        # Verificar que puede avanzar una casilla a (2, 4)
        is_valid = pawn.valid_positions(1, 4, 2, 4)
        self.assertTrue(is_valid)

    def test_pawn_promotion(self):
        # Verificar que el peón se promueva a reina al llegar a la última fila
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(1, 4, pawn)  # Colocar peón blanco en (1, 4)
        
        # El peón se mueve a (0, 4) y debe promocionar a reina
        pawn.verify_promote(0, 4)
        
        promoted_piece = self.board.get_piece(0, 4)
        # Verificar que ahora hay una reina en la posición (0, 4)
        self.assertIsInstance(promoted_piece, Queen)

"""
    def test_initial_black(self):
        board = Board(for_test = True)
        pawn = Pawn("BLACK", board)

        possibles = pawn.get_possible_positions(1, 5)
        self.assertEqual(
            possibles,
            [(2, 5), (3, 5)]
        )

    def test_not_initial_black(self):
        board = Board(for_test = True)
        pawn = Pawn("BLACK", board)

        possibles = pawn.get_possible_positions(2, 5)
        self.assertEqual(
            possibles,
            [(3, 5)]
        )

    def test_eat_left_black(self):
        board = Board(for_test = True)
        pawn = Pawn("BLACK", board)
        board.set_piece(3, 6, Pawn("WHITE", board))

        possibles = pawn.get_possible_positions(2, 5)
        self.assertEqual(
            possibles,
            [(3, 5), (3, 6)]
        )

    def test_initial_white(self):
        board = Board(for_test = True)
        pawn = Pawn("WHITE", board)

        possibles = pawn.get_possible_positions(6, 4)
        self.assertEqual(
            possibles,
            [(5, 4), (4, 4)]
        )

    def test_not_initial_white(self):
        board = Board(for_test = True)
        pawn = Pawn("WHITE", board)

        possibles = pawn.get_possible_positions(5, 4)
        self.assertEqual(
            possibles,
            [(4, 4)]
        )

    def test_not_initial_white_block(self):
        board = Board(for_test = True)
        pawn = Pawn("WHITE", board)
        board.set_piece(4, 4, Pawn("BLACK", board))

        possibles = pawn.get_possible_positions(5, 4)
        self.assertEqual(
            possibles,
            []
        )

    def test_not_initial_black_block(self):
        board = Board(for_test = True)
        pawn = Pawn("BLACK", board)
        board.set_piece(5, 4, Pawn("BLACK", board))

        possibles = pawn.get_possible_positions(4, 4)
        self.assertEqual(
            possibles,
            []
        )

"""

if __name__ == '__main__':
    unittest.main()