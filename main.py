from model.board import Board
from model.cleaner import Cleaner

board = Board(4, 5)
# board.print_board()

cleaner = Cleaner()

# board.print_board()


def game():
    print('here', end='\n')
    cur_x, cur_y = cleaner.cur_x, cleaner.cur_y
    right, down = cleaner.right, cleaner.down
    print(f'x: {cur_x}, y: {cur_y}')

    board.board[cur_x][cur_y].set_cleaner(cleaner)
    board.print_board()
    board.board[cur_x][cur_y].remove_cleaner()

    # TODO: move
    if right and len(board.board) - 1 > cur_x:
        cleaner.cur_x = cur_x + 1
        cleaner.cur_y = cur_y
    elif not right and len(board.board) - 1 < cur_x:
        cleaner.cur_x = cur_x - 1
        cleaner.cur_y = cur_y
    elif right and len(board.board) - 1 == cur_x:
        cleaner.cur_x = cleaner.cur_x
        cleaner.cur_y = cur_y + 1
        cleaner.right = not cleaner.right
    elif not right and cur_x == 0:
        cleaner.cur_x = cur_x + 1
        cleaner.cur_y = cur_y
        cleaner.right = not cleaner.right
    elif down and len(board.board[cur_x]) - 1 > cur_y:
        cleaner.cur_x = cur_x
        cleaner.cur_y = cur_y + 1
    elif not down and len(board.board[cur_x]) - 1 < cur_y:
        cleaner.cur_x = cur_x
        cleaner.cur_y = cur_y - 1
    elif down and len(board.board[cur_x]) - 1 == cur_y:
        cleaner.cur_y = cleaner.cur_y
        cleaner.cur_x = cur_x + 1
        cleaner.down = not cleaner.down
    elif not down and cur_y == 0:
        cleaner.cur_y = cur_y + 1
        cleaner.cur_x = cur_x
        cleaner.down = not cleaner.down
    else:
        print('else')


    # cleaner.print()
    # if right and len(board.board) - 1 > cur_x:
    #     cleaner.cur_x = cur_x + 1
    #     cleaner.cur_y = cur_y
    # elif not right and len(board.board) - 1 <= cur_x:
    #     cleaner.cur_x = cur_x - 1
    #     cleaner.cur_y = cur_y
    # elif down and len(board.board[cur_x]) - 1 > cur_y:
    #     cleaner.cur_x = cur_x
    #     cleaner.cur_y = cur_y + 1
    # elif not down and len(board.board[cur_x]) - 1 <= cur_y:
    #     cleaner.cur_x = cur_x
    #     cleaner.cur_y = cur_y - 1
    # elif right and len(board.board[cur_x]) - 1 == cur_y:
    #     cleaner.cur_y = cur_y
    #     cleaner.cur_x = cur_x + 1
    #     cleaner.down = not cleaner.down
    # elif not right and cur_y == 0:
    #     cleaner.cur_y = cur_y
    #     cleaner.cur_x = cur_x - 1
    #     cleaner.down = not cleaner.down
    # elif down and len(board.board) - 1 == cur_x:
    #     cleaner.cur_y = cur_y + 1
    #     cleaner.cur_x = cur_x
    #     cleaner.right = not cleaner.right
    # elif not down and cur_x == 0:
    #     cleaner.cur_y = cur_y - 1
    #     cleaner.cur_x = cur_x
    #     cleaner.right = not cleaner.right
    # else:
    #     print('else')


game()
game()
game()
game()
game()
game()
game()
game()
game()
