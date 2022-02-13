from random import randint


def get_random_cells(width, height):
    b = [[False for _ in range(height)] for _ in range(width)]

    for x in range(width):
        for y in range(height):
            if randint(0, 10) > 8:
                b[x][y] = True

    return b


def get_blank_cells(width, height):
    b = [[False for _ in range(height)] for _ in range(width)]

    for x in range(width):
        for y in range(height):
            b[x][y] = False

    return b


class Board:
    def __init__(self, width: int, height: int, blank: bool=False) -> None:
        self.width = width
        self.height = height
        if not blank:
            self.cells = get_random_cells(width, height)
        else:
            self.cells = get_blank_cells(width, height)

    def set_cell(self, x: int, y: int, alive: bool) -> None:
        self.cells[x][y] = alive

    def is_cell_alive(self, x: int, y: int) -> bool:
        return self.cells[x][y]

    def get_number_of_neighbors(self, x: int, y: int) -> int:
        neighbors = 0
        for x_, y_ in self.get_neighbors_coordinates(x, y):
            neighbors = neighbors + self.is_cell_alive(x_, y_)
        return neighbors

    def get_neighbors_coordinates(self, x, y):
        x_minus_one = (x - 1) % self.width
        x_plus_one = (x + 1) % self.width
        y_minus_one = (y - 1) % self.height
        y_plus_one = (y + 1) % self.height

        return [
            [x_minus_one, y_minus_one],
            [x, y_minus_one],
            [x_plus_one, y_minus_one],
            [x_minus_one, y],
            [x_plus_one, y],
            [x_minus_one, y_plus_one],
            [x, y_plus_one],
            [x_plus_one, y_plus_one],
        ]

    def add_glider(self, x, y) -> None:
        self.set_cell(x, y, False)
        self.set_cell(x+1, y, True)
        self.set_cell(x+2, y, False)
        self.set_cell(x, y+1, False)
        self.set_cell(x+1, y+1, False)  # center
        self.set_cell(x+2, y+1, True)
        self.set_cell(x, y+2, True)
        self.set_cell(x+1, y+2, True)
        self.set_cell(x+2, y+2, True)
