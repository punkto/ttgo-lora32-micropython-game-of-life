from .board import Board


def will_be_cell_alive(b: Board, x, y) -> bool:
    neighbors = b.get_number_of_neighbors(x, y)

    if b.is_cell_alive(x, y) and (2 <= neighbors <= 3):
        return True

    if (not b.is_cell_alive(x, y)) and neighbors == 3:
        return True

    return False


def update_board(b: Board, new_board: Board):
    for x in range(b.width):
        for y in range(b.height):
            new_board.set_cell(x,y, will_be_cell_alive(b, x, y))
    return new_board
