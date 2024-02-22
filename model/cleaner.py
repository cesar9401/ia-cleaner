class Cleaner:
    cur_x = 0
    cur_y = 0
    right = True
    down = True

    def __init__(self):
        pass

    def visit(self, square):
        self.cur_x = square.pos_x
        self.cur_y = square.pos_y

        # clean
        if square.dirty:
            square.dirty = False

    def print(self):
        print(f'x: {self.cur_x}, y: {self.cur_y}')
        print(f'right: {self.right}, down: {self.down}')
