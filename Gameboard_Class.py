class Gameboard:
    def __init__(self, last_piece):
        self.last_piece = last_piece
        self.board = [[0, 4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4, 0]]

    def get_last_piece(self):
        return self.last_piece

    def get_current_mancala(self):
        return self.board[1][6]

    def get_opposing_mancala(self):
        return self.board[0][0]

    def get_board(self):
        return self.board

    def show_board(self):
        for i in range(len(self.board)):
            print(self.board[i])

    def get_pocket(self, pocket):
        return int(self.board[1][pocket])

    def move_pieces(self, start):
        row = 1
        start -= 1
        piece_num = self.board[row][start]
        self.board[row][start] = 0
        start += 1
        while piece_num > 1:
            if row == 1 and start <= 5:
                self.board[row][start] += 1
                start += 1
            elif row == 1 and start == 6:
                self.board[row][start] += 1
                row -= 1
            elif row == 0 and start >= 1:
                self.board[row][start] += 1
                start -= 1
            else:
                self.board[row][start] += 1
                row += 1
            piece_num -= 1
        if piece_num == 1:
            self.board[row][start] += 1
        self.last_piece = [row, start]
        return self.last_piece

    def extra_turn(self):
        if self.last_piece == [1, 6]:
            return True
        else:
            return False

    def capture(self):
        if self.last_piece[0] == 1:
            if self.board[self.last_piece[0]][self.last_piece[1]] == 1:
                if self.board[0][self.last_piece[1] + 1] > 0:
                    capture_sum = self.board[self.last_piece[0]][self.last_piece[1]] + \
                                  self.board[0][self.last_piece[1] + 1]
                    self.board[1][6] += capture_sum
                    self.board[self.last_piece[0]][self.last_piece[1]] = 0
                    self.board[0][self.last_piece[1] + 1] = 0

    def steal(self):
        if self.last_piece == [0, 0]:
            if self.board[0][0] >= 2:
                self.board[0][0] -= 2
                self.board[1][6] += 2
            else:
                self.board[0][0] -= 1
                self.board[1][6] += 1

    def end_game(self):
        sum_top = 0
        sum_bot = 0
        for i in range(6):
            sum_top = sum_top + self.board[0][i+1]
        if sum_top == 0:
            return True
        else:
            for j in range(6):
                sum_bot += self.board[1][j]
            if sum_bot == 0:
                return True
            else:
                return False

    def flip_board(self):
        self.board.reverse()
        for i in range(len(self.board)):
            self.board[i].reverse()
