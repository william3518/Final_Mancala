from Player_SuperClass import Player
from Human_SubClass import Human
from Gameboard_Class import Gameboard


class Game:
    def __init__(self, p1, p2, gb):
        self.p1 = p1
        self.p2 = p2
        self.gb = gb

    def start_point(self):
        print("")
        print("[1, 2, 3, 4, 5, 6]")
        pocket_num = int(input("What pocket do you want to start from? (1-6): "))
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








