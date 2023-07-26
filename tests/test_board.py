from src.board import Board


board_width = 12
board_height = 20
board = Board(board_width, board_height)


class TestBoard:
    def test_get_board_generates_a_board(self):

        assert len(board.cells) == board_width
        assert all([len(board.cells[i]) == board_height for i in range(board_width)])

    def test_can_set_a_cell_value(self):
        board.set_cell(2, 2, False)

        assert not board.cells[2][2]

    def test_can_get_a_cell_value(self):
        board.set_cell(2, 2, True)

        assert board.is_cell_alive(2, 2)

    def test_get_number_of_neighbors_1(self):
        set_neighbors(board, 1, 1, False)

        assert board.get_number_of_neighbors(1, 1) == 0

    def test_get_number_of_neighbors_2(self):
        set_neighbors(board, 2, 2, False)
        board.set_cell(3, 3, True)

        assert board.get_number_of_neighbors(2, 2) == 1

    def test_get_number_of_neighbors_3(self):
        set_neighbors(board, 2, 2, False)
        board.set_cell(2, 2, True)
        board.set_cell(3, 3, True)

        assert board.get_number_of_neighbors(2, 2) == 1

    def test_get_number_of_neighbors_4(self):
        set_neighbors(board, 3, 3, True)
        board.set_cell(3, 3, False)

        assert board.get_number_of_neighbors(3, 3) == 8

    def test_get_number_of_neighbors_5(self):
        set_neighbors(board, 0, 0, True)
        board.set_cell(board_width-1, board_height-1, False)

        assert board.get_number_of_neighbors(0, 0) == 7


def set_neighbors(b: Board, x: int, y: int, value: bool) -> None:
    neighbors_coordinates = [
        [x - 1, y - 1],
        [x, y - 1],
        [x + 1, y - 1],
        [x - 1, y],
        [x + 1, y],
        [x - 1, y + 1],
        [x, y + 1],
        [x + 1, y + 1],
    ]
    for x_, y_ in neighbors_coordinates:
        b.set_cell(x_, y_, value)
