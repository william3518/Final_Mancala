class Gameboard:
    def __init__(self, last_piece):
        self.last_piece = last_piece
        self.board = [[0, 4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4, 0]]

    # accessor method that accesses the last_piece instance variable
    def get_last_piece(self):
        return self.last_piece

    # accessor method that accesses the current player's mancala
    def get_current_mancala(self):
        return self.board[1][6]

    # accessor method that accesses the opponent's mancala
    def get_opposing_mancala(self):
        return self.board[0][0]

    # accessor method that accesses the pocket that the current player intends to start their turn at
    def get_pocket(self, pocket):
        return int(self.board[1][pocket])

    # accessor method that accesses the entire mancala board
    def get_board(self):
        return self.board

    # prints the mancala board
    def show_board(self):  # traverses the 2D array
        for i in range(len(self.board)):  # prints each row on a new line
            print(self.board[i])

    # takes the piece's from the current player's chosen starting pocket and drops one in each pocket starting one
    # pocket to the righting and following in a counterclockwise rotation
    # start parameter: the pocket that the pieces are picked up from
    def move_pieces(self, start):
        row = 1
        start -= 1
        piece_num = self.board[row][start]
        self.board[row][start] = 0
        start += 1
        while piece_num > 1:  # while loop runs until all pieces from the starting pocket are redistributed
            if row == 1 and start <= 5:
                # next piece is dropped to the right of the previous pocket if the previous pocket is one of
                # the 6 leftmost bottom pockets
                self.board[row][start] += 1
                start += 1
            elif row == 1 and start == 6:
                # next piece is dropped above the previous pocket if the previous pocket is the last in the bottom row
                self.board[row][start] += 1
                row -= 1
            elif row == 0 and start >= 1:
                # next piece is dropped to the left of the previous pocket if the previous pocket is one of
                # the 6 rightmost upper pockets
                self.board[row][start] += 1
                start -= 1
            else:
                # next piece is dropped below the previous pocket if the previous pocket is the first in the upper row
                self.board[row][start] += 1
                row += 1
            piece_num -= 1
        if piece_num == 1:
            self.board[row][start] += 1
        self.last_piece = [row, start]
        return self.last_piece

    # evaluates whether the current player receives an extra turn
    def extra_turn(self):
        if self.last_piece == [1, 6]:
            # if last piece is dropped in the player's mancala return true
            return True
        else:
            return False

    # evaluates whether the current player can capture any of the opponent's pieces
    def capture(self):
        if self.last_piece[0] == 1:  # evaluated whether the last piece was dropped on the current player's side
            if self.board[self.last_piece[0]][self.last_piece[1]] == 1:
                # evaluates whether the last piece dropped is the only in its pocket
                if self.board[0][self.last_piece[1] + 1] > 0:
                    # evaluates if the corresponding opponent pocket has any pieces
                    # if the three conditions are true, the last piece dropped and all pieces in the opponent's
                    # corresponding pocket are moved to the current player's mancala
                    capture_sum = self.board[self.last_piece[0]][self.last_piece[1]] + \
                                  self.board[0][self.last_piece[1] + 1]
                    self.board[1][6] += capture_sum
                    self.board[self.last_piece[0]][self.last_piece[1]] = 0
                    self.board[0][self.last_piece[1] + 1] = 0

    # evaluates whether the current player can steal from the opponent's mancala
    def steal(self):
        if self.last_piece == [0, 0]:  # evaluates if the last piece was dropped in the opponent's mancala
            if self.board[0][0] >= 2:
                # takes the last piece and one more if the opponent had pieces in their mancala before the drop
                self.board[0][0] -= 2
                self.board[1][6] += 2
            else:
                self.board[0][0] -= 1
                self.board[1][6] += 1

    # evaluates whether the game is finished
    def end_game(self):
        sum_top = 0
        sum_bot = 0
        for i in range(6):  # traverses the top row counting the pieces in the pockets
            sum_top = sum_top + self.board[0][i + 1]
        if sum_top == 0:  # game is over if there are no pieces in the top row
            return True
        elif sum_top != 0:  # checks the bottom row if there are pieces in the top row
            for j in range(6):  # traverses the top bottom counting the pieces in the pockets
                sum_bot += self.board[1][j]
            if sum_bot == 0:  # game is over if there are no pieces in the bottom row
                return True
        else:
            return False

    # flips the board so that whoever turn it is has their row on the bottom
    def flip_board(self):
        self.board.reverse()
        for i in range(len(self.board)):  # flips the contents each row after flipping the top and bottom row
            self.board[i].reverse()
