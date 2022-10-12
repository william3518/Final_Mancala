class Gameboard:
    def __init__(self):
        self.board = [[0, 4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4, 0]]

    def show_board(self):
        for i in range(len(self.board)):
            print(self.board[i])

    def move_pieces(self, start):
        self.row = 1
        self.piece_num = self.board[self.row][start]
        self.board[self.row][start] = 0
        self.board[self.row][start+1]
        while self.piece_num > 0:
            if self.row == 1 and start <= 5:
                self.board[self.row][start] += 1
                start += 1
            elif self.row == 1 and start == 6:
                self.board[self.row][start] += 1
                self.row -= 1
            elif self.row == 0 and start >= 1:
                self.board[self.row][start] += 1
                start -= 1
            else:
                self.board[self.row][start] += 1
                self.row += 1
            self.piece_num -= 1