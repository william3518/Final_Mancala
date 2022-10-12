from Player_SuperClass import Player


class Human:
    def __init__(self, name):
        self.player_name = name

    def get_name(self):
        return self.player_name


h1 = Human("Will")
player1 = Player(1)

print("Player " + str(player1.get_num()) + " is " + h1.get_name())