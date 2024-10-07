
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

    def test_pawn_promotion(self):
        # Verificar que el peón se promueve a reina cuando llega al final
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(1, 4, pawn)  # Colocamos el peón en (1, 4)

        pawn.verify_promote(0, 4)  # Simular que llega a la última fila
        piece = self.board.get_piece(0, 4)
        self.assertIsInstance(piece, Queen)  # Debería haberse convertido en una reina

    def test_pawn_out_of_bounds(self):
        # Verificar que los movimientos fuera de los límites del tablero no sean válidos
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(0, 4, pawn)  # Peón en la primera fila

        moves = pawn.get_possible_moves(0, 4)
        self.assertNotIn((-1, 4), moves)  # No puede moverse fuera del tablero


"""
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
"""


if __name__ == '__main__':
    unittest.main()