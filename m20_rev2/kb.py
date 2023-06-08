import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class mlego(_KMKKeyboard):
    col_pins = (
        board.GP1,
        board.GP6,
        board.GP7,
        board.GP8,
    )

    row_pins = (
        board.GP9,
        board.GP10,
        board.GP11,
        board.GP12,
        board.GP13,
    )

    diode_orientation = DiodeOrientation.COL2ROW

    lower_led = board.GP25
    raise_led = board.GP14

    en_a = board.GP4
    en_b = board.GP5

    scl = board.GP3
    sda = board.GP2
