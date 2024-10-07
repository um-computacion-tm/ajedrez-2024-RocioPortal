import unittest
from chess.chess import Chess
from chess.pawn import Pawn
from chess.exceptions import InvalidMove, InvalidTurn, EmptyPosition, GameOverException
from chess.board import Board
from unittest.mock import patch

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

    def test_change_turn(self):
        # Verificar que el turno cambie después de un movimiento
        self.game.move(6, 4, 5, 4)  # Mover el peón blanco
        self.assertEqual(self.game.turn, "BLACK")  # Ahora debe ser el turno de las negras

        self.game.move(1, 4, 2, 4)  # Mover el peón negro
        self.assertEqual(self.game.turn, "WHITE")  # Ahora debe ser el turno de las blancas

    def test_invalid_turn(self):
        # Intentar mover una pieza negra en el turno de las blancas
        with self.assertRaises(InvalidTurn):
            self.game.move(1, 4, 2, 4)  # Mover un peón negro cuando es turno de las blancas

    def test_invalid_move(self):
        # Intentar mover un peón blanco dos casillas adelante cuando ya no es el primer movimiento
        self.game.move(6, 4, 5, 4)  # Primer movimiento válido
        with self.assertRaises(InvalidMove):
            self.game.move(5, 4, 3, 4)  # Este movimiento debería ser inválido

    def test_get_board(self):
        # Verificar que el tablero se obtiene correctamente a través de get_board()
        board = self.game.get_board()
        self.assertIsInstance(board, Board)  # Asegura que es una instancia de la clase Board

        #verificar que el tablero contiene piezas en posiciones iniciales
        self.assertIsNotNone(board.get_piece(0, 0))  # Debería haber una torre negra en la posición (0, 0)
        self.assertIsNotNone(board.get_piece(7, 0))  # Debería haber una torre blanca en la posición (7, 0)

    @patch('builtins.input', return_value='si')  # Simular que el usuario acepta el empate
    def test_offer_draw_accept(self, mock_input):
        chess = Chess()
        with self.assertRaises(GameOverException) as context:
            chess.offer_draw()
        self.assertEqual(str(context.exception), "El jugador ha aceptado el empate. El juego ha terminado.")

    @patch('builtins.input', return_value='no')  # Simular que el usuario rechaza el empate
    def test_offer_draw_decline(self, mock_input):
        chess = Chess()
        result = chess.offer_draw()
        self.assertTrue(result)  # Verificar que el juego continúa si se rechaza el empate

if __name__ == '__main__':
    unittest.main()