from Player_SuperClass import Player
from Human_SubClass import Human

class Game:
    def __init__(self, p1, p2, gb):
        self.p1 = p1
        self.p2 = p2
        self.gb = gb

    def start_point(self):
        pocket_num = int(input("What pocket do you want to start from? (1-5) "))
        return pocket_num

    def end_turn(self, current_player):
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1
        return current_player

    def turn(self, current_player):
        if current_player == 1:
            print(self.p1.get_name, "'s turn:")
            do {
                self.gb.display_board()
                start = self.start_point()
                end = self.gb.move_pieces(start)
            }
            while self.gb.extra_turn(end) == True



