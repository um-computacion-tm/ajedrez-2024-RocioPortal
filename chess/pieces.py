class Piece:
    def __init__(self, color):     #concepto de herencia 
        self.__color__ = color
        #self.__board__ = board

#    def __str__(self):
#        if self.__color__=="WHITE":
#            return self.white_str
#        else:
#            return self.black_str

    @property
    def get_color (self):
        return self.__color__