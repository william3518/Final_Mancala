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
            self.gb.move_pieces(self.start_point())
            if self.gb.extra_turn() == False:
                break
        self.gb.capture()
        if self.gb.end_game() == True:
            if self.gb[1][6] > self.gb[0][0]:
                if current_player == 1:
                    print("Game over,", self.p1.get_name(), "wins")
                    print("Score:",self.gb[1][6], "-", self.gb[0][0])
                else:
                    print("Game over,", self.p2.get_name(), "wins")
                    print("Score:", self.gb[1][6], "-", self.gb[0][0])
            else:
                if current_player == 1:
                    print("Game over,", self.p2.get_name(), "wins")
                    print("Score:", self.gb[0][0], "-", self.gb[1][6])
                else:
                    print("Game over,", self.p1.get_name(), "wins")
                    print("Score:", self.gb[0][0], "-", self.gb[1][6])
            return False
        else:
            self.gb.flip_board()
            self.end_turn(current_player)
            return True








