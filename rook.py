from piece import Piece

class Rook(Piece):
    def __init__(self, color):
        symbol = "R" if color == "White" else "r"
        super().__init__(color, symbol)

    def possible_moves(self, board, row, col):
        directions=[
            (-1,0),(1,0),
            (0,-1),(0,1)
            ]
        return self.sliding_moves(board,row,col,directions)