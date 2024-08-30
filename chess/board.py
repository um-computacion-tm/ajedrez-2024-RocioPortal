from chess.rook import Rook
from chess.knight import Knight
from chess.bishop import Bishop
from chess.queen import Queen
from chess.king import King
from chess.pawn import Pawn

class Board:    
    def __init__(self):
        self.__positions__ = []    
        for _ in range (8):
            col= []
            for _ in range (8):
                col.append(None)
            self.__positions__.append(col)

    #torres
        self.__positions__ [0] [0] = Rook("BLACK")    
        self.__positions__ [0] [7] = Rook("BLACK") 
        self.__positions__ [7] [7] = Rook("WHITE") 
        self.__positions__ [7] [0] = Rook("WHITE") 

    #Caballos
        self.__positions__[0][1] = Knight("BLACK")
        self.__positions__[0][6] = Knight("BLACK")
        self.__positions__[7][1] = Knight("WHITE")  
        self.__positions__[7][6] = Knight("WHITE")

    #Alfiles
        self.__positions__[0][2] = Bishop("BLACK")  
        self.__positions__[0][5] = Bishop("BLACK")
        self.__positions__[7][2] = Bishop("WHITE")
        self.__positions__[7][5] = Bishop("WHITE")

    #Reinas
        self.__positions__[0][3] = Queen("BLACK")
        self.__positions__[7][3] = Queen("WHITE")

    #Reyes
        self.__positions__[0][4] = King("BLACK")
        self.__positions__[7][4] = King("WHITE")

    #Peones
        for i in range(8):
            self.__positions__[1][i] = Pawn("BLACK")
            self.__positions__[6][i] = Pawn("WHITE")


    def __str__(self):      #define cómo se convierte el objeto Board a una cadena de texto cuando se intenta imprimirlo o convertirlo a una cadena usando str().
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str


    def get_piece (self, row, col):
        return self.__positions__[row] [col]

    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece