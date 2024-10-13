from chess.game import Chess
from chess.exceptions import InvalidMove, GameOverException, InvalidCoordinateInputError
import sys

def main():
    '''
    La función principal del juego de ajedrez.
    Funcionalidad:
    Inicializa el juego de ajedrez y entra en un bucle que permite a los jugadores hacer sus movimientos.
    Captura la excepción `GameOverException` cuando el juego ha terminado y finaliza el programa.
    '''
    chess = Chess()
    try:
        while True:  # Bucle principal del juego
            play(chess)
    except GameOverException as e:
        print(e)
        sys.exit()  # Finalizar el programa cuando el juego ha terminado

def play (chess):
    '''
    La función controla el flujo de una jugada en el juego de ajedrez.
    Funcionalidad:
    Muestra el tablero, solicita al jugador que ingrese sus movimientos, y verifica si el jugador quiere terminar la partida.
    Verifica si el movimiento es válido y si el jugador ha ganado.
    Parámetros:
    chess: Recibe una instancia del juego de ajedrez para gestionar el estado actual del tablero y las jugadas.
    '''
    try:
        print(chess.show_board()) 
        print("turn: ", chess.turn)
         # Capturar la entrada del usuario y verificar si quiere salir
        print("Ingrese su movimiento o EXIT para terminar: ")
        
        # Capturar la entrada del usuario y verificar si quiere salir
        from_row = input("Desde fila: ").strip().upper()
        if from_row == "EXIT":
            print("El jugador ha terminado la partida.")
            exit()
        from_col = input("Desde columna: ").strip().upper()
        if from_col == "EXIT":                      
            print("El jugador ha terminado la partida.")
            exit()
        to_row = input("A fila: ").strip().upper()
        if to_row == "EXIT":
            print("El jugador ha terminado la partida.")
            exit()
        to_col = input("A columna: ").strip().upper()
        if to_col == "EXIT":
            print("El jugador ha terminado la partida.")
            exit()
        try:
            from_row = int(from_row)
            from_col = int(from_col)
            to_row = int(to_row)
            to_col = int(to_col)
        except ValueError:
            raise InvalidCoordinateInputError()  # Lanzar la excepción si no es un número

        chess.move(
            from_row,
            from_col,
            to_row,
            to_col
        )

        # Verificar si hay un ganador
        winner = chess.check_winner()
        if winner:
            print(print(f"El juego ha terminado. {winner} es el ganador."))  # Imprimir el mensaje de quién ganó
            sys.exit()  # Salir del programa
        return

#las excepciones se ponen de la mas particular a la mas general
    except InvalidCoordinateInputError as e:
        print(e)
    except InvalidMove as e:
        print(e)
    except Exception as e:
        print("error", e)


if __name__ == '__main__':
    main()