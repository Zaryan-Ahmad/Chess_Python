from piece import Piece

class King(Piece):
    def __init__(self, color):
        symbol = "K" if color == "White" else "k"
        super().__init__(color, symbol)

    def possible_moves(self,board,row,col):
        steps=[
            (-1,-1),(-1,0),(-1,1),(0,-1),
            (0,1),(1,0),(1,-1),(1,1)
            ]
        return self.step_moves(board,row,col,steps)