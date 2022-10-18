class Gameboard:
    def __init__(self):
        self.board = [[0, 4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4, 0]]

    def show_board(self):
        for i in range(len(self.board)):
            print(self.board[i])

    def move_pieces(self, start):
        row = 1
        start -= 1
        piece_num = self.board[row][start]
        self.board[row][start] = 0
        start += 1
        while piece_num > 0:
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
        last_piece = [row, start]
        return last_piece

    def extra_turn(self, last_piece):
        if last_piece == [1, 6]:
            return True
        else:
            return False

    def capture(self, last_piece):
        if last_piece[0] == 1:
            if self.board[last_piece[0]][last_piece[1]] == 1:
                if self.board[0][last_piece[1]] > 0:
                    capture_sum = self.board[last_piece[0]][last_piece[1]] + self.board[0][last_piece[1]]
                    self.board[1][6] += capture_sum
                    self.board[last_piece[0]][last_piece[1]] = 0
                    self.board[0][last_piece[1]] = 0

    def end_game(self):
        sum_top = 0
        sum_bot = 0
        for i in range(5):
            sum_top = sum_top + self.board[0][i+1]
        if sum_top == 0:
            return True
        elif sum_top != 0:
            for j in range(6):
                sum_bot += self.board[1][j]
            if sum_bot == 0:
                return True
        else:
            return False

    def flip_board(self):
        temp = self.board[1]
        self.board[1] = self.board[0]
        self.board[0] = temp
        self.board[0] = self.board[0].reverse()
        self.board[1] = self.board[1].reverse()

