import sys
sys.path.insert(0,'./src/')

from time import sleep
from src.board import Board
from src.game_of_life import update_board


def paint_board(b: Board):
    print("--------------------------------")
    for y in range(b.height):
        for x in range(b.width):
            if b.is_cell_alive(x, y):
                print("A", end="")
            else:
                print(" ", end="")
        print()
    print("--------------------------------")
    

oled_width = 80
oled_heigh = 20
board_width = oled_width
board_height = oled_heigh

board_1 = Board(width=oled_width, height=oled_heigh, blank=True)
board_1.add_glider(1, 1)

board_2 = Board(width=oled_width, height=oled_heigh, blank=True)

i = 0
while True:
    sleep(1)
    paint_board(board_1)
    update_board(board_1, board_2)
    print(i)
    i = i +1

    sleep(1)
    paint_board(board_2)
    update_board(board_2, board_1)
    print(i)
    i = i +1

    #if i > 20:
    #    exit()
