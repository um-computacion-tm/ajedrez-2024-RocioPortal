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
        
        # Validar que las coordenadas están dentro del rango permitido
            
        if not (0 <= from_row < 8) or not (0 <= from_col < 8):
                raise ValueError("Las coordenadas de inicio están fuera del rango permitido.")
        if not (0 <= to_row < 8) or not (0 <= to_col < 8):
                raise ValueError("Las coordenadas de destino están fuera del rango permitido.")
            
            
    except Exception as e:
        print("error")



if __name__ == '__main__':
    main()

    