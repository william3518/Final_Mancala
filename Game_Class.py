from Player_SuperClass import Player
from Human_SubClass import Human
from Gameboard_Class import Gameboard


class Game:
    def __init__(self, p1, p2, gb, cp):
        self.p1 = p1
        self.p2 = p2
        self.gb = gb
        self.current_player = cp

    def start_point(self):
        print("")
        print("[1, 2, 3, 4, 5, 6]")
        pocket_num = 0
        while True :
            pocket_num = int(input("What pocket do you want to start from? (1-6): "))
            if 6 < pocket_num  or  pocket_num < 1 :
                continue
            elif self.gb.get_board(pocket_num - 1) == 0:
                continue
            else:
                break
        return pocket_num

    def end_turn(self):
        if self.current_player == 1:
            self.current_player += 1
        else:
            self.current_player -= 1
        return self.current_player

    def determine_winner(self):
        if self.gb.get_current_mancala() == self.gb.get_opposing_mancala():
            print("Tie game: 24 - 24")
        elif self.current_player == 1:
            if self.gb.get_current_mancala() > self.gb.get_opposing_mancala():
                print(self.p1.get_name(), "wins: ", str(self.gb.get_current_mancala()), "-",
                      str(self.gb.get_opposing_mancala()))
            else:
                print(self.p2.get_name(), "wins: ", str(self.gb.get_opposing_mancala()), "-",
                      str(self.gb.get_current_mancala()))
        else:
            if self.gb.get_current_mancala() > self.gb.get_opposing_mancala():
                print(self.p2.get_name(), "wins: ", str(self.gb.get_current_mancala()), "-",
                      str(self.gb.get_opposing_mancala()))
            else:
                print(self.p1.get_name(), "wins: ", str(self.gb.get_opposing_mancala()), "-",
                      str(self.gb.get_current_mancala()))

    def remaining_pieces(self):
        sum_top = 0
        sum_bot = 0
        for i in range(6):
            sum_top += self.gb.get_board()[0][i+1]
        self.gb.get_board()[0][0] += sum_top
        for j in range(6):
            sum_bot += self.gb.get_board()[1][j]
        self.gb.get_board()[1][6] += sum_bot

    def turn(self):
        if self.current_player == 1:
            print(self.p1.get_name(), "'s turn:")
        else:
            print(self.p2.get_name(), "'s turn:")
        while True:
            self.gb.show_board()
            start = self.start_point()
            self.gb.move_pieces(start)
            if self.gb.extra_turn() == False:
                break
        self.gb.capture()
        self.gb.show_board()
        if self.gb.end_game() == True:
            self.remaining_pieces()
            self.determine_winner()
        else:
            self.gb.flip_board()
            self.end_turn()
            print("")











