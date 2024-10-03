from chess.chess import Chess
from chess.exceptions import InvalidMove, InvalidTurn, EmptyPosition

def main():
    chess = Chess()   
    while  chess.is_playing:       
        play(chess)

def play (chess):
    try:

        #print(chess.show_board()) 
        print("turn: ", chess.turn)
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
    except InvalidTurn as e:
        print(e)
    except Exception as e:
        print("error", e)



# if __name__ == '__main__':
#      main()

    