class Gameboard:
    def __init__(self):
        self.board = [[0, 4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4, 0]]

    def show_board(self):
        for i in range(len(self.board)):
            print(self.board[i])

    def move_pieces(self, start):
        row = 1
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

    def extra_turn(self, end):
        if end == [1, 6]:
            return True
        else:
            return False

    def capture(self, end):
        if end[0] == 1:
            if self.board[end[0]][end[1]] == 1:
                if self.board[0][end[1]] > 0:
                    capture_sum = self.board[end[0]][end[1]] + self.board[0][end[1]]
                    self.board[1][6] += capture_sum
                    self.board[end[0]][end[1]] = 0
                    self.board[0][end[1]] = 0

    def end_game(self):
        sumtop = 0
        sumbot = 0
        for i in range(5):
            sumtop += self.board[0][i+1]
        if sumtop == 0:
            return True
        elif sumtop != 0:
            for z in range(4):
                sumbot += self.board[1][z]
            if sumbot == 0:
                return True
        else:
            return False

    def flip_board(self):
        temp = self.board[1]
        self.board[1] = self.board[0]
        self.board[0] = temp
        self.board[0] = self.board[0].reverse()
        self.board[1] = self.board[1].reverse()