class Piece:
    def __init__(self, color):     #concepto de herencia 
        self.__color__ = color

    @property
    def get_color (self):
        return self.__color__