from board import Board
from player import Player

class Game:
    def __init__(self):
        self.board=Board()
        self.player_1=Player("White","Player 1")
        self.player_2=Player("Black","Player 2")
        self.current_player=self.player_1

    def switch_turns(self):
        if self.current_player==self.player_1:
            self.current_player=self.player_2
        else:
            self.current_player=self.player_1

    def convert_input(self,text):
        if len(text) != 2:
            return None

        letter=text[0].lower()
        number=text[1]
        if letter not in "abcdefgh" or number not in "12345678":
            return None
        col = ord(letter)-ord("a")
        row=8-int(number)

        return (row,col)

    def play(self):
        while True:
            self.board.display()
            color = self.current_player.color
            if not self.board.has_legal_moves(color):
                if self.board.is_in_check(color):
                    self.switch_turns()
                    print(f"Checkmate! {self.current_player.name} wins!")
                else:
                    print("Stalemate! Game is a draw.")
                break
            if self.board.is_in_check(color):
                print(f"Check! {self.current_player.name} is in check.")

            text = input(f"{self.current_player.name}'s turn ({color}): ")
            if text.strip().lower() == "quit":
                print("Game quit")
                break
            if self.make_move(text, color):
                self.switch_turns()

    def make_move(self,text,color):
        parts=text.split()
        if len(parts) != 2:
            print("please type : e2 e4")
            return False
        start=self.convert_input(parts[0])
        end=self.convert_input(parts[1])
        if start is None or end is None:
            print ("Invalid move, use letters a-h and numbers 1-8")
            return False

        piece=self.board.get_piece(start[0],start[1])
        if piece is None:
            print("There is no piece on the square")
            return False
        if piece.color != color:
            print("That is not your piece")
            return False

        if end not in self.board.get_legal_moves(start[0],start[1]):
            print ("That move is not valid")
            return False

        self.board.move_piece(start[0],start[1],end[0],end[1])
        return True



