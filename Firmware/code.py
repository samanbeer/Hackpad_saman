import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.RGB import RGB

keyboard = KMKKeyboard()

keyboard.pins = [
    board.A0,
    board.A1,
    board.A2,
    board.A3,
    board.D6,
    board.D7,
]

keyboard.diode_orientation = DiodeOrientation.COL2ROW

rgb = RGB(
    pixel_pin=board.D3,  
    num_pixels=6,          
    val_default=100,        # Brighteness (0-255)
)
keyboard.extensions.append(rgb)

keyboard.keymap = [
    [
        KC.PAUSE,          # Still thinking what to add :)
        KC.,
        KC.,
        KC.LCTL(KC.C),
        KC.LCTL(KC.V),
        KC.MUTE,
    ]
]

if __name__ == '__main__':
    keyboard.go()