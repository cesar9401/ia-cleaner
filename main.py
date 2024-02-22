import threading
import time
from random import randrange

from model.board import Board
from model.cleaner import Cleaner

board = Board(1, 2)
board.print_board()
cleaner = Cleaner()


def game(cleaner1, seconds):
    # print(end='\n')
    while True:
        cur_x, cur_y = cleaner1.cur_x, cleaner1.cur_y
        right, down = cleaner1.right, cleaner1.down

        # print(f'x: {cur_x}, y: {cur_y}')
        # print(f'right: {right}, down: {down}')
        board.board[cur_x][cur_y].set_cleaner(cleaner1)
        # board.print_board()

        # TODO: move
        if right and len(board.board) - 1 > cur_x:
            cleaner1.cur_x = cur_x + 1
            cleaner1.cur_y = cur_y
        elif not right and cur_x > 0:
            cleaner1.cur_x = cur_x - 1
            cleaner1.cur_y = cur_y
        elif right and len(board.board) - 1 == cur_x:
            if len(board.board[cur_x]) - 1 == cur_y:
                cleaner1.cur_x = cur_x - 1
                cleaner1.cur_y = cur_y
                cleaner1.right = not right
                cleaner1.down = not down
            else:
                cleaner1.cur_x = cur_x
                cleaner1.right = not right
                if down:
                    cleaner1.cur_y = cur_y + 1
                elif not down and cur_y > 0:
                    cleaner1.cur_y = cur_y - 1
                elif cur_y == 0 or len(board.board[cur_x]) - 1 == cur_y:
                    cleaner1.down = not down
        elif not right and cur_x == 0:
            if len(board.board[cur_x]) - 1 == cur_y and cur_y > 0:
                cleaner1.cur_x = cur_x
                cleaner1.cur_y = cur_y - 1
                cleaner1.right = not right
            elif down:
                cleaner1.cur_x = cur_x
                cleaner1.cur_y = cur_y + 1
                cleaner1.right = not right
            elif not down:
                cleaner1.cur_x = cur_x + 1
                cleaner1.cur_y = cur_y
                cleaner1.down = not down
                cleaner1.right = not right
        elif down and len(board.board[cur_x]) - 1 > cur_y:
            cleaner1.cur_x = cur_x
            cleaner1.cur_y = cur_y + 1
        elif not down and cur_y > 0:
            cleaner1.cur_x = cur_x
            cleaner1.cur_y = cur_y - 1
        elif down and len(board.board[cur_x]) - 1 == cur_y:
            # TODO: update here
            cleaner1.cur_y = cur_y
            cleaner1.cur_x = cur_x + 1
            cleaner1.down = not down
        elif not down and cur_y == 0:
            # TODO: update here
            cleaner1.cur_y = cur_y
            cleaner1.cur_x = cur_x + 1
            cleaner1.down = not down
        else:
            print('else')

        time.sleep(seconds)
        board.board[cur_x][cur_y].remove_cleaner()


def dirty_board(board1, seconds):
    while True:
        i, j = randrange(board1.total_x), randrange(board1.total_y)
        square = board1.board[i][j]
        if not square.dirty and square.cleaner is None:
            board1.board[i][j].dirty = not board1.board[i][j].dirty
        time.sleep(seconds)


def print_board(board1, seconds):
    while True:
        board1.print_board()
        time.sleep(seconds)


print_thread = threading.Thread(target=print_board, args=(board, 2,))
dirty_thread = threading.Thread(target=dirty_board, args=(board, 2,))
game_thread = threading.Thread(target=game, args=(cleaner, 4,))

print_thread.start()
game_thread.start()
dirty_thread.start()
