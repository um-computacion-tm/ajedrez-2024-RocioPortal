import unittest
from unittest.mock import patch, MagicMock
from chess.game import Chess
from chess.cli import play, main, GameOverException
import sys


class TestCli(unittest.TestCase):
    
    @patch('chess.cli.play')  # Simular la función play en cli.py
    @patch('chess.cli.Chess')  # Simular la clase Chess en cli.py
    @patch('sys.exit')  # Capturar la llamada a sys.exit para no terminar el test
    def test_game_over_exception(self, mock_exit, mock_chess, mock_play):
        # Simular una instancia de Chess y su atributo is_playing
        mock_chess_instance = MagicMock()
        mock_chess_instance.is_playing = True  # El juego está activo inicialmente
        mock_chess.return_value = mock_chess_instance
        
        # Configurar la función play para lanzar la excepción GameOverException
        mock_play.side_effect = GameOverException("Fin del juego")

        # Ejecutar el método main
        main()

        # Verificar que se haya lanzado y capturado GameOverException
        mock_exit.assert_called_once()  # sys.exit debe haber sido llamado una vez
        mock_play.assert_called()  # Verificar que play fue llamado

    @patch('chess.cli.play')  # Simular la función play en cli.py
    @patch('chess.cli.Chess')  # Simular la clase Chess en cli.py
    @patch('sys.exit')  # Capturar la llamada a sys.exit
    def test_game_runs_normally(self, mock_exit, mock_chess, mock_play):
        # Simular una instancia de Chess y su atributo is_playing
        mock_chess_instance = MagicMock()
        mock_chess_instance.is_playing = False  # El juego termina inmediatamente
        mock_chess.return_value = mock_chess_instance
        
        # Ejecutar el método main
        main()

        # Verificar que no se haya llamado sys.exit (porque el juego terminó sin excepciones)
        mock_exit.assert_not_called()
        mock_play.assert_not_called()  # El método play no debería llamarse si el juego no está activo

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
        self.assertEqual(mock_input.call_count, 5)
        self.assertEqual(mock_print.call_count, 2)
        self.assertEqual(mock_chess_move.call_count, 0)

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
        self.assertEqual(mock_input.call_count, 5)
        self.assertEqual(mock_print.call_count, 2)
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
    ): #
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 2)
        self.assertEqual(mock_chess_move.call_count, 0)


if __name__ == '__main__':
    unittest.main()