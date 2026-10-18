from piece import Piece

class Knight(Piece):
    def __init__(self, color):
        symbol = "N" if color == "White" else "n"
        super().__init__(color, symbol)

    def possible_moves(self,board,row,col):
       steps=[
           (-2,-1),(-2,1),
           (-1,-2),(-1,2),
           (1,-2),(1,2),
           (2,-1),(2,1)
           ]
       return self.step_moves(board,row,col,steps)