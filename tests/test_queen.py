import unittest
from chess.queen import Queen
from chess.rook import Rook
from chess.board import Board
from chess.pawn import Pawn

class TestQueen(unittest.TestCase):
    """
    Clase de pruebas para la pieza `Queen` en el juego de ajedrez.
    """

    def test_str(self):
        """
        Prueba que la representación en cadena (str) de la reina sea correcta.
        Funcionalidad:
        - Verifica que el símbolo de la reina blanca sea "♛".
        """
        board = Board()
        queen = Queen("WHITE", board)
        self.assertEqual(
            str(queen),
            "♛",
        )

    def setUp(self):
        """
        Configuración inicial para cada prueba.
        Funcionalidad:
        - Crea un nuevo tablero de prueba antes de ejecutar cada test.
        """
        self.board = Board(for_test=True)

    def test_queen_move_orthogonal_vertical(self):
        """
        Prueba que la reina pueda moverse en direcciones ortogonales.
        Funcionalidad:
        - Verifica que la reina pueda moverse tanto vertical como horizontalmente en el tablero.
        """
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen) 

        is_valid = queen.valid_positions(4, 4, 7, 4)
        self.assertTrue(is_valid)  

        is_valid = queen.valid_positions(4, 4, 4, 7)
        self.assertTrue(is_valid)  

    def test_queen_move_diagonal(self):
        """
        Prueba que la reina pueda moverse en diagonal.
        Funcionalidad:
        - Verifica que la reina pueda moverse diagonalmente en el tablero.
        """
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)  

        is_valid = queen.valid_positions(4, 4, 7, 7)
        self.assertTrue(is_valid)  

    def test_queen_blocked_by_own_piece(self):
        """
        Prueba que la reina no pueda moverse si hay una pieza propia bloqueando.
        Funcionalidad:
        - Verifica que la reina no pueda avanzar si una pieza del mismo color bloquea su camino.
        """
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)  
        self.board.set_piece(6, 4, Queen("WHITE", self.board)) 

        is_valid = queen.valid_positions(4, 4, 7, 4)
        self.assertFalse(is_valid) 

    def test_queen_capture_enemy(self):
        """
        Prueba que la reina pueda capturar una pieza enemiga.
        Funcionalidad:
        - Verifica que la reina pueda moverse a una casilla ocupada por una pieza enemiga y capturarla.
        """
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)  
        self.board.set_piece(6, 4, Queen("BLACK", self.board)) 

        is_valid = queen.valid_positions(4, 4, 6, 4)
        self.assertTrue(is_valid)  

    def test_queen_blocked_by_enemy(self):
        """
        Prueba que la reina no pueda moverse más allá de una pieza enemiga.
        Funcionalidad:
        - Verifica que la reina no pueda avanzar más allá de una pieza enemiga bloqueando su camino.
        """
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen) 
        self.board.set_piece(6, 4, Queen("BLACK", self.board)) 

        is_valid = queen.valid_positions(4, 4, 7, 4)
        self.assertFalse(is_valid)  

    def test_queen_invalid_diagonal_move(self):
        """
        Prueba que la reina no pueda moverse en diagonal si está bloqueada.
        Funcionalidad:
        - Verifica que la reina no pueda moverse en diagonal si hay una pieza bloqueando su trayectoria.
        """
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        self.board.set_piece(5, 5, Pawn("WHITE", self.board)) 
        is_valid = queen.valid_positions(4, 4, 6, 6)  
        self.assertFalse(is_valid)  

    def test_queen_move_out_of_bounds(self):
        """
        Prueba que la reina no pueda moverse fuera de los límites del tablero.
        Funcionalidad:
        - Verifica que la reina no pueda moverse fuera del tablero.
        """
        queen = Queen("WHITE", self.board)
        self.board.set_piece(0, 0, queen) 
        is_valid = queen.valid_positions(0, 0, -1, 0)  
        self.assertFalse(is_valid)  

    def test_queen_long_move_horizontal(self):
        """
        Prueba que la reina pueda realizar un movimiento largo horizontal.
        Funcionalidad:
        - Verifica que la reina pueda moverse horizontalmente sin estar bloqueada.
        """
        queen = Queen("WHITE", self.board)
        self.board.set_piece(0, 0, queen)
        is_valid = queen.valid_positions(0, 0, 0, 7) 
        self.assertTrue(is_valid) 

    def test_queen_cannot_jump_over_pieces(self):
        """
        Prueba que la reina no pueda saltar por encima de otras piezas.
        Funcionalidad:
        - Coloca una pieza en el camino de la reina y verifica que no pueda saltarla.
        """
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        self.board.set_piece(5, 4, Pawn("WHITE", self.board))
        is_valid = queen.valid_positions(4, 4, 7, 4)
        self.assertFalse(is_valid)  

    def test_queen_blocked_by_own_piece_in_diagonal(self):
        """
        Prueba que la reina no pueda moverse en diagonal si está bloqueada por una pieza propia.
        Funcionalidad:
        - Coloca una pieza propia en la trayectoria diagonal de la reina y verifica que no pueda avanzar.
        """
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        self.board.set_piece(5, 5, Pawn("WHITE", self.board)) 
        is_valid = queen.valid_positions(4, 4, 6, 6)
        self.assertFalse(is_valid) 



if __name__ == '__main__':
    unittest.main()