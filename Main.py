from Game_Class import Game
from Human_SubClass import Human
from Gameboard_Class import Gameboard


p1 = Human(1, "Will")
p2 = Human(2, "Robert")
gb1 = Gameboard([1, 6])
g1 = Game(p1, p2, gb1)
starting_turn = 1

while g1.turn(starting_turn):
   if g1.gb.end_game() == True:
       break



