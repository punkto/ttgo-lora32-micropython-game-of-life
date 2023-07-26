from src.board import Board
from src.game_of_life import will_be_cell_alive


board_width = 3
board_height = 3
board = Board(board_width, board_height)


class TestGameOfLife:
    def setup_method(self):
        clear_board()

    def teardown_method(self):
        clear_board()

    def test_will_be_cell_alive_cell_dead_no_neighbors(self):
        assert will_be_cell_alive(board, 1, 1) == False

    def test_will_be_cell_alive_cell_dead_1_neighbor(self):
        cell_has_neighbors(1)
        assert will_be_cell_alive(board, 1, 1) == False

    def test_will_be_cell_alive_cell_dead_2_neighbors(self):
        cell_has_neighbors(2)
        assert will_be_cell_alive(board, 1, 1) == False

    def test_will_be_cell_alive_cell_dead_3_neighbors(self):
        cell_has_neighbors(3)
        assert will_be_cell_alive(board, 1, 1) == True

    def test_will_be_cell_alive_cell_dead_4_neighbors(self):
        cell_has_neighbors(4)
        assert will_be_cell_alive(board, 1, 1) == False

    def test_will_be_cell_alive_cell_dead_5_neighbors(self):
        cell_has_neighbors(5)
        assert will_be_cell_alive(board, 1, 1) == False

    def test_will_be_cell_alive_cell_dead_6_neighbors(self):
        cell_has_neighbors(6)
        assert will_be_cell_alive(board, 1, 1) == False

    def test_will_be_cell_alive_cell_dead_7_neighbors(self):
        cell_has_neighbors(7)
        assert will_be_cell_alive(board, 1, 1) == False

    def test_will_be_cell_alive_cell_dead_8_neighbors(self):
        cell_has_neighbors(8)
        assert will_be_cell_alive(board, 1, 1) == False

    def test_will_be_cell_alive_cell_alive_no_neighbors(self):
        cell_is_alive()
        assert will_be_cell_alive(board, 1, 1) == False

    def test_will_be_cell_alive_cell_alive_1_neighbor(self):
        cell_is_alive()
        cell_has_neighbors(1)
        assert will_be_cell_alive(board, 1, 1) == False

    def test_will_be_cell_alive_cell_alive_2_neighbors(self):
        cell_is_alive()
        cell_has_neighbors(2)
        assert will_be_cell_alive(board, 1, 1) == True

    def test_will_be_cell_alive_cell_alive_3_neighbors(self):
        cell_is_alive()
        cell_has_neighbors(3)
        assert will_be_cell_alive(board, 1, 1) == True

    def test_will_be_cell_alive_cell_alive_4_neighbors(self):
        cell_is_alive()
        cell_has_neighbors(4)
        assert will_be_cell_alive(board, 1, 1) == False

    def test_will_be_cell_alive_cell_alive_5_neighbors(self):
        cell_is_alive()
        cell_has_neighbors(5)
        assert will_be_cell_alive(board, 1, 1) == False

    def test_will_be_cell_alive_cell_alive_6_neighbors(self):
        cell_is_alive()
        cell_has_neighbors(6)
        assert will_be_cell_alive(board, 1, 1) == False

    def test_will_be_cell_alive_cell_alive_7_neighbors(self):
        cell_is_alive()
        cell_has_neighbors(7)
        assert will_be_cell_alive(board, 1, 1) == False

    def test_will_be_cell_alive_cell_alive_8_neighbors(self):
        cell_is_alive()
        cell_has_neighbors(8)
        assert will_be_cell_alive(board, 1, 1) == False



def clear_board():
    board.set_cell(0, 0, False)
    board.set_cell(1, 0, False)
    board.set_cell(2, 0, False)
    board.set_cell(0, 1, False)
    board.set_cell(1, 1, False)  # center
    board.set_cell(2, 1, False)
    board.set_cell(0, 2, False)
    board.set_cell(1, 2, False)
    board.set_cell(2, 2, False)


def cell_is_alive():
    board.set_cell(1, 1, True)


def cell_has_neighbors(n: int) -> None:
    if n == 0:
        return
    board.set_cell(0, 0, True)
    if n == 1:
        return
    board.set_cell(1, 0, True)
    if n == 2:
        return
    board.set_cell(2, 0, True)
    if n == 3:
        return
    board.set_cell(0, 1, True)
    if n == 4:
        return
    board.set_cell(2, 1, True)
    if n == 5:
        return
    board.set_cell(0, 2, True)
    if n == 6:
        return
    board.set_cell(1, 2, True)
    if n == 7:
        return
    board.set_cell(2, 2, True)
