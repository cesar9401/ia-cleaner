class Cleaner:
    cur_x = 0
    cur_y = 0
    square = None

    def __init__(self):
        pass

    def accept(self, square):
        self.cur_x = square.pos_x
        self.cur_y = square.pos_y
        self.square = square

    def remove_square(self):
        self.square = None

    def get_perception(self):
        if not self.square:
            return 'nothing'

        if self.square.dirty:
            if self.square.pos_y == 0:
                return 'left_dirty'
            if self.square.pos_x == 0:
                return 'right_dirty'
        else:
            if self.square.pos_y == 0:
                return 'left_clean'
            if self.square.pos_x == 0:
                return 'right_clean'

        return 'nothing'
