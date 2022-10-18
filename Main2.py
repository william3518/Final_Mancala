from Gameboard_Class import Gameboard
lp1 = [0,0]
gb1 = Gameboard(lp1)
gb1.show_board()
print("")
gb1.move_pieces(3)
gb1.show_board()
print(gb1.get_last_piece())
print(gb1.extra_turn())