import unittest
from unittest.mock import patch, MagicMock
from chess.game import Chess
from chess.cli import play, main
from chess.exceptions import InvalidMove, InvalidCoordinateInputError, GameOverException
import sys


class TestCli(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['hola', '0', '1', '0', 'EXIT'])
    @patch('builtins.print')  # Simular print
    @patch.object(Chess, 'move')
    def test_invalid_coordinate_input(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        play(chess)
        # Verifica que el programa pidió 5 entradas
        self.assertEqual(mock_input.call_count, 4)
        # Verifica que el print se llamó 4 veces
        self.assertEqual(mock_print.call_count, 4)
        # Verifica que el movimiento no se ejecutó por entrada inválida
        self.assertEqual(mock_chess_move.call_count, 0)


    @patch('builtins.input', side_effect=['EXIT'])
    @patch('builtins.print')  # Simular print
    def test_exit_game(self, mock_print, mock_input):
        with self.assertRaises(SystemExit):  # Esperamos que el juego termine con "EXIT"
            main()
        # Verifica que se imprimió el mensaje de salida
        mock_print.assert_any_call("El jugador ha terminado la partida.")


    @patch('builtins.input', side_effect=['EXIT'])
    @patch('builtins.print')  # Simular print
    @patch.object(Chess, 'move')
    def test_game_over_exception(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        with self.assertRaises(SystemExit):  # Esperamos que el juego termine con "EXIT"
            play(chess)
        mock_print.assert_any_call("El jugador ha terminado la partida.")


    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        side_effect=['1', '1', '2', '2'], # estos son los valores que simula lo que ingresaria el usuario
    )
    @patch('builtins.print') # este patch controla lo que hace el print
    @patch.object(Chess, 'move')
    def test_happy_path(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ): #
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(mock_chess_move.call_count, 1)

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        side_effect=['hola', '1', '2', '2'], # estos son los valores que simula lo que ingresaria el usuario
    )
    @patch('builtins.print') # este patch controla lo que hace el print
    @patch.object(Chess, 'move')
    def test_not_happy_path(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ): #
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 4)
        self.assertEqual(mock_chess_move.call_count, 0)

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        side_effect=['1', '1', '2', 'hola'], # estos son los valores que simula lo que ingresaria el usuario
    )
    @patch('builtins.print') # este patch controla lo que hace el print
    @patch.object(Chess, 'move')
    def test_more_not_happy_path(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ): 
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 4)
        self.assertEqual(mock_chess_move.call_count, 0)


if __name__ == '__main__':
    unittest.main()