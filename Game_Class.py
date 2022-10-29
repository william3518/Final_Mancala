from Player_SuperClass import Player
from Human_SubClass import Human
from Gameboard_Class import Gameboard


class Game:
    def __init__(self, p1, p2, gb, cp):
        self.p1 = p1
        self.p2 = p2
        self.gb = gb
        self.current_player = cp

    # determines which pocket the current player wants to start from
    def start_point(self):
        print("")
        print("[1, 2, 3, 4, 5, 6]")
        pocket_num = 0
        while True : # ensures that the starting pocket is valid
            pocket_num = int(input("What pocket do you want to start from? (1-6): "))
            if 6 < pocket_num or pocket_num < 1 :
                # user must input a new number if their selected pocket is out of the range of 1-6
                continue
            elif self.gb.get_pocket(pocket_num - 1) == 0:
                # # user must input a new number if their selected pocket has no pieces in it
                continue
            else:
                break
        return pocket_num

    # flips the current_player between 1 and 2
    def end_turn(self):
        if self.current_player == 1:  # makes the current player 2 if it was previously 1
            self.current_player += 1
        else:
            self.current_player -= 1  # makes the current player 1 if it was previously 2
        return self.current_player

    # checks the mancalas to see which player has more pieces and prints the winner and score
    def determine_winner(self):
        if self.gb.get_current_mancala() == self.gb.get_opposing_mancala():
            # calls a tie if both the current player and opposing player have the same number of pieces
            print("Tie game: 24 - 24")
        elif self.current_player == 1: # checks if it is player 1's turn
            if self.gb.get_current_mancala() > self.gb.get_opposing_mancala():
                # player 1 wins if they are the current player and there are more pieces in the current_mancala
                # than the opponent_mancala
                print(self.p1.get_name(), "wins: ", str(self.gb.get_current_mancala()), "-",
                      str(self.gb.get_opposing_mancala()))
            else:
                # player 2 wins if they are not the current player and there are more pieces in the opponent_mancala
                # than the current_mancala
                print(self.p2.get_name(), "wins: ", str(self.gb.get_opposing_mancala()), "-",
                      str(self.gb.get_current_mancala()))
        else:
            if self.gb.get_current_mancala() > self.gb.get_opposing_mancala():
                # player 2 wins if they are the current player and there are more pieces in the current_mancala
                # than the opponent_mancala
                print(self.p2.get_name(), "wins: ", str(self.gb.get_current_mancala()), "-",
                      str(self.gb.get_opposing_mancala()))
            else:
                # player 1 wins if they are not the current player and there are more pieces in the opponent_mancala
                # than the current_mancala
                print(self.p1.get_name(), "wins: ", str(self.gb.get_opposing_mancala()), "-",
                      str(self.gb.get_current_mancala()))

    # transfers the remaining pieces in a player's row into their mancala
    def remaining_pieces(self):
        sum_top = 0
        sum_bot = 0
        for i in range(6):  # traverses the top row adding any pieces to the opponent's mancala
            sum_top += self.gb.get_board()[0][i+1]
            self.gb.get_board()[0][i + 1] = 0
        self.gb.get_board()[0][0] += sum_top
        for j in range(6):  # traverses the bottom row adding any pieces to the current player's mancala
            sum_bot += self.gb.get_board()[1][j]
            self.gb.get_board()[1][j] = 0
        self.gb.get_board()[1][6] += sum_bot

    # executes a player's turn
    def turn(self):
        if self.current_player == 1:  # prints whose turn it is based on current_player field
            print(self.p1.get_name(), "'s turn:")
        else:
            print(self.p2.get_name(), "'s turn:")
        while True:  # player gets additional turns while extra_turn() is true
            self.gb.show_board()
            start = self.start_point()
            self.gb.move_pieces(start)
            if self.gb.extra_turn() == False:
                break
        self.gb.capture()
        self.gb.steal()
        self.gb.show_board()
        if self.gb.end_game() == True:
            # if there are no pieces left in either row, the remaining pieces are moved to the mancala
            # and the winner and final score is calculated
            self.remaining_pieces()
            self.determine_winner()
        else:
            # if the game is not over, the current player is changed and the board is flipped for the other player
            self.gb.flip_board()
            self.end_turn()
            print("")











