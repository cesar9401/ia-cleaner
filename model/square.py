class Square:
    pos_x = 0
    pos_y = 0
    dirty = False
    cleaner = None

    def __init__(self, pos_x, pos_y, dirty):
        self.posX = pos_x
        self.posY = pos_y
        self.dirty = dirty

    def set_cleaner(self, cleaner):
        self.cleaner = cleaner
        cleaner.visit(self)

    def remove_cleaner(self):
        if self.cleaner is not None:
            self.cleaner = None
