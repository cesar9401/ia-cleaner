# status: 'left_dirty', 'right_dirty', 'left_clean', 'right_clean'
# perceptions: 'left_dirty', 'right_dirty', 'left_clean', 'right_clean', 'nothing'

import threading
import time
from random import randrange

from model.board import Board
from model.cleaner import Cleaner

rules = {
    'left_dirty': 'clean_left',
    'right_dirty': 'clean_right',
    'left_clean': 'move_to_right',
    'right_clean': 'move_to_left',
    'nothing': 'do_nothing'
}

actions = {
    'clean_left': 'cleaning left',
    'clean_right': 'cleaning right',
    'move_to_left': 'moving to the left',
    'move_to_right': 'moving to the right',
    'do_nothing': 'resting...'
}

model = [
    ['left_dirty', 'clean_left', 'left_clean', 'move_to_right'],
    ['left_dirty', 'clean_left', 'left_dirty', 'clean_left'],
    ['right_dirty', 'clean_right', 'right_clean', 'move_to_left'],
    ['right_dirty', 'clean_right', 'right_dirty', 'clean_right'],
    ['left_clean', 'move_to_right', 'right_dirty', 'clean_right'],
    ['left_clean', 'move_to_right', 'right_clean', 'do_nothing'],
    ['right_clean', 'move_to_left', 'left_dirty', 'clean_left'],
    ['right_clean', 'move_to_left', 'left_clean', 'do_nothing'],
    ['left_clean', 'move_to_right', 'nothing', 'do_nothing'],
    ['right_clean', 'move_to_left', 'nothing', 'do_nothing'],
    ['left_clean', 'move_to_right', 'left_clean', 'move_to_right'],
    ['right_clean', 'move_to_left', 'right_clean', 'move_to_left'],
    ['right_clean', 'do_nothing', 'right_clean', 'do_nothing'],
    ['left_clean', 'do_nothing', 'left_clean', 'do_nothing'],
    ['right_clean', 'do_nothing', 'right_dirty', 'clean_right'],
    ['left_clean', 'do_nothing', 'left_dirty', 'clean_left'],
]

cleaner = Cleaner()
board = Board(1, 2, cleaner)

cur_status = cleaner.get_perception()
cur_action = rules[cur_status]


def find_in_model(status, action, perception):
    print(f'find_in_model: {status}, action: {action}, perception: {perception}')

    for tmp in model:
        if tmp[0] == status and tmp[1] == action and tmp[2] == perception:
            return {'perception': tmp[2], 'action': tmp[3]}

    return {'perception': '', 'action': ''}


def game(seconds):
    global cur_action, cur_status
    while True:
        cur_perception = cleaner.get_perception()
        print(cur_perception)

        status = find_in_model(cur_status, cur_action, cur_perception)
        cur_status = status['perception']
        cur_action = status['action']

        print(status)
        if cur_status != '' and cur_action != '':
            txt_action = actions[cur_action]
            print(txt_action)
        else:
            print('unknown action')
        time.sleep(seconds)
        board.set_action(cur_action)


def dirty_board(seconds):
    while True:
        i, j = randrange(board.total_x), randrange(board.total_y)
        square = board.board[i][j]
        if not square.dirty:
            board.board[i][j].dirty = not board.board[i][j].dirty
        time.sleep(seconds)


def print_board(seconds):
    while True:
        board.print_board()
        time.sleep(seconds)


game_thread = threading.Thread(target=game, args=(2,))
painting_thread = threading.Thread(target=print_board, args=(2,))
dirty_thread = threading.Thread(target=dirty_board, args=(2,))

game_thread.start()
painting_thread.start()
dirty_thread.start()
