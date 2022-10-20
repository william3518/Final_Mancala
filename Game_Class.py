from Player_SuperClass import Player
from Human_SubClass import Human
from Gameboard_Class import Gameboard


class Game:
    def __init__(self, p1, p2, gb, current_player):
        self.p1 = p1
        self.p2 = p2
        self.gb = gb
        self.current_player = current_player

    def start_point(self):
        print("")
        print("[1, 2, 3, 4, 5, 6]")
        pocket_num = 7
        while 6 < pocket_num or pocket_num < 1:
            pocket_num = int(input("What pocket do you want to start from? (1-6): "))
            if 6 >= pocket_num > 0:
                break
            else:
                continue
        return pocket_num

    def end_turn(self, current_player):
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1
        return current_player

    def turn(self, current_player):
        if current_player == 1:
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
        self.gb.flip_board()
        self.end_turn(current_player)









