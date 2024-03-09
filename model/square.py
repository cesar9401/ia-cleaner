class Square:
    pos_x = 0
    pos_y = 0
    dirty = False
    cleaner = None

    def __init__(self, pos_x, pos_y, dirty):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dirty = dirty

    def set_cleaner(self, cleaner):
        self.cleaner = cleaner
        cleaner.accept(self)

    def remove_cleaner(self):
        if self.cleaner is not None:
            # remove square
            self.cleaner.remove_square()
            # remove cleaner
            self.cleaner = None
