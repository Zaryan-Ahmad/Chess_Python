from piece import Piece

class Pawn(Piece):
    def __init__(self, color):
        symbol = "P" if color == "White" else "p"
        super().__init__(color, symbol)

    def possible_moves(self, board, row, col):
        moves = []
        if self.color == "White":
            direction = -1
            starting_row = 6
        else:
            direction = 1
            starting_row = 1
        
        one_ahead = row + direction

        if board.is_inside(one_ahead, col) and board.get_piece(one_ahead, col) is None:
            moves.append((one_ahead, col))

            two_ahead = row + 2 * direction
            if row == starting_row and board.is_inside(two_ahead, col) and board.get_piece(two_ahead, col) is None:
                moves.append((two_ahead, col))

        for dc in [-1, 1]:
            r = row + direction
            c = col + dc
            if board.is_inside(r, c):
                target = board.get_piece(r, c)
                if target is not None and target.color != self.color:
                    moves.append((r, c))
        return moves

