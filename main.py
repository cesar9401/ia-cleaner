from model.board import Board
from model.cleaner import Cleaner

board = Board(3, 3)
# board.print_board()

cleaner = Cleaner()

# board.print_board()

def game(cleaner):
    print(end='\n')
    cur_x, cur_y = cleaner.cur_x, cleaner.cur_y
    right, down = cleaner.right, cleaner.down

    print(f'x: {cur_x}, y: {cur_y}')
    print(f'right: {right}, down: {down}')
    board.board[cur_x][cur_y].set_cleaner(cleaner)
    board.print_board()
    board.board[cur_x][cur_y].remove_cleaner()

    # TODO: move
    if right and len(board.board) - 1 > cur_x:
        cleaner.cur_x = cur_x + 1
        cleaner.cur_y = cur_y
    elif not right and cur_x > 0:
        cleaner.cur_x = cur_x - 1
        cleaner.cur_y = cur_y
    elif right and len(board.board) - 1 == cur_x:
        if len(board.board[cur_x]) - 1 == cur_y:
            cleaner.cur_x = cur_x - 1
            cleaner.cur_y = cur_y
            cleaner.right = not right
            cleaner.down = not down
        else:
            cleaner.cur_x = cur_x
            cleaner.right = not right
            if down:
                cleaner.cur_y = cur_y + 1
            else:
                cleaner.cur_y = cur_y - 1
    elif not right and cur_x == 0:
        if len(board.board[cur_x]) - 1 == cur_y:
            cleaner.cur_x = cur_x
            cleaner.cur_y = cur_y - 1
            cleaner.right = not right
        else:
            cleaner.cur_x = cur_x
            cleaner.cur_y = cur_y + 1
            cleaner.right = not right
    elif down and len(board.board[cur_x]) - 1 > cur_y:
        cleaner.cur_x = cur_x
        cleaner.cur_y = cur_y + 1
    elif not down and cur_y > 0:
        cleaner.cur_x = cur_x
        cleaner.cur_y = cur_y - 1
        print('down 1')
    elif down and len(board.board[cur_x]) - 1 == cur_y:
        cleaner.cur_y = cur_y
        cleaner.cur_x = cur_x + 1
        cleaner.down = not down
        print('down 2')
    elif not down and cur_y == 0:
        cleaner.cur_y = cur_y
        cleaner.cur_x = cur_x + 1
        cleaner.down = not down
    else:
        print('else')

game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
game(cleaner)
