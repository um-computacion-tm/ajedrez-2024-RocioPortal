
import unittest
from chess.pawn import Pawn
from chess.board import Board
from chess.rook import Rook

class TestPawn(unittest.TestCase):
    """
    Clase de pruebas para la pieza `Pawn` en el juego de ajedrez.
    """

    def test_str(self):
        """
        Prueba que la representación en cadena (str) del peón sea correcta.
        Funcionalidad:
        - Verifica que el símbolo del peón blanco sea "♟".
        """
        board = Board()
        pawn = Pawn("WHITE", board)
        self.assertEqual(
            str(pawn),
            "♟",
        )

    def setUp(self):
        """
        Configuración inicial para cada prueba.
        Funcionalidad:
        - Crea un nuevo tablero de prueba antes de ejecutar cada test.
        """
        self.board = Board(for_test=True)

    def test_pawn_move_forward(self):
        """
        Prueba que el peón pueda moverse una casilla hacia adelante.
        Funcionalidad:
        - Verifica que el peón blanco pueda moverse una casilla hacia adelante desde su posición inicial.
        """
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(6, 4, pawn)
        moves = pawn.get_possible_moves(6, 4)
        self.assertIn((5, 4), moves)
        self.assertNotIn((6, 4), moves) 

    def test_pawn_double_move_initial_position(self):
        """
        Prueba que el peón pueda moverse dos casillas adelante desde la posición inicial.
        Funcionalidad:
        - Verifica que el peón blanco pueda avanzar dos casillas en su primer movimiento.
        - Verifica que el peón negro pueda avanzar dos casillas en su primer movimiento.
        """
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(6, 4, pawn)
        moves = pawn.get_possible_moves(6, 4)
        self.assertIn((4, 4), moves)  

        pawn_black = Pawn("BLACK", self.board)
        self.board.set_piece(1, 4, pawn_black)
        moves = pawn_black.get_possible_moves(1, 4)
        self.assertIn((3, 4), moves) 

    def test_pawn_blocked_by_piece(self):
        """
        Prueba que el peón no pueda avanzar si hay una pieza bloqueando su camino.
        Funcionalidad:
        - Verifica que un peón blanco no pueda moverse hacia adelante si una pieza está en frente.
        """
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(6, 4, pawn)
        blocking_piece = Pawn("BLACK", self.board)
        self.board.set_piece(5, 4, blocking_piece)
        moves = pawn.get_possible_moves(6, 4)
        self.assertNotIn((5, 4), moves)  

    def test_pawn_capture_diagonal(self):
        """
        Prueba que el peón pueda capturar una pieza enemiga en diagonal.
        Funcionalidad:
        - Coloca un peón blanco en el tablero y una pieza enemiga en diagonal para verificar que pueda capturarla.
        """
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(4, 4, pawn)

        enemy_piece = Pawn("BLACK", self.board)
        self.board.set_piece(3, 5, enemy_piece)

        captures = pawn.get_possible_moves(4, 4)
        self.assertIn((3, 5), captures) 

    def test_pawn_cannot_capture_forward(self):
        """
        Prueba que el peón no pueda capturar piezas hacia adelante.
        Funcionalidad:
        - Verifica que el peón blanco no pueda capturar una pieza directamente en frente de él.
        """
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(4, 4, pawn)

        enemy_piece = Pawn("BLACK", self.board)
        self.board.set_piece(3, 4, enemy_piece)

        moves = pawn.get_possible_moves(4, 4)
        self.assertNotIn((3, 4), moves) 

    def test_pawn_out_of_bounds(self):
        """
        Prueba que el peón no pueda moverse fuera de los límites del tablero.
        Funcionalidad:
        - Verifica que un peón blanco no pueda moverse fuera del tablero desde la primera fila.
        """
        pawn = Pawn("WHITE", self.board)
        self.board.set_piece(0, 4, pawn) 

        moves = pawn.get_possible_moves(0, 4)
        self.assertNotIn((-1, 4), moves)  # No puede moverse fuera del tablero

if __name__ == '__main__':
    unittest.main()