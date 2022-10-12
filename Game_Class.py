from Player_SuperClass import Player
from Human_SubClass import Human

class Game:
    def __init__(self, p1, p2, gb):
        self.p1 = p1
        self.p2 = p2
        self.gb = gb

    def start_point(self):
        pocket_num = int(input("What pocket do you want to start from? "))
        return pocket_num
