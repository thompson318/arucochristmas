"""
An interface between skarucotracker and a raspberry pi 
Christmas tree
"""

from gpiozero import LEDBoard #pylint:disable=import-error

from arucochristmas.aruco import init_camera_and_tracker, get_marker_pos

def light_led(tree, led_no):
    print("lighting", led_no)
    tree.leds[led_no].on()

def delight_led(tree, led_no):
    if led_no > 25:
        led_no -= 26
    print("de-lighting", led_no)
    tree.leds[led_no].off()

if __name__ == '__main__':

    tree=LEDBoard(*range(2,28), pwm=False)
    artracker, camera = init_camera_and_tracker()
    while True:
        ok, x_ord, y_ord = get_marker_pos(artracker, camera)
        if ok:
            print ("\n[x, y] = ", x_ord, y_ord)
            light_led(tree, int(x_ord)%26)
            delight_led(tree, int(x_ord)%26 + 1)
        else:
            print('.',end='')

