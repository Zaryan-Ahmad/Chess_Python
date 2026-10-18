from piece import Piece
from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King

class Board:
    def __init__(self):
        self.grid=[[None for _ in range(8)]for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self):
        # Setting up pawns
        for col in range(8):
            self.grid[1][col]=Pawn("Black")
            self.grid[6][col]=Pawn("White")

        #setting up back rank pieces
        back_rank=[Rook,Knight,Bishop,Queen,King,Bishop,Knight,Rook]
        for col in range(8):
            self.grid[0][col]=back_rank[col]("Black")
            self.grid[7][col]=back_rank[col]("White")

    def move_piece(self,from_row,from_col,to_row,to_col):
        piece=self.grid[from_row][from_col]
        self.grid[to_row][to_col]=piece
        self.grid[from_row][from_col]=None

        if isinstance(piece, Pawn):
            if to_row == 0 or to_row == 7:
                self.grid[to_row][to_col] = Queen(piece.color)
                print("Promotion successful")

    def display(self):
        print()
        print("    a b c d e f g h")
        print("   -----------------")
        for row in range(8):
            line = str(8 - row) + " | "
            for col in range(8):
                piece = self.grid[row][col]
                if piece is None:
                    line += ". "
                else:
                    line += piece.symbol + " "
            line += "| " + str(8 - row)
            print(line)
        print("   -----------------")
        print("    a b c d e f g h")
        print()

    def is_inside(self,row,col):
        return 0 <= row < 8 and 0<= col <8

    def get_piece(self,row,col):
        return self.grid[row][col]

    def find_king(self,color):
        for row in range(8):
            for col in range(8):
                piece=self.grid[row][col]
                if isinstance(piece, King) and piece.color==color:
                    return (row,col)
        return None

    def is_in_check(self,color):
        king_position=self.find_king(color)
        if king_position is None:
            return False
        for row in range(8):
            for col in range(8):
                piece=self.grid[row][col]
                if piece is not None and piece.color!=color:
                    if king_position in piece.possible_moves(self,row,col):
                        return True
        return False

    def get_legal_moves(self, row, col):
        piece = self.grid[row][col]
        if piece is None:
            return []
        legal_moves=[]
        for (to_row,to_col) in piece.possible_moves(self,row,col):
            captured = self.grid[to_row][to_col]
            self.grid[to_row][to_col]= piece
            self.grid[row][col]= None

            if not self.is_in_check(piece.color):
                legal_moves.append((to_row,to_col))

            self.grid[row][col]= piece
            self.grid[to_row][to_col]= captured
        return legal_moves

    def has_legal_moves(self,color):
        for row in range(8):
            for col in range(8):
                piece=self.grid[row][col]
                if piece is not None and piece.color == color:
                    if len(self.get_legal_moves(row,col))>0:
                        return True

        return False



