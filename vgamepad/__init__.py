import sys
from vgamepad.win.vigem_commons import VIGEM_TARGET_TYPE, XUSB_BUTTON, DS4_BUTTONS, DS4_SPECIAL_BUTTONS, DS4_DPAD_DIRECTIONS

if sys.platform == 'win32':
    from vgamepad.win.virtual_gamepad import VX360Gamepad, VDS4Gamepad
elif sys.platform == 'linux':  # Linux
    from vgamepad.lin.virtual_gamepad import VX360Gamepad, VDS4Gamepad
