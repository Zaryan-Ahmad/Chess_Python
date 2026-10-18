class Piece:
    def __init__(self,color,symbol):
        self.color=color
        self.symbol=symbol
    
    def possible_moves(self,board,row,col):
        return []

    def sliding_moves(self, board, row, col, directions):
        moves = []
        for dr, dc in directions:
            r = row + dr
            c = col + dc
            while board.is_inside(r, c):
                target = board.get_piece(r, c)
                if target is None:
                    moves.append((r, c))
                else:
                    if target.color != self.color:
                        moves.append((r, c))
                    break
                r += dr
                c += dc
        return moves

    def step_moves(self, board, row, col, steps):
        moves = []
        for dr, dc in steps:
            r = row + dr
            c = col + dc
            if board.is_inside(r, c):
                target = board.get_piece(r, c)
                if target is None or target.color != self.color:
                    moves.append((r, c))
        return moves
