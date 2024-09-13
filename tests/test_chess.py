import unittest
from chess.chess import Chess
from chess.pawn import Pawn
from chess.exceptions import InvalidMove, InvalidTurn, EmptyPosition

class TestChess(unittest.TestCase):

    def setUp(self):
        # Crear una instancia del juego de ajedrez para cada prueba
        self.game = Chess()

    def test_initial_turn(self):
        # Verificar que las blancas comienzan el juego
        self.assertEqual(self.game.turn, "WHITE")

    def test_invalid_move_empty_position(self):
        # Intentar mover desde una posición vacía (debería lanzar EmptyPosition)
        with self.assertRaises(EmptyPosition):
            self.game.move(4, 4, 5, 4)  # No hay ninguna pieza en (4, 4)


    def test_show_board(self):
        # Verificar que se puede mostrar el estado del tablero
        board_str = self.game.show_board()
        expected_str = (
            "♖♘♗♕♔♗♘♖\n"
            "♙♙♙♙♙♙♙♙\n"
            "        \n"
            "        \n"
            "        \n"
            "        \n"
            "♟♟♟♟♟♟♟♟\n"
            "♜♞♝♛♚♝♞♜\n"
        )
        self.assertEqual(board_str, expected_str)


if __name__ == '__main__':
    unittest.main()