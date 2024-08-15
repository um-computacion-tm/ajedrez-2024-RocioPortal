from chess import Chess

def main():
    chess = Chess()   
    while True:       
        play(chess)

def play (chess):
    try:
        print(chess.show_board()) 
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

    except Exception as e:
        print("error")



if __name__ == '__main__':
    main()

    