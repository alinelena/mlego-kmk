import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class mlego(_KMKKeyboard):
    col_pins = (
        board.GP1,
        board.GP6,
        board.GP7,
        board.GP8,
        board.GP9,
        board.GP15,
        board.GP14,
        board.GP13,
        board.GP12,
        board.GP11,
        board.GP10,
        board.GP17,
        board.GP21,
    )

    row_pins = (
        board.GP22,
        board.GP16,
        board.GP18,
        board.GP19,
        board.GP20,
    )

    diode_orientation = DiodeOrientation.COL2ROW

    lower_led = board.GP28
    raise_led = board.GP27
    caps_led = board.GP25

    en_a = board.GP4
    en_b = board.GP5

    scl = board.GP3
    sda = board.GP2
