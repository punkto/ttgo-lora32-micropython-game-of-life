from board import Board
from game_of_life import update_board
from display import get_display, paint_board



oled_width = 128
oled_heigh = 64
board_width = oled_width
board_height = oled_heigh
oled = get_display(oled_width, oled_heigh)

board_1 = Board(width=oled_width, height=oled_heigh, blank=False)
#board_1.add_glider(1, 1)

board_2 = Board(width=oled_width, height=oled_heigh, blank=True)

i = 0
while True:
    paint_board(board_1, i, oled)
    update_board(board_1, board_2)
    i = i +1

    paint_board(board_2, i, oled)
    update_board(board_2, board_1)
    i = i +1