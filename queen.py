from piece import Piece

class Queen(Piece):
    def __init__(self, color):
        symbol = "Q" if color == "White" else "q"
        super().__init__(color, symbol)

    def possible_moves(self,board,row,col):
        directions=[
            (-1,-1),(-1,0),(-1,1),(0,-1),
            (0,1),(1,0),(1,-1),(1,1)
            ]
        return self.sliding_moves(board,row,col,directions)
