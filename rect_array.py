import copy


def array2d_init(width, height, val):
    return [copy.deepcopy([copy.deepcopy(val) for x in range(width)]) for y in range(height)]


def index_wh(screen_width, screen_height, rect_width, rect_height):
    index_width = int(screen_width / rect_width)
    index_height = int(screen_height / rect_height)
    return index_width, index_height


class array2d:
    def init(self, screen_width, screen_height, rect_width, rect_height):
        self.index_width, self.index_height = index_wh(screen_width, screen_height, rect_width, rect_height)
    def make(self, inner):
        self.array2d = array2d_init(self.index_width, self.index_height, inner)


class rect_array2d(array2d):
    def __init__(self, screen_width, screen_height, rect_width, rect_height):
        self.init(screen_width, screen_height, rect_width, rect_height)
        inner = [0 for x in range(4)]
        self.make(inner)
        for y in range(self.index_height):
            for x in range(self.index_width):
                self.array2d[y][x][0] = rect_width * x# x
                self.array2d[y][x][1] = rect_height * y# y
                self.array2d[y][x][2] = rect_width# width
                self.array2d[y][x][3] = rect_height# height


class data_array2d(array2d):
    def __init__(self, screen_width, screen_height, rect_width, rect_height):
        self.init(screen_width, screen_height, rect_width, rect_height)
        inner = 'black'
        self.make(inner)
