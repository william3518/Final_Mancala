from Player_SuperClass import Player


class Human:
    def __init__(self, num, name):
        self.player_name = num
        self.player_name = name

    # accessor method that accesses the human's name
    def get_name(self):
        return self.player_name
