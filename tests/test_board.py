import unittest
from chess.board import Board
from chess.rook import Rook
from chess.pawn import Pawn
from chess.exceptions import OutOfBoard


class TestBoard(unittest.TestCase):
    """
    Clase de prueba para verificar la funcionalidad del tablero de ajedrez (`Board`).
    """

    def test_str_board(self):
        """
        Prueba que la representación en cadena (str) del tablero sea correcta.
        Funcionalidad:
        - Verifica que el tablero se inicialice correctamente con las piezas en sus posiciones predeterminadas.
        - Compara la representación en cadena del tablero con un string esperado.
        """
        board = Board()
        expected_str = (
            "    0    1    2    3    4    5    6    7 \n"
            "0   ♖    ♘    ♗    ♕    ♔    ♗    ♘    ♖  \n\n"
            "1   ♙    ♙    ♙    ♙    ♙    ♙    ♙    ♙  \n\n"
            "2   .    .    .    .    .    .    .    .  \n\n"
            "3   .    .    .    .    .    .    .    .  \n\n"
            "4   .    .    .    .    .    .    .    .  \n\n"
            "5   .    .    .    .    .    .    .    .  \n\n"
            "6   ♟    ♟    ♟    ♟    ♟    ♟    ♟    ♟  \n\n"
            "7   ♜    ♞    ♝    ♛    ♚    ♝    ♞    ♜  \n\n"
        )
        self.assertEqual(str(board), expected_str)

    def setUp(self):
        """
        Configuración inicial para cada prueba.
        Funcionalidad:
        - Crea una nueva instancia de `Board` antes de cada test.
        """
        self.board = Board()

    def test_initial_positions(self):
        """
        Prueba que las piezas estén en las posiciones iniciales correctas.
        Funcionalidad:
        - Verifica que las torres y los peones estén en las posiciones iniciales tanto para las piezas blancas como negras.
        """
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertEqual(self.board.get_piece(0, 0).get_color, "BLACK")
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertEqual(self.board.get_piece(7, 0).get_color, "WHITE")
        self.assertIsInstance(self.board.get_piece(1, 0), Pawn)
        self.assertEqual(self.board.get_piece(1, 0).get_color, "BLACK")
        self.assertIsInstance(self.board.get_piece(6, 0), Pawn)
        self.assertEqual(self.board.get_piece(6, 0).get_color, "WHITE")

    def test_get_piece(self):
        """
        Prueba que `get_piece` devuelva la pieza correcta en una posición específica.
        Funcionalidad:
        - Verifica que `get_piece` devuelva la pieza correcta (torre o peón) en las posiciones esperadas.
        """
        rook = self.board.get_piece(0, 0)
        self.assertIsInstance(rook, Rook)
        self.assertEqual(rook.get_color, "BLACK")

        pawn = self.board.get_piece(6, 0)
        self.assertIsInstance(pawn, Pawn)
        self.assertEqual(pawn.get_color, "WHITE")

        pawn = self.board.get_piece(1, 0)
        self.assertIsInstance(pawn, Pawn)
        self.assertEqual(pawn.get_color, "BLACK")

    def test_set_piece(self):
        """
        Prueba que `set_piece` coloque correctamente una pieza en el tablero.
        Funcionalidad:
        - Verifica que una pieza (en este caso, un peón negro) pueda ser colocada en una posición específica del tablero.
        - Verifica que `get_piece` devuelva la pieza correcta después de colocarla.
        """
        new_pawn = Pawn("BLACK", self.board)
        self.board.set_piece(4, 4, new_pawn)
        piece = self.board.get_piece(4, 4)
        self.assertIsInstance(piece, Pawn)
        self.assertEqual(piece.get_color, "BLACK")

    def test_move(self):
        """
        Prueba que `move` funcione correctamente para mover una pieza en el tablero.
        Funcionalidad:
        - Coloca una torre negra en la posición (0, 0) y la mueve a la posición (2, 0).
        - Verifica que la pieza se haya movido correctamente y que la representación en cadena del tablero sea correcta después del movimiento.
        """
        board = Board(for_test=True)
        rook = Rook(color='BLACK', board=board)
        board.set_piece(0, 0, rook)

        board.move(
            from_row=0,
            from_col=0,
            to_row=2,
            to_col=0,
        )
        
        self.assertIsInstance(
            board.get_piece(2, 0),
            Rook,
        )
        self.assertEqual(
            str(board),
            (
                "    0    1    2    3    4    5    6    7 \n"  
                "0   .    .    .    .    .    .    .    .  \n\n"
                "1   .    .    .    .    .    .    .    .  \n\n"
                "2   ♖    .    .    .    .    .    .    .  \n\n"
                "3   .    .    .    .    .    .    .    .  \n\n"
                "4   .    .    .    .    .    .    .    .  \n\n"
                "5   .    .    .    .    .    .    .    .  \n\n"
                "6   .    .    .    .    .    .    .    .  \n\n"
                "7   .    .    .    .    .    .    .    .  \n\n"
            )
        )

    def test_get_piece_out_of_range(self):
        """
        Prueba que se lance una excepción `OutOfBoard` cuando se intenta acceder a una posición fuera del tablero.
        Funcionalidad:
        - Verifica que `get_piece` lance la excepción `OutOfBoard` al intentar acceder a coordenadas fuera del rango del tablero.
        """
        board = Board(for_test=True)

        with self.assertRaises(OutOfBoard) as exc:
            board.get_piece(10, 10)

        self.assertEqual(
            exc.exception.message,
            "La posicion indicada se encuentra fuera del tablero"
        )

if __name__ == '__main__':
    unittest.main()