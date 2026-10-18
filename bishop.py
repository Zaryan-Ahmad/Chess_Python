from piece import Piece

class Bishop(Piece):
    def __init__(self, color):
        symbol = "B" if color == "White" else "b"
        super().__init__(color, symbol)

    def possible_moves(self, board, row, col):
        directions=[
            (-1,-1),(-1,1),
            (1,-1),(1,1)
            ]
        return self.sliding_moves(board,row,col,directions)