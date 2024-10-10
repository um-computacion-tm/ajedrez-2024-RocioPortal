from chess.game import Chess
from chess.exceptions import InvalidMove, GameOverException
import sys

def main():
    chess = Chess()
    try:   
        while  chess.is_playing:       
            play(chess)
    except GameOverException as e:
        print(e)
        sys.exit()  # Finalizar el programa cuando el juego ha terminado

def play (chess):
    try:

        #print(chess.show_board()) 
        print("turn: ", chess.turn)
         # Capturar la entrada del usuario y verificar si quiere salir
        user_input = input("Ingrese su movimiento o EXIT para terminar: ").strip().lower()

        if user_input == "EXIT":
            raise GameOverException("El jugador ha terminado la partida.")
        
        from_row= int(input("Desde fila: "))
        from_col= int(input("Desde columna: "))
        to_row= int(input("A fila: "))
        to_col= int(input("A columna: "))

        chess.move(
            from_row,
            from_col,
            to_row,
            to_col
        )

        promotion_happened = chess.move(from_row, from_col, to_row, to_col)
        
        if promotion_happened:   #muestra el mensaje de que ha ocurrido el cambio
            print(f"¡El peón ha sido promovido a reina en la posición: ({to_row}, {to_col})!")

#las excepciones se ponen de la mas particular a la mas general
    
    except InvalidMove as e:
        print(e)
    except Exception as e:
        print("error", e)



# if __name__ == '__main__':
#      main()

    