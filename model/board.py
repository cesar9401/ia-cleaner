import random

from model.square import Square


class Board:
    total_x = 1
    total_y = 1
    board = None

    def __init__(self, total_x, total_y):
        self.total_x = total_x
        self.total_y = total_y
        self.board = []

        for i in range(total_x):
            row = []
            for j in range(total_y):
                dirty = random.random() > 0.7
                square = Square(i, j, dirty)
                row.insert(len(row), square)
            self.board.insert(len(self.board), row)

    def print_board(self):
        for i in range(self.total_x):
            for j in range(self.total_y):
                if self.board[i][j].cleaner is not None and self.board[i][j].dirty:
                    print('c', end=' ')
                elif self.board[i][j].cleaner is not None and not self.board[i][j].dirty:
                    print('-', end=' ')
                elif self.board[i][j].dirty:
                    print('x', end=' ')
                else:
                    print('o', end=' ')
            print()
        print()
