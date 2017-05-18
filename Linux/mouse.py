import time

import uinput

def main(muut_x,muut_y):
    events = (
        uinput.REL_X,
        uinput.REL_Y,
        uinput.BTN_LEFT,
        uinput.BTN_RIGHT,
        )

    device = uinput.Device(events)

    #for i in range(2):
        # syn=False to emit an "atomic" (5, 5) event.
   # 	device.emit(uinput.REL_X, -2000, syn=False)
    #	device.emit(uinput.REL_Y, -2000)

        # Just for demonstration purposes: shows the motion. In real
        # application, this is of course unnecessary.
    time.sleep(0.01)
    device.emit(uinput.REL_X, muut_x, syn=False)
    device.emit(uinput.REL_Y, muut_y)

muut_x=-500
muut_y=-500
main(muut_x,muut_y)
