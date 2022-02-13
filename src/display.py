from machine import Pin, SoftI2C
import ssd1306
from time import sleep_ms
from board import Board

COLOR_WHITE = 1

def reset_oled() -> None:
    pin_reset = Pin(16, Pin.OUT)
    pin_reset.value(0)
    sleep_ms(10)
    pin_reset.value(1)


def get_display(width: int, height: int) -> ssd1306.SSD1306_I2C:
    # ESP32 Pin assignment
    i2c = SoftI2C(scl=Pin(15), sda=Pin(4))

    reset_oled()

    return ssd1306.SSD1306_I2C(width, height, i2c)


def paint_board(b: Board, i: int, o: ssd1306.SSD1306_I2C) -> None:
    for x in range(b.width):
        for y in range(b.height):
            if b.cells[x][y]:
                o.pixel(x, y, COLOR_WHITE)
            else:
                o.pixel(x, y, 0)
    o.text(str(i), 0, 0)
    o.show()
