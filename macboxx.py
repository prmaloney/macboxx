from pynput import keyboard
import melee
from melee.enums import Button

console = melee.Console('./Slippi Dolphin.app/')

controller = melee.Controller(console=console, port=1)

console.run()
console.connect()

controller.connect()

keymap = {
    'w': 'CONTROL_UP',
    'a': 'CONTROL_LEFT',
    's': 'CONTROL_DOWN',
    'd': 'CONTROL_RIGHT',
    'j': 'BUTTON_A',
    'o': 'BUTTON_B',
    'i': 'BUTTON_Z',
    'k': 'BUTTON_X',
    keyboard.Key.space: 'BUTTON_L',
    '1': 'BUTTON_R',
    ';': 'C_UP',
    ':': 'C_UP',
    ',': 'C_DOWN',
    'l': 'C_RIGHT',
    'n': 'C_LEFT',
    keyboard.Key.enter: 'START',
    keyboard.Key.shift_l: 'MOD_Y',
    keyboard.Key.shift_r: 'MOD_X',
    keyboard.Key.up: 'D_UP',
    keyboard.Key.left: 'D_LEFT',
    keyboard.Key.down: 'D_DOWN',
    keyboard.Key.right: 'D_RIGHT'
}

control_up = False
control_left = False
control_down = False
control_right = False

modx = False
mody = False

c_up = False
c_left = False
c_down = False
c_right = False


def tilt_c():
    stick_x = 0.5
    stick_y = 0.5

    if c_up:
        stick_y += 0.5
    if c_down:
        stick_y -= 0.5
    if c_left:
        stick_x -= 0.5
    if c_right:
        stick_x += 0.5

    controller.tilt_analog(Button.BUTTON_C, stick_x, stick_y)


def tilt_analog():
    mod_up_tilt = 0.22
    mod_x_tilt = 0.18
    mod_down_tilt = 0.25
    full_y_tilt = 0.5
    full_x_tilt = 0.4

    stick_x = 0.5
    if control_left:
        stick_x -= mod_x_tilt if modx else full_x_tilt

    if control_right:
        stick_x += mod_x_tilt if modx else full_x_tilt

    stick_y = 0.5
    if control_up:
        stick_y += mod_up_tilt if mody else full_y_tilt

    if control_down:
        stick_y -= mod_down_tilt if mody else full_y_tilt

    controller.tilt_analog(Button.BUTTON_MAIN, stick_x, stick_y)


def on_press(key):
    try:
        input = keymap.get(key.char.lower(), None)
    except AttributeError:
        input = keymap.get(key, None)

    global modx, mody, control_left, control_right, control_up, control_down, c_up, c_left, c_down, c_right

    match input:
        case 'CONTROL_UP':
            control_up = True
        case 'CONTROL_LEFT':
            control_left = True
        case 'CONTROL_DOWN':
            control_down = True
        case 'CONTROL_RIGHT':
            control_right = True
        case 'C_UP':
            c_up = True
        case 'C_LEFT':
            c_left = True
        case 'C_DOWN':
            c_down = True
        case 'C_RIGHT':
            c_right = True
        case 'BUTTON_A':
            controller.press_button(Button.BUTTON_A)
        case 'BUTTON_B':
            controller.press_button(Button.BUTTON_B)
        case 'BUTTON_Z':
            controller.press_button(Button.BUTTON_Z)
        case 'BUTTON_X':
            controller.press_button(Button.BUTTON_X)
        case 'BUTTON_L':
            controller.press_button(Button.BUTTON_L)
        case 'BUTTON_R':
            controller.press_button(Button.BUTTON_R)
        case 'START':
            controller.press_button(Button.BUTTON_START)
        case 'MOD_X':
            modx = True
        case 'MOD_Y':
            mody = True
        case 'D_UP':
            controller.press_button(Button.BUTTON_D_UP)
        case 'D_LEFT':
            controller.press_button(Button.BUTTON_D_LEFT)
        case 'D_DOWN':
            controller.press_button(Button.BUTTON_D_DOWN)
        case 'D_RIGHT':
            controller.press_button(Button.BUTTON_D_RIGHT)

    tilt_analog()
    tilt_c()
    controller.flush()


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        console.stop()
        return False
    try:
        input = keymap.get(key.char.lower(), None)
    except AttributeError:
        input = keymap.get(key, None)

    global modx, mody, control_left, control_right, control_up, control_down, c_up, c_left, c_down, c_right

    match input:
        case 'CONTROL_UP':
            control_up = False
        case 'CONTROL_LEFT':
            control_left = False
        case 'CONTROL_DOWN':
            control_down = False
        case 'CONTROL_RIGHT':
            control_right = False
        case 'C_UP':
            c_up = False
        case 'C_LEFT':
            c_left = False
        case 'C_DOWN':
            c_down = False
        case 'C_RIGHT':
            c_right = False
        case 'BUTTON_A':
            controller.release_button(Button.BUTTON_A)
        case 'BUTTON_B':
            controller.release_button(Button.BUTTON_B)
        case 'BUTTON_Z':
            controller.release_button(Button.BUTTON_Z)
        case 'BUTTON_X':
            controller.release_button(Button.BUTTON_X)
        case 'BUTTON_L':
            controller.release_button(Button.BUTTON_L)
        case 'BUTTON_R':
            controller.release_button(Button.BUTTON_R)
        case 'START':
            controller.release_button(Button.BUTTON_START)
        case 'MOD_X':
            modx = False
        case 'MOD_Y':
            mody = False
        case 'D_UP':
            controller.release_button(Button.BUTTON_D_UP)
        case 'D_LEFT':
            controller.release_button(Button.BUTTON_D_LEFT)
        case 'D_DOWN':
            controller.release_button(Button.BUTTON_D_DOWN)
        case 'D_RIGHT':
            controller.release_button(Button.BUTTON_D_RIGHT)

    tilt_analog()
    tilt_c()
    controller.flush()


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
