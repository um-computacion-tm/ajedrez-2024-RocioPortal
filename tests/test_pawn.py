
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

    def test_pawn_move_forward_one_step(self):
        # Test de movimiento hacia adelante por una casilla
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(6, 4, pawn)
        
        # El peón debe poder moverse hacia adelante una casilla
        is_valid = pawn.valid_positions(6, 4, 5, 4)
        self.assertTrue(is_valid)

    def test_pawn_move_forward_two_steps_initial(self):
        # Test de movimiento hacia adelante por dos casillas desde la fila inicial
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(6, 4, pawn)
        
        is_valid = pawn.valid_positions(6, 4, 4, 4)
        self.assertTrue(is_valid)

    def test_pawn_blocked_move(self):
        # Test de movimiento bloqueado
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(6, 4, pawn)
        blocking_pawn = Pawn("WHITE", self.board)
        self.board.set_piece(5, 4, blocking_pawn)
        
        # El peón no debe poder moverse hacia adelante si está bloqueado
        is_valid = pawn.valid_positions(6, 4, 5, 4)
        self.assertFalse(is_valid)

    def test_pawn_capture_diagonal(self):
        # Test de captura en diagonal
        pawn = Pawn("WHITE", self.board)
        enemy_pawn = Pawn("BLACK", self.board)
        self.board.set_piece(6, 4, pawn)
        self.board.set_piece(5, 5, enemy_pawn)

        is_valid = pawn.valid_positions(6, 4, 5, 5)
        self.assertTrue(is_valid)

    def test_pawn_invalid_diagonal_no_capture(self):
        # Test de movimiento diagonal inválido si no hay pieza enemiga
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(6, 4, pawn)

        is_valid = pawn.valid_positions(6, 4, 5, 5)
        self.assertFalse(is_valid)

    def test_pawn_promotion(self):
        # Test de promoción de peón
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(1, 4, pawn)

        # Mover el peón a la fila de promoción
        pawn.verify_promote(0, 4)

        # Verificar si el peón fue promovido a reina
        promoted_piece = self.board.get_piece(0, 4)
        self.assertIsInstance(promoted_piece, Queen)

    def test_pawn_no_promotion_before_final_row(self):
        # Test de que el peón no se promueve antes de llegar a la fila final
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(2, 4, pawn)

        # No debe haber promoción antes de la fila final
        pawn.verify_promote(2, 4)
        promoted_piece = self.board.get_piece(2, 4)
        self.assertNotIsInstance(promoted_piece, Queen)  # Debe seguir siendo un peón



if __name__ == '__main__':
    unittest.main()